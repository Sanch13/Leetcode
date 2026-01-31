"""
942. DI String Match
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""

"""
Перестановка perm из n + 1 целых чисел, содержащая все числа в диапазоне [0, n], может быть представлена строкой s длиной n, где:

s[i] == 'I' если perm[i] < perm[i + 1], и
s[i] == 'D' если perm[i] > perm[i + 1].

Дана строка s, восстанови перестановку perm и верни её. Если существует несколько валидных перестановок perm, верни любую из них.

Пример 1:
Вход: s = "IDID"
Выход: [0,4,1,3,2]

Пример 2:
Вход: s = "III"
Выход: [0,1,2,3]

Пример 3:
Вход: s = "DDI"
Выход: [3,2,0,1]
 
Ограничения:
1 <= s.length <= 105
s[i] либо 'I', либо 'D'.
"""

"""
s = "IDID"
позиции:  0   1   2   3   4
числа:   [0,  4,  1,  3,  2]
         
0 → 4: s[0] = 'I' ✓ (0 < 4, увеличение)
4 → 1: s[1] = 'D' ✓ (4 > 1, уменьшение)
1 → 3: s[2] = 'I' ✓ (1 < 3, увеличение)
3 → 2: s[3] = 'D' ✓ (3 > 2, уменьшение)
"""
"""
Теперь у тебя есть полная логика:
Основной цикл:
Итерируемся по строке s
Если 'I' → добавляем low, делаем low += 1
Если 'D' → добавляем high, делаем high -= 1
После цикла:
Добавляем последнее число (оно будет равно и low, и high)
"""
from typing import List


class Solution:
	def diStringMatch(self, s: str) -> List[int]:
		n: int = len(s)
		result: list[int] = []
		low: int = 0
		high: int = n
		for c in s:
			if "I" == c:
				result.append(low)
				low += 1
			else:
				result.append(high)
				high -= 1

		result.append(low)

		return result


if __name__ == '__main__':
	s = "IDIDIDIIID"
	sol = Solution()
	print(sol.diStringMatch(s))
