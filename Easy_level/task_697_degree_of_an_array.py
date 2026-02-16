""""""
from typing import List

"""
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
"""
Задача: Степень массива
Дано: непустой массив неотрицательных целых чисел nums
Степень массива — это максимальная частота появления любого элемента в массиве.
Задача: найти наименьшую возможную длину непрерывного подмассива, который имеет ту же степень, что и исходный массив.

Пример 1:
Вход: nums = [1,2,2,3,1]
Выход: 2
Объяснение:

Степень массива = 2 (элементы 1 и 2 встречаются по 2 раза)
Подмассивы с той же степенью: [1,2,2,3,1], [1,2,2,3], [2,2,3,1], [1,2,2], [2,2,3], [2,2]
Самый короткий: [2,2] — длина 2

Пример 2:
Вход: nums = [1,2,2,3,1,4,2]
Выход: 6
Объяснение:

Степень = 3 (элемент 2 встречается 3 раза)
Самый короткий подмассив: [2,2,3,1,4,2] — длина 6

Паттерн: Hash Map (словари) + одно линейное сканирование
"""
'''
Подзадача 1: Сбор статистики
Пройдись по массиву один раз и собери:

Частоту каждого элемента
Индекс первого вхождения каждого элемента
Индекс последнего вхождения каждого элемента
'''


class Solution:
	def findShortestSubArray(self, nums: List[int]) -> int:

		data = {}

		for i, el in enumerate(nums):
			if el not in data:
				data[el] = {
					"first": i,
					"last": i,
					"count": 1,
				}
			else:
				data[el]["last"] = i
				data[el]["count"] += 1

		degree = 0
		min_diff = len(nums)
		for k, v in data.items():
			cnt = v.get("count")

			if cnt > degree:
				degree = cnt
				min_diff = v["last"] - v["first"] + 1
			elif cnt == degree:
				diff = v["last"] - v["first"] + 1
				min_diff = min(min_diff, diff)

		return min_diff


if __name__ == '__main__':
	nums = [1, 2, 2, 3, 1, 4, 2]
	s = Solution()
	print(s.findShortestSubArray(nums))
