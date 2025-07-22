def two_sum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return []

# quick test
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))