""""""
from collections import defaultdict, Counter
from typing import List

"""
1995. Count Special Quadruplets
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d
 
Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
 
Constraints:

4 <= nums.length <= 50
1 <= nums[i] <= 100
"""
"""
Дан массив целых чисел nums с индексацией с нуля. Верни количество уникальных четвёрок (a, b, c, d) таких что:

nums[a] + nums[b] + nums[c] == nums[d]
a < b < c < d (индексы строго по возрастанию)

Проще говоря: найди все комбинации из 4 элементов массива (по порядку индексов), где сумма первых трёх равна четвёртому.
"""


class Solution:
	def countQuadruplets(self, nums: List[int]) -> int:
		length = len(nums)
		count = 0

		for a in range(length):
			for b in range(a + 1, length):
				for c in range(b + 1, length):
					for d in range(c + 1, length):
						if nums[a] + nums[b] + nums[c] == nums[d]:
							count += 1

		return count


if __name__ == '__main__':
	nums = [1, 1, 1, 3, 5]
	s = Solution()
	print(s.countQuadruplets(nums))
