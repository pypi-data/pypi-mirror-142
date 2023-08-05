import csv
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
from typing import List, Optional

from logger_cfg import logger
from pydantic import BaseSettings

from .components import AlertComponent, Table
from .core import attach_tables, render_components_html, use_inline_tables


class EmailSettings(BaseSettings):
    sender_email: str
    sender_email_pass: str
    receiver_email: str
    email_attachment_max_size_mb: int = 20
    email_inline_tables_max_rows: int = 2000

    class Config:
        env_prefix = "alerts_"


class SlackSettings(BaseSettings):
    slack_attachment_max_size_mb: int = 20
    slack_inline_tables_max_rows: int = 2000


def send_email(
    subject: str,
    components: List[AlertComponent],
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
    settings: Optional[EmailSettings] = None,
    n_attempts: int = 2,
) -> bool:
    settings = settings or EmailSettings()

    def _construct_message(body: str, tables: List[Table] = []) -> MIMEMultipart:
        message = MIMEMultipart("mixed")
        message["From"] = settings.sender_email
        message["To"] = settings.receiver_email
        message["Subject"] = subject

        body = MIMEText(body, "html")
        message.attach(body)

        if not isinstance(tables, (list, tuple)):
            tables = [tables]

        for table_no, t in enumerate(tables, start=1):
            file = StringIO()
            csv.DictWriter(file, fieldnames=t.header).writerows(t.rows)
            file.seek(0)
            p = MIMEText(file.read(), _subtype="text/csv")
            stem = t.caption[:50].replace(" ", "_") if t.caption else f"table"
            filename = f"{stem}_{table_no}.csv"
            p.add_header("Content-Disposition", f"attachment; filename={filename}")
            message.attach(p)
        return message

    def _send_message(message: MIMEMultipart):
        with smtplib.SMTP_SSL(
            host=smtp_server, port=smtp_port, context=ssl.create_default_context()
        ) as s:
            for _ in range(n_attempts):
                try:
                    s.login(settings.sender_email, settings.sender_email_pass)
                    s.send_message(message)
                    return True
                except smtplib.SMTPSenderRefused as e:
                    logger.error(f"{type(e)} Error sending email: {e}")
        logger.error(
            f"Exceeded max number of attempts ({n_attempts}). Email can not be sent."
        )
        return False

    email_body = render_components_html(
        components, inline_tables_max_rows=settings.email_inline_tables_max_rows
    )

    tables = [t for t in components if isinstance(t, Table)]
    # check if we should add table CSVs as attachments.
    attachment_tables = (
        [tables]
        if not use_inline_tables(tables, settings.email_inline_tables_max_rows)
        and attach_tables(tables, settings.email_attachment_max_size_m)
        else []
    )
    if not _send_message(_construct_message(email_body, tables=attachment_tables)):
        # try sending again, but with tables as attachments.
        subject += f" ({len(attachment_tables)} Failed Attachments)"
        return _send_message(_construct_message(email_body))
    return email_body
