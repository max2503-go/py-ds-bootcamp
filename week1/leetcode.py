#Two Sums
def two_sum(nums, target):
    seen = {}                      # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i              # store after the check
    return []                      # should never hit
#Fizz Buzz
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:          # 3 and 5 both divide
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Valid Anagram
def is_anagram(s, t):
     if len(s) != len(t):
        return False
     from collections import Counter
     return Counter(s) == Counter(t)

# quick test
if __name__ == "__main__":
    print("Two Sum:", two_sum([2,7,11,15], 9))        # ➜ [0,1]
    print("FizzBuzz (n=15):", fizz_buzz(15))            # ➜ ["1","2","Fizz","4","Buzz", 6, 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz Buzz"]
    print("Anagram:", is_anagram("anagram", "nagaram"))  # ➜ True
    print("Anagram:", is_anagram("rat", "car"))          # ➜ False

 # ------------------------------------------------------------------
#  WEEK 1 – DAY 2  MINI-SPRINT  – DETAILED EXPLANATIONS
#  Paste this block at the VERY BOTTOM of week1/leetcode.py
# ------------------------------------------------------------------
#
# ======================== 1. TWO SUM ========================
# Problem
#     Given a list `nums` and an int `target`, return the
#     indices of the two numbers that add up to `target`.
#
# Algorithm (step-by-step)
# 1.  Create an empty dict `seen`.
# 2.  Loop with `enumerate(nums)` → gives (index, value).
# 3.  For each number `num`:
#         complement = target - num
#         - If complement already exists in `seen`
#              → we have found the pair.
#              → return [seen[complement], current_index]
#         - Else store `seen[num] = current_index`.
# 4.  Complexity: O(n) time, O(n) extra space.
#
# Example walk-through
#     nums = [2, 7, 11, 15], target = 9
#     Step 1: i=0, num=2  → complement=7  → 7 not in seen
#             seen = {2:0}
#     Step 2: i=1, num=7  → complement=2  → 2 **is** in seen
#             return [seen[2], 1] → [0, 1]
#
# ======================== 2. FIZZBUZZ ========================
# Problem
#     Given integer n, return list 1..n where
#         multiple of 3   → "Fizz"
#         multiple of 5   → "Buzz"
#         multiple of 3&5 → "FizzBuzz"
#         else            → str(number)
#
# Algorithm
# 1.  Create empty list `result`.
# 2.  `for i in range(1, n+1)`:
#         remainder_15 = i % 15
#         remainder_3  = i % 3
#         remainder_5  = i % 5
#         - If remainder_15 == 0  → "FizzBuzz"
#         - Else if remainder_3 == 0 → "Fizz"
#         - Else if remainder_5 == 0 → "Buzz"
#         - Else append str(i)
# 3.  Complexity: O(n) time, O(1) extra space besides output list.
#
# Key concepts
#     % (modulo) → remainder after division
#     str(i)     → convert integer to string so list stays homogeneous
#
# ======================== 3. VALID ANAGRAM ========================
# Problem
#     Return True if strings `s` and `t` are anagrams.
#
# Definition
#     Same letters with identical frequencies; only order may differ.
#
# Algorithm
# 1.  Fast fail: if len(s) != len(t) → False immediately.
# 2.  Use collections.Counter to build frequency maps:
#         Counter(s) → {'a':2, 'n':1, ...}
#         Counter(t) → same structure
# 3.  Compare the two Counter objects with `==`.
# 4.  Complexity: O(n) time, O(1) extra space (alphabet size is constant).
#
# Edge cases handled
#     - Different lengths → False
#     - Empty strings → True (both empty)
# ------------------------------------------------------------------