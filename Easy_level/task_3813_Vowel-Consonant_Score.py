"""
3813. Vowel-Consonant Score
You are given a string s consisting of lowercase English letters, spaces, and digits.
Let v be the number of vowels in s and c be the number of consonants in s.
A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u', while any other letter in the English alphabet is considered a consonant.
The score of the string s is defined as follows:
If c > 0, the score = floor(v / c) where floor denotes rounding down to the nearest integer.
Otherwise, the score = 0.
Return an integer denoting the score of the string.

Example 1:
Input: s = "cooear"

Output: 2
Explanation:
The string s = "cooear" contains v = 4 vowels ('o', 'o', 'e', 'a') and c = 2 consonants ('c', 'r').
The score is floor(v / c) = floor(4 / 2) = 2.

Example 2:
Input: s = "axeyizou"

Output: 1
Explanation:
The string s = "axeyizou" contains v = 5 vowels ('a', 'e', 'i', 'o', 'u') and c = 3 consonants ('x', 'y', 'z').
The score is floor(v / c) = floor(5 / 3) = 1.

Example 3:
Input: s = "au 123"

Output: 0
Explanation:
The string s = "au 123" contains no consonants (c = 0), so the score is 0.

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters, spaces and digits.
"""
"""
3813. Подсчет гласных и согласных

Дана строка s, состоящая из строчных английских букв, пробелов и цифр.

Пусть v — количество гласных в s, а c — количество согласных в s.

Гласными являются буквы 'a', 'e', 'i', 'o', 'u', 
а любая другая буква английского алфавита считается согласной.

Счет строки s определяется следующим образом:
- Если c > 0, то счет = floor(v / c), где floor означает округление вниз до ближайшего целого числа.
- Иначе счет = 0.

Верните целое число, обозначающее счет строки.

Пример 1:
Вход: s = "cooear"
Выход: 2
Объяснение:
Строка s = "cooear" содержит v = 4 гласных ('o', 'o', 'e', 'a') и c = 2 согласных ('c', 'r').
Счет = floor(v / c) = floor(4 / 2) = 2.

Пример 2:
Вход: s = "axeyizou"
Выход: 1
Объяснение:
Строка s = "axeyizou" содержит v = 5 гласных ('a', 'e', 'i', 'o', 'u') и c = 3 согласных ('x', 'y', 'z').
Счет = floor(v / c) = floor(5 / 3) = 1.

Пример 3:
Вход: s = "au 123"
Выход: 0
Объяснение:
Строка s = "au 123" не содержит согласных (c = 0), поэтому счет = 0.

Ограничения:
1 <= s.length <= 100
s состоит из строчных английских букв, пробелов и цифр.
"""
"""
Ключевые моменты:
Гласные: только 'a', 'e', 'i', 'o', 'u'
Согласные: все остальные буквы английского алфавита (не цифры, не пробелы!)
Пробелы и цифры игнорируем — они не считаются ни гласными, ни согласными
Деление с округлением вниз (floor division)
Особый случай: если согласных нет (c = 0), возвращаем 0
"""


class Solution:
	def vowelConsonantScore(self, s: str) -> int:
		vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
		v, c = 0, 0

		for char in s:
			if char.isalpha():
				if char in vowels:
					v += 1
				else:
					c += 1

		return v // c if c > 0 else 0


if __name__ == '__main__':
	s = "axeyizou"
	sol = Solution()
	print(sol.vowelConsonantScore(s))
