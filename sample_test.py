from sample import median
from sample import MedianError

import pytest

def test_invalid_empty_list():
    with pytest.raises(MedianError):
        median([])

def test_invalid_not_a_list():
    with pytest.raises(TypeError):
        median(123)

def test_invalid_non_num_element():
    with pytest.raises(TypeError):
        median([10, 20, 30, "fourty"])

def test_valid_input_odd_count():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([4.5, 2, 5, 1.1, 3]) == 3

def test_valid_input_even_count():
    assert median([1, 2, 3, 4, 5, 6]) == 3.5
    assert median([4, 2, 5, 6, 1, 3]) == 3.5