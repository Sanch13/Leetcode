from timeit import timeit

"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def is_palindrome(self, x: int) -> bool:
        x = str(x)
        dist = len(x) // 2
        start, end = 0, -1
        for _ in range(dist):
            if x[start] != x[end]:
                return False
            start += 1
            end -= 1
        return True

    def is_palindrome_1(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

    def is_palindrome_2(self, x: int) -> bool:
        if x < 0:
            return False

        input_num = x
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        return new_num == input_num


obj = Solution()

print(timeit("obj.is_palindrome(12122121)", globals=globals(), number=10000))  # 0.022779089000323438
print(timeit("obj.is_palindrome_1(12122121)", globals=globals(), number=10000))  # 0.010494815000129165
print(timeit("obj.is_palindrome_2(12122121)", globals=globals(), number=10000))  # 0.0259501979999186
