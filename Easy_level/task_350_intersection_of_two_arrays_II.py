""""""
from collections import defaultdict
from typing import List

"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
"""
350. Пересечение двух массивов II
Условие:
Даны два массива целых чисел nums1 и nums2. Верни массив их пересечения. Каждый элемент результата 
должен появляться столько раз, сколько он встречается в обоих массивах. Порядок элементов в ответе не важен.
Примеры:

[1,2,2,1] и [2,2] → [2,2] (двойка есть дважды в обоих)
[4,9,5] и [9,4,9,8,4] → [4,9] (каждый элемент берём минимальное количество раз из обоих массивов)
"""


class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		result: list[int] = []
		nums1_d: dict[int, int] = defaultdict(int)

		for v in nums1:
			nums1_d[v] += 1

		for v in nums2:
			if nums1_d[v] > 0:
				result.append(v)
				nums1_d[v] -= 1

		return result


if __name__ == '__main__':
	nums1 = [4, 9, 5]
	nums2 = [9, 4, 9, 8, 4]
	s = Solution()
	print(s.intersect(nums1, nums2))
