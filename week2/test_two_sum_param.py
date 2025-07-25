import pytest #Today we use @pytest.mark.parametrize, which is defined inside the pytest library,
#so we must import pytest to tell Python where that decorator lives.
from day5_twosum import two_sum

@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4],     6, [1, 2]),
        ([0, 4, 3, 0],  0, [0, 3]),
        ([],             5, []), #[] in "target" possion means no pair possible, which is true (will pass the test)
        ([5],            5, []),
        ([-1, -2, -3], -3, [0, 1])
    ]
)
def test_two_sum_param(nums, target, expected):
    assert two_sum(nums, target) == expected
