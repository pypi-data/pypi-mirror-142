#!/usr/bin/env python
import sys
import argparse
import typing
from statistics import mean, median
from collections import Counter

from rich import print
from rich.live import Live
from rich.text import Text
from rich.table import Table, Column


class Histogram:
    def __init__(
        self,
        file: typing.TextIO,
        char: str = "*",
        max_width: int = 40,
        top_n: int = 15,
    ):
        self.samples = Counter()
        self.file = file
        self.char = char
        self.max_width = max_width
        self.top_n = top_n
        self.max = -1

    def update(self, *args):
        self.samples.update(args)
        _, self.max = self.samples.most_common(1)[0]

    def render(self) -> Text:
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

        for line, count in self.samples.most_common(self.top_n):
            table.add_row(
                f"{line}",
                f"[{count}]",
                f"{(count / self.max) * 100:.2f}%",
                f"{self.char * round(count / self.max * self.max_width)}",
            )

        return table

    def stats(self) -> Table:
        values = [float(i) for i in self.samples.keys()]
        table = Table("avg", "median", "max", "min")
        table.add_row(
            f"{mean(values):.2f}",
            f"{median(values)}",
            f"{max(values)}",
            f"{min(values)}",
        )
        return table

    def run(self):
        with Live() as live:
            for newline in self.file:
                self.update(newline.strip())
                live.update(self.render())


def run():
    parser = argparse.ArgumentParser(
        "fq",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="file or stdin for live chart",
    )
    parser.add_argument(
        "-n",
        "--top",
        help="top N samples",
        type=int,
        default=15,
    )
    parser.add_argument(
        "-c",
        "--character",
        default="*",
        help="character to represent bins",
    )
    parser.add_argument(
        "-w",
        "--max-width",
        default=40,
        type=int,
        help="max symbol width",
    )
    parser.add_argument(
        "-s",
        "--stats",
        action="store_true",
        default=False,
        help="print stats at exit (make sure your input is numerical)",
    )
    args = parser.parse_args()

    hist = Histogram(
        file=args.file,
        char=args.character,
        max_width=args.max_width,
        top_n=args.top,
    )

    try:
        hist.run()
    except KeyboardInterrupt:
        pass
    finally:
        print(f"\n{len(hist.samples)} samples.")
        if args.stats:
            print(hist.stats())


if __name__ == "__main__":
    run()
