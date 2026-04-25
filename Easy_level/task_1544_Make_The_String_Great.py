"""
1544. Make The String Great
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"

Constraints:
1 <= s.length <= 100
s contains only lower and upper case English letters.
"""
"""
Задача: "Сделай строку хорошей"
Дано: строка из маленьких и больших латинских букв.
"Хорошая строка" — это строка, в которой нет двух соседних символов, где одна буква — маленькая,
 а соседняя — та же буква, но большая (или наоборот). Например eE, Aa, bB — плохие пары.
Задача: удалять такие пары до тех пор, пока строка не станет хорошей. Вернуть результат.
"""
"""
Логика такая:

Идёшь по строке слева направо, берёшь каждый символ
Смотришь на верхушку стека — не плохая ли это пара с текущим символом?
Если плохая — что делать со стеком?
Если хорошая — что делать со стеком?

В конце стек и есть твой ответ.
Сложность:
Время: O(n) — из-за s
Память: O(n) — из-за s
LIFO гарантирует что верхушка стека — это всегда ближайший левый сосед текущего символа.
"""


class Solution:
	def makeGood(self, s: str) -> str:
		stack = []

		for char in s:
			if stack and self.is_bad_pair(stack[-1], char):
				stack.pop()
			else:
				stack.append(char)

		return ''.join(stack)

	def is_bad_pair(self, a, b) -> bool:
		return a.lower() == b.lower() and a != b

if __name__ == '__main__':
	s = "leEeetcode"
	sol = Solution()
	print(sol.makeGood(s))
