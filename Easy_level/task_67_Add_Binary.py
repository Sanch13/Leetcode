"""
67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
	def addBinary(self, a: str, b: str) -> str:
		carry: int = 0
		result: list = []
		pointer_a = len(a) - 1
		pointer_b = len(b) - 1

		while pointer_a >= 0 or pointer_b >= 0 or carry:
			value_a = 0 if pointer_a < 0 else int(a[pointer_a])
			value_b = 0 if pointer_b < 0 else int(b[pointer_b])

			total = value_a + value_b + carry
			current_bit = total % 2
			carry = total // 2

			result.append(str(current_bit))
			pointer_a -= 1
			pointer_b -= 1

		return ''.join(reversed(result))


if __name__ == '__main__':
	a = '1010'
	b = "1011"
	s = Solution()
	print(s.addBinary(a, b))

