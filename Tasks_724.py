import sys

"""Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no 
elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i
            left_sum += x
        return -1


obj = Solution()
# print(obj.pivotIndex([2, 1, 3, 2, 1]))  # 2
# print(obj.pivotIndex([1, 7, 3, 6, 5, 6]))   # 3
# print(obj.pivotIndex([1, 2, 3]))   # -1
# print(obj.pivotIndex([2, 1, -1]))   # 0
# print(obj.pivotIndex([-1, -1, -1, -1, -1, 0]))   # 2












