from typing import List, TextIO
from collections import Counter

import numpy as np
import termplotlib as tpl
from rich import box, print
from rich.live import Live
from rich.table import Table, Column
from rich.console import Console


class Chart:
    def __init__(
        self,
        file: TextIO,
        force_ascii: bool = False,
        max_width: int = 40,
        top_n: int = 15,
        fullscreen: bool = False,
        **kwargs,
    ):
        self.file = file
        self.max_width = max_width
        self.top_n = top_n
        self.force_ascii = force_ascii
        self.fullscreen = fullscreen

    def render(self):
        raise NotImplementedError

    def update(self, lines: List[str]):
        raise NotImplementedError

    def run(self):
        console = Console(highlight=False)
        if self.file.name == "<stdin>":
            with Live(console=console, screen=self.fullscreen) as live:
                for line in self.file:
                    self.update([line])
                    live.update(self.render())
        else:
            lines = self.file.readlines()
            self.update(lines)
            console.print(self.render())

    @property
    def total(self):
        raise NotImplementedError

    def on_exit(self):
        pass


class Bar(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = Counter()
        self.char = "*" if self.force_ascii else "█"
        self.max = -1

    def update(self, lines):
        self.counter.update(line.strip() for line in lines)
        _, self.max = self.counter.most_common(1)[0]

    def render(self) -> Table:
        table = Table.grid(
            Column(
                "line",
                justify="right",
                max_width=self.max_width,
                no_wrap=True,
            ),
            Column("count"),
            Column("percent"),
            Column("bins"),
            padding=(0, 1),
        )

        for line, count in self.counter.most_common(self.top_n):
            table.add_row(
                f"{line}",
                f"[{count}]",
                f"{(count / self.max) * 100:.2f}%",
                f"{self.char * round(count / self.max * self.max_width)}",
            )

        return table

    @property
    def total(self):
        return sum(self.counter.values())


class Histogram(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.samples = []
        self.hide_stats = kwargs.get("hide_stats", False)

    def update(self, lines):
        self.samples.extend(float(line) for line in lines)

    def render(self):
        fig = tpl.figure(width=28 + self.max_width)
        counts, bins = np.histogram(self.samples, bins=self.top_n)
        fig.hist(counts, bins, orientation="horizontal", force_ascii=self.force_ascii)
        return fig

    def stats(self) -> Table:
        table = Table("avg", "median", "max", "min", box=box.ASCII)
        arr = np.array(self.samples)
        table.add_row(
            f"{np.mean(arr):.2f}",
            f"{np.median(arr)}",
            f"{np.min(arr)}",
            f"{np.max(arr)}",
        )
        return table

    @property
    def total(self):
        return len(self.samples)

    def on_exit(self):
        if self.total > 0 and not self.hide_stats:
            print(self.stats())
