from __future__ import annotations
from dataclasses import dataclass


class NotMergable(Exception):
    pass


class InvalidInterval(Exception):
    pass


def merge(input: list[Interval]) -> list[Interval]:
    if len(input) <= 1:
        return input
    result = []
    iterator = iter(sorted(input))
    current = next(iterator)
    for interval in iterator:
        if current.has_overlap(interval):
            current = current.merge(interval)
        else:
            result.append(current)
            current = interval
    result.append(current)
    return result


@dataclass(frozen=True, order=True)
class Interval:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise InvalidInterval

    def __repr__(self) -> str:
        return f"[{self.start},{self.end}]"

    def has_overlap(self, other: Interval) -> bool:
        return not self._has_no_overlap(other)

    def _has_no_overlap(self, other: Interval) -> bool:
        return other.end < self.start or self.end < other.start

    def merge(self, other: Interval) -> Interval:
        if not self.has_overlap(other):
            raise NotMergable
        start = min(self.start, other.start)
        end = max(self.end, other.end)
        return Interval(start, end)


def make_interval_list(input: list[list[int]]) -> list[Interval]:
    output = []
    for start, end in input:
        output.append(Interval(start, end))
    return output
