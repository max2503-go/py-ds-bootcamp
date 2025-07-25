import pytest
from day5_twosum import two_sum

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4],     6, [1, 2]),
        ([0, 4, 3, 0],  0, [0, 3]),
        ([],             5, []),
        ([5],            5, []),
        ([-1, -2, -3], -3, [0, 1])
    ]
)
def test_two_sum_param(nums, target, expected):
    assert two_sum(nums, target) == expected
