from numbers import Number
from typing import List


class MedianError(Exception):
    pass


def median(lst: List[Number]) -> Number:
    """Return the median (middle value) of numeric data.

    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values:

    >>> median([1, 3, 5])
    3
    >>> median([1, 3, 5, 7])
    4.0

    """
    # checking if input is not a List
    if not isinstance(lst, List):
        raise TypeError

    # checking if input is an empty List
    lst_len = len(lst)
    if lst_len == 0:
        raise MedianError("Empty list is not a valid input")

    # sort the List (TODO(arsivanov): what if the list is BIG)
    lst.sort()

    # if even number of elements
    if lst_len % 2 == 0:
        median_one = lst[lst_len//2]
        median_two = lst[lst_len//2 - 1]
        median = (median_one + median_two)/2
    # if odd number of elements
    else:
        median = lst[lst_len//2]

    return median


if __name__ == "__main__":
    print(median([1, 2, 3, 4]))
