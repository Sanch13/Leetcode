"""
506. Relative Ranks
You are given an integer array score of size n, where score[i] is the score of the ith athlete
in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score,
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
"""
"""
Задача: Относительные ранги
Что нужно сделать:
Тебе дан массив очков спортсменов. Нужно вернуть массив рангов, где:

1-е место → "Gold Medal"
2-е место → "Silver Medal"
3-е место → "Bronze Medal"
Остальные → их номер места как строка ("4", "5", ...)

Важно: индекс спортсмена в массиве не меняется — ты должен вернуть ранг на той же позиции.
"""
"""
Сложность:
Время: O(n log n) — из-за сортировки
Память: O(n) — словарь + answer
"""
from typing import List


class Solution:
	def findRelativeRanks(self, score: List[int]) -> List[str]:
		answer = [""] * len(score)
		medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		score_index = {}  # {10: 0, 3: 1, 8: 2, 9: 3, 4: 4}

		for i, val in enumerate(score):
			score_index[val] = i

		sorted_score = sorted(score, reverse=True)  # [10, 9, 8, 4, 3]
		for i, val in enumerate(sorted_score):
			indx = score_index[val]
			value = medals[i] if i < 3 else str(i + 1)
			answer[indx] = value

		return answer


if __name__ == '__main__':
	score = [10, 3, 8, 9, 4]
	sol = Solution()
	print(sol.findRelativeRanks(score))
