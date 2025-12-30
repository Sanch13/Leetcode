"""
27. Remove Element
Hint
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which
are not equal to val. Consider the number of elements in nums which are not equal to val be k,
 to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are
not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

"""
Анализ задачи
Что нужно понять:
In-place — это значит, что мы НЕ создаём новый массив, а модифицируем существующий
Нам не важен порядок элементов — это ключевая подсказка!
Нам не важно, что остаётся после первых k элементов
Мы возвращаем количество элементов, не равных val

Аналогия из жизни 🏠
Представь, что у тебя есть полка с книгами:
Тебе нужно убрать все книги определённого автора (это val)
Все остальные книги нужно сдвинуть влево, чтобы они стояли плотно в начале полки
Не важно, в каком порядке будут остальные книги
Не важно, что останется справа на освободившемся месте


Подходящий шаблон
Эта задача решается шаблоном Two Pointers (Два указателя)!
Идея:
Один указатель (i) идёт по всему массиву и проверяет элементы
Второй указатель (k) указывает на позицию, куда мы будем помещать "хороший" элемент (не равный val)

Эта задача решается шаблоном Two Pointers (Два указателя)
Ключевые принципы Two Pointers:

Один указатель читает (i или item)
Другой указатель пишет (k)
Указатель для записи двигается только при условии
"""
from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		k: int = 0
		for i, item in enumerate(nums):
			if item != val:
				nums[k] = item
				k += 1
		return k


if __name__ == "__main__":
	print(Solution().removeElement([3, 2, 2, 3], 3))
	print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
	print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 7))
