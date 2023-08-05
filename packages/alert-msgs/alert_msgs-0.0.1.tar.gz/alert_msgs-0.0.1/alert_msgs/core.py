import sys
from pathlib import Path
from typing import List

import dominate
from dominate import tags as d
from logger_cfg import logger
from premailer import transform

from .components import AlertComponent, Table


def use_inline_tables(tables: List[Table], inline_tables_max_rows: int) -> bool:
    if sum([len(t.rows) for t in tables]) < inline_tables_max_rows:
        logger.info("Using inline tables.")
        return True
    logger.info("Can not use inline tables because tables have too many rows.")
    return False


def attach_tables(tables: List[Table], attachments_max_size_mb: int) -> bool:
    tables_size_mb = sum([sys.getsizeof(t.rows) for t in tables]) / 10 ** 6
    if tables_size_mb < attachments_max_size_mb:
        logger.info(f"Adding {len(tables)} tables as attachments.")
        return True
    else:
        logger.info(
            f"Can not add tables as attachments because size {tables_size_mb}mb exceeds max {attachments_max_size_mb}"
        )
        return False


def render_components_html(
    components: List[AlertComponent], inline_tables_max_rows: int
) -> str:
    if not isinstance(components, (list, tuple)):
        components = [components]

    doc = dominate.document()
    with doc.head:
        d.style("body {text-align:center;}")
    # check size of tables to determine how best to process.
    tables = [c for c in components if isinstance(c, Table)]
    if len(tables):
        with doc.head:
            d.style(Path(__file__).parent.joinpath("styles", "table.css").read_text())

    with doc:
        for c in components:
            d.div(
                c.html(
                    include_table_rows=use_inline_tables(tables, inline_tables_max_rows)
                )
                if isinstance(c, Table)
                else c.html()
            )
            d.br()

    return transform(doc.render())


def render_components_md(
    components: List[AlertComponent], inline_tables_max_rows: int
) -> str:

    if not isinstance(components, (list, tuple)):
        components = [components]

    return "".join([c.md() for c in components])
