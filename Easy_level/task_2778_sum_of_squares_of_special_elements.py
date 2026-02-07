""""""
from typing import List

"""
2778. Sum of Squares of Special Elements 
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: 21
Explanation: There are exactly 3 special elements in nums: nums[1] since 1 divides 4, nums[2] since 2 divides 4, and nums[4] since 4 divides 4. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1 * 1 + 2 * 2 + 4 * 4 = 21.  
Example 2:

Input: nums = [2,7,1,19,18,3]
Output: 63
Explanation: There are exactly 4 special elements in nums: nums[1] since 1 divides 6, nums[2] since 2 divides 6, nums[3] since 3 divides 6, and nums[6] since 6 divides 6. 
Hence, the sum of the squares of all special elements of nums is nums[1] * nums[1] + nums[2] * nums[2] + nums[3] * nums[3] + nums[6] * nums[6] = 2 * 2 + 7 * 7 + 1 * 1 + 3 * 3 = 63. 

Constraints:

1 <= nums.length == n <= 50
1 <= nums[i] <= 50
"""
"""
2778. Сумма квадратов специальных элементов
Дан массив целых чисел nums длиной n с индексацией с 1 (1-indexed).
Элемент nums[i] массива nums называется специальным, если i делит n без остатка, 
то есть n % i == 0.
Верните сумму квадратов всех специальных элементов массива nums.

Пример 1:

Вход: nums = [1,2,3,4]
Выход: 21
Объяснение: В nums ровно 3 специальных элемента: 
- nums[1], так как 1 делит 4
- nums[2], так как 2 делит 4
- nums[4], так как 4 делит 4
Следовательно, сумма квадратов всех специальных элементов:
nums[1] * nums[1] + nums[2] * nums[2] + nums[4] * nums[4] = 1*1 + 2*2 + 4*4 = 21

Пример 2:

Вход: nums = [2,7,1,19,18,3]
Выход: 63
Объяснение: В nums ровно 4 специальных элемента:
- nums[1], так как 1 делит 6
- nums[2], так как 2 делит 6
- nums[3], так как 3 делит 6
- nums[6], так как 6 делит 6
Следовательно, сумма квадратов всех специальных элементов:
nums[1]*nums[1] + nums[2]*nums[2] + nums[3]*nums[3] + nums[6]*nums[6] = 
2*2 + 7*7 + 1*1 + 3*3 = 63

Ограничения:

1 <= nums.length == n <= 50
1 <= nums[i] <= 50
"""


class Solution:
	def sumOfSquares(self, nums: List[int]) -> int:
		total: int = 0
		n = len(nums)

		for i, el in enumerate(nums, start=1):
			if n % i ==  0:
				total += el ** 2

		return total


if __name__ == '__main__':
	nums = [2, 7, 1, 19, 18, 3]
	s = Solution()
	print(s.sumOfSquares(nums))
