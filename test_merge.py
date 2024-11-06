from merge import make_interval_list, merge, Interval, InvalidInterval
import pytest


def test_example_from_task():
    input = make_interval_list([[25, 30], [2, 19], [14, 23], [4, 8]])
    output = make_interval_list([[2, 23], [25, 30]])
    assert merge(input) == output


def test_empty_inputs():
    assert merge([]) == []


def test_single_interval():
    input = [Interval(1, 3)]
    assert merge(input) == input


def test_merge_no_overlap():
    input = [Interval(1, 3), Interval(5, 7)]
    assert merge(input) == input


def test_merge_with_overlap():
    input = make_interval_list([[1, 5], [4, 7]])
    assert merge(input) == [Interval(1, 7)]


# assumption: output order does not need to match input order
def test_merge_no_overlap_inverted_input():
    input = [Interval(5, 7), Interval(1, 3)]
    assert set(merge(input)) == set(input)


def test_interval_has_overlap():
    first = Interval(1, 5)
    with_overlap = Interval(4, 7)
    no_overlap = Interval(10, 15)
    contained = Interval(2, 3)
    assert first.has_overlap(with_overlap)
    assert first.has_overlap(contained)
    assert not first.has_overlap(no_overlap)


def test_interval_merge():
    first = Interval(1, 5)
    second = Interval(4, 7)
    assert Interval(1, 7) == first.merge(second)
    assert Interval(1, 7) == second.merge(first)


def test_merge_fully_contained_interval():
    outer = Interval(1, 8)
    inner = Interval(3, 5)
    assert merge([outer, inner]) == [outer]


# assumption: inverse intervals are not allowed
def test_invalid_interval():
    with pytest.raises(InvalidInterval):
        Interval(3, 1)


def test_make_interval_list():
    intervals = make_interval_list([[1, 3], [5, 7], [4, 8]])
    assert intervals == [Interval(1, 3), Interval(5, 7), Interval(4, 8)]
