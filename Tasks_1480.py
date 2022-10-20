"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]."""

from timeit import timeit
from itertools import accumulate


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:  # my version
        nums_out = [sum(nums[:i + 1]) for i in range(len(nums))]
        return nums_out

    def runningSum2(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    def runningSum3(self, nums: list[int]) -> list[int]:  # the best version
        return list(accumulate(nums))


obj = Solution()
print(timeit('obj.runningSum([3, 1, 2, 10, 1])', globals=globals(), number=10000))  # 0.0107657
print(timeit('obj.runningSum2([3, 1, 2, 10, 1])', globals=globals(), number=10000))  # 0.0046014
print(timeit('obj.runningSum3([3, 1, 2, 10, 1])', globals=globals(), number=10000))  # 0.0026851
