from timeit import timeit

from typing import List

"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such 
that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice. You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    # THE FIRST WAY
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:    # THE SECOND WAY
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


obj = Solution()
# print(timeit("obj.twoSum([2, 7, 11, 15], target=9)", globals=globals(), number=10000))    # [0, 1]
# print(timeit("obj.twoSum([3, 2, 4], target=6)", globals=globals(), number=10000))          # [1, 2]
# print(timeit("obj.twoSum([3, 1, 4, 2], target=6)", globals=globals(), number=10000))       # [2, 3]
# print(timeit("obj.twoSum([3, 2, 3], target=6)", globals=globals(), number=10000))          # [0, 2]
# print(timeit("obj.twoSum([2, 5, 5, 11], target=10)", globals=globals(), number=10000))     # [1, 2]

# 0.004576
# 0.006950499999999998
# 0.0105023
# 0.005176399999999998
# 0.007557100000000004

# print(timeit("obj.twoSum2([2, 7, 11, 15], target=9)", globals=globals(), number=10000))    # [0, 1]
# print(timeit("obj.twoSum2([3, 2, 4], target=6)", globals=globals(), number=10000))          # [1, 2]
# print(timeit("obj.twoSum2([3, 1, 4, 2], target=6)", globals=globals(), number=10000))       # [2, 3]
# print(timeit("obj.twoSum2([3, 2, 3], target=6)", globals=globals(), number=10000))          # [0, 2]
# print(timeit("obj.twoSum2([2, 5, 5, 11], target=10)", globals=globals(), number=10000))     # [1, 2]

# 0.008351400000000002
# 0.009414399999999996
# 0.010751899999999995
# 0.009636100000000009
# 0.00966489999999999