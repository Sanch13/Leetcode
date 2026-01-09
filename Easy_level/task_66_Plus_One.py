"""
66. Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is
the ith digit of the integer. The digits are ordered from most significant to least significant
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

Идем справа налево:
  если цифра == 9:
    - ставим 0
    - идем дальше (перенос продолжается)
  иначе (цифра < 9):
    - прибавляем 1
    - СТОП и возвращаем массив

Теперь у тебя есть понимание всех трёх случаев:
✅ Простой случай: последняя цифра < 9 → просто +1 и return
✅ Перенос в середине: встречаем 9 → ставим 0, идём дальше;
встречаем <9 → +1 и return
✅ Все девятки: прошли весь массив, все стали 0 → digits[0] = 1; digits.append(0)

Математическое моделирование с переносом (Carry Simulation)
"""
from typing import List


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		idx = len(digits) - 1

		while idx >= 0:
			if digits[idx] < 9:
				digits[idx] += 1
				return digits
			else:
				digits[idx] = 0

			idx -= 1

		digits[0] = 1
		digits.append(0)
		return digits


if __name__ == '__main__':
	d_ = [[1,2,3], [1,2,9], [1,9,9], [9,9,9]]
	s = Solution()
	for d in d_:
		print(s.plusOne(d))
