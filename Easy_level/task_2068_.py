""""""
from collections import defaultdict, Counter
from typing import List

"""
2068. Check Whether Two Strings are Almost Equivalent

Two strings word1 and word2 are considered almost equivalent if the differences between the 
frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.

Example 1:

Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.
Example 2:

Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.
Example 3:

Input: word1 = "cccddabba", word2 = "babababab"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
- 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
- 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
- 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.
 
Constraints:

n == word1.length == word2.length
1 <= n <= 100
word1 and word2 consist only of lowercase English letters.
"""
"""
Две строки word1 и word2 считаются "почти эквивалентными", если разница между частотами каждой 
буквы от 'a' до 'z' в этих двух строках — не превышает 3.
Дано две строки word1 и word2 одинаковой длины n. Верни true если строки почти эквивалентны, иначе false.
Проще говоря: посчитай сколько раз каждая буква встречается в первой строке и во второй. 
Если для каждой буквы разница между этими числами ≤ 3 — возвращаем true, иначе false.
"""
from string import ascii_lowercase


class Solution:
	def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
		counter_1 = Counter(word1)
		counter_2 = Counter(word2)

		for c in ascii_lowercase:
			if abs(counter_1.get(c, 0) - counter_2.get(c, 0)) > 3:
				return False

		return True


# class Solution:
# 	def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
# 		a = False
# 		count1 = Counter(word1)
# 		count2 = Counter(word2)
# 		for key in set(word1 + word2):
# 			if abs(count1[key] - count2[key]) <= 3:
# 				a = True
# 			else:
# 				a = False
# 				break
#
# 		return a

if __name__ == '__main__':
	word1 = "cccddabba"
	word2 = "babababab"
	s = Solution()
	print(s.checkAlmostEquivalent(word1, word2))
