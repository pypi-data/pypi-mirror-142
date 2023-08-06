#!/usr/bin/env python
import sys
import argparse

from .charts import Bar, Histogram


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
        help="file or stdin",
    )
    parser.add_argument(
        "-n",
        "--top",
        help="top N samples / bins",
        type=int,
        default=15,
    )
    parser.add_argument(
        "-t",
        "--type",
        default="bar",
        choices=["bar", "hist"],
        help="bar for categorical data, or hist for numerical",
    )
    parser.add_argument(
        "-a",
        "--force-ascii",
        default=False,
        action="store_true",
        help="force ascii *, by default renders unicode",
    )
    parser.add_argument(
        "-w",
        "--max-width",
        default=40,
        type=int,
        help="max symbol width",
    )
    parser.add_argument(
        "-f",
        "--fullscreen",
        action="store_true",
        default=False,
        help="show at full screen",
    )
    parser.add_argument(
        "--hide-stats",
        action="store_true",
        default=False,
        help="hide stats (avg, mean, min, max) on exit, only for histogram",
    )
    args = parser.parse_args()

    chart_factory = {
        "bar": Bar,
        "hist": Histogram,
    }[args.type]

    chart = chart_factory(
        file=args.file,
        force_ascii=args.force_ascii,
        max_width=args.max_width,
        top_n=args.top,
        hide_stats=args.hide_stats,
    )

    try:
        chart.run()
    except KeyboardInterrupt:
        pass
    finally:
        print(f"\n{chart.total} samples.")
        chart.on_exit()


if __name__ == "__main__":
    run()
