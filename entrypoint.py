import click
import sys

from merge import Interval, merge, InvalidInterval


@click.command()
@click.argument("intervals", nargs=-1)
def main(intervals: list[str]):
    input = []
    for interval in intervals:
        try:
            start, end = interval.strip("][").split(",")
            input.append(Interval(int(start), int(end)))
        except (InvalidInterval):
            print(f"Invalid interval {interval}")
            sys.exit(1)
        except (Exception):
            print(
                f"Could not parse Interval {interval}. Required format is [int,int] i.e. [1,42]")
            sys.exit(1)

    print(merge(input))


if __name__ == "__main__":
    main()
