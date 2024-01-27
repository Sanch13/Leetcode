"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = list()
        for el in s:
            if el in "({[":
                stack.append(el)
            elif not stack or stack.pop() != brackets[el]:
                return False

        return not stack


s = '()[]{}'
res = Solution()
print(res.is_valid(s))

assert res.is_valid("([)]") == False
assert res.is_valid("(]") == False
assert res.is_valid("()[]{}") == True
