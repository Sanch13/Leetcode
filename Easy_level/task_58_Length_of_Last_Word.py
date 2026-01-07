"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""


class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		length = len(s)
		idx = length - 1

		res = 0
		while idx >= 0:
			if s[idx] == " ":
				if res != 0:
					return res
			else:
				res += 1
			idx -= 1
		return res


if __name__ == '__main__':
	string = "    a "
	s = Solution()
	print(s.lengthOfLastWord(string))

