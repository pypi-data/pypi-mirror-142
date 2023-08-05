from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from dominate import tags as d
from logger_cfg import logger


class AlertComponent(ABC):
    @abstractmethod
    def html(self) -> d.html_tag:
        pass

    @abstractmethod
    def md(self) -> str:
        pass


class FontSize(Enum):
    SMALL = "16px"
    MEDIUM = "18px"
    LARGE = "20px"


class FontColors(Enum):
    INFO = "black"
    WARNING = "#ffca28;"
    ERROR = "#C34A2C"
    IMPORTANT = "#1967d3"


@dataclass
class Text(AlertComponent):
    text: str
    size: FontSize = FontSize.MEDIUM
    color: FontColors = FontColors.INFO
    # HTML tag to place text in. e.g. div, p, h1, h2..
    tag: str = "div"

    def html(self):
        tag = getattr(d, self.tag)
        return tag(
            self.text, style=f"font-size:{self.size.value};color:{self.color.value};"
        )

    def md(self):
        if self.size is FontSize.SMALL:
            return self.text
        if self.size is FontSize.MEDIUM:
            return f"## {self.text}"
        if self.size is FontSize.LARGE:
            return f"# {self.text}"


@dataclass
class KVData(AlertComponent):
    data: Dict[str, Any]

    def html(self):
        with (container := d.div()):
            for k, v in self.data.items():
                d.div(
                    d.span(
                        d.b(
                            Text(
                                f"{k}: ", FontSize.LARGE, FontColors.IMPORTANT, "span"
                            ).html()
                        ),
                        Text(v, FontSize.LARGE, tag="span").html(),
                    )
                )
        return container

    def md(self):
        rows = ["|||", "|---:|:---|"]
        for k, v in self.data.items():
            rows.append(f"|**{k}:**|{v}|")
        rows.append("|||")
        return "\n".join(rows)


@dataclass
class Table(AlertComponent):
    rows: Union[List[List[str]], List[Dict[str, Any]]]
    caption: str
    header: Optional[List[str]] = None
    # an SQL query that was used to select `rows`
    query: str = None

    def __post_init__(self):
        self.caption = Text(self.caption, FontSize.LARGE, FontColors.IMPORTANT)

        kv_data = {"Total Rows": len(self.rows)}
        if self.query:
            kv_data["Query"] = self.query
        self.kv_data = KVData(kv_data)

        if not self.header:
            # If header is not provided, rows should be dicts.
            self.header = []
            for row in self.rows:
                self.header += [f for f in row.keys() if f not in self.header]
        else:
            # If header is provided, rows may be lists.
            # Convert all row lists to dicts.
            for i, row in enumerate(self.rows):
                if isinstance(row, list):
                    self.rows[i] = dict(zip(self.header, row))

    def html(self, include_table_rows: bool = True):
        with (container := d.div(style="border:1px solid black;")):
            self.caption.html()
            self.kv_data.html()
            if include_table_rows:
                logger.info(f"Creating HTML for {len(self.rows)} rows.")
                with d.div():
                    with d.table():
                        with d.tr():
                            for column in self.header:
                                d.th(column)
                        for row in self.rows:
                            with d.tr():
                                for column in self.header:
                                    d.td(row.get(column, ""))
        return container

    def md(self) -> str:
        table_rows = [self.header, [":----:" for _ in range(len(self.header))]] + [
            [row[col] for col in self.header] for row in self.rows
        ]
        table = "\n".join(["|".join([str(v) for v in row]) for row in table_rows])
        return "\n\n".join([self.caption.md(), self.kv_data.md(), table])
