"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""
from tracemalloc import start
"""
Задача: Подъём по лестнице
Ты поднимаешься по лестнице. Нужно сделать n шагов чтобы добраться до верха.
За один раз ты можешь подняться на 1 или 2 ступеньки. Сколько различных способов добраться до верха?
Пример 1: n = 2 → ответ 2
Пример 2: n = 3 → ответ 3
"""


class Solution:
	def climbStairs(self, n: int) -> int:
		if n == 1:
			return 1

		if n == 2:
			return 2

		pre_last = 1
		last = 2

		i = 3
		while i <= n:
			f = pre_last + last
			pre_last = last
			last = f
			i += 1

		return last


if __name__ == '__main__':
	n = 5
	sol = Solution()
	print(sol.climbStairs(n))
