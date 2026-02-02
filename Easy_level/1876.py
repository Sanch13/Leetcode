""""""
"""
876. Substrings of Size Three with Distinct Characters
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 
Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.
"""
"""
Задача: Подстроки длины три с различными символами
Строка называется «хорошей», если в ней нет повторяющихся символов.
Дана строка s. Требуется вернуть количество хороших подстрок длины ровно три в строке s.
Важно:
Если одна и та же подстрока встречается несколько раз — каждое вхождение учитывается отдельно.
Подстрока — это непрерывная последовательность символов в строке.

Пример 1:
Вход: s = "xyzzaz"
Выход: 1
Объяснение: Всего 4 подстроки длины 3: "xyz", "yzz", "zza", "zaz".
Хорошая только "xyz" (все символы уникальны).

Пример 2:
Вход: s = "aababcabc"
Выход: 4
Объяснение: Подстроки длины 3: "aab", "aba", "bab", "abc", "bca", "cab", "abc".
Хорошие: "abc", "bca", "cab", "abc" (последняя "abc" — второе вхождение, тоже считается).

Ограничения:
1 <= s.length <= 100
Строка состоит только из строчных латинских букв.
"""

"""
Скользим окном длины 3 от индекса 0 до n - 3
На каждом шаге проверяем уникальность через set
Считаем, сколько окон прошли проверку
"""

class Solution:
	def countGoodSubstrings(self, s: str) -> int:
		length: int = len(s) - 2

		cnt = 0
		for i in range(length):
			if len(set(s[i: i + 3])) == 3:
				cnt += 1

		return cnt



if __name__ == '__main__':
	s = "xyzzaz"
	sol = Solution()
	print(sol.countGoodSubstrings(s))
