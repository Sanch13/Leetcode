from timeit import timeit
from typing import List

"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(min(strs, key=len))
        prefix = ''
        for i in range(min_length):
            letter = strs[0][i]
            for word in strs[1:]:
                if letter != word[i]:
                    return prefix if prefix else ""
            prefix += letter
        return prefix

    def sort_lex(self, v: List[str]):
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


o = Solution()
print(o.longestCommonPrefix(["flower", "flow", "flight"]))
print(o.longestCommonPrefix(["dog", "racecar", "car"]))
print(o.sort_lex(["flower", "flow", "flight", "fly", "flash"]))

