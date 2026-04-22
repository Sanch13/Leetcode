"""
1232. Check If It Is a Straight Line
You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the
coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
from typing import List

"""
Задача: Проверить, лежат ли точки на одной прямой
Тебе дан массив координат точек на плоскости XY. Нужно проверить, лежат ли все точки на одной прямой.
Пример 1: точки [1,2], [2,3], [3,4]... — все на одной прямой → true
Пример 2: точки [1,1], [2,2], [3,4]... — точка [3,4] выбивается → false
"""
"""
Декомпозиция задачи
Подзадача 1 — Математическая основа
Прежде чем писать код, нужно понять: как математически определить, лежат ли три точки на одной прямой?
Аналогия из жизни: представь, что ты идёшь по дороге. Если на каждом шаге ты поворачиваешь на одинаковый угол — ты идёшь прямо. Если угол изменился — ты свернул.
В математике это называется наклон прямой (slope):
slope = (y2 - y1) / (x2 - x1)
Если все точки на одной прямой — наклон между любыми двумя соседними точками одинаковый.

Итоговый алгоритм словами:

Взять точки [0] и [1] как базу — вычислить "эталонный" наклон через перекрёстное умножение
Пройтись по всем точкам начиная с [2]
Для каждой точки проверить — совпадает ли наклон с эталонным
Если хоть одна не совпала → False
Если все совпали → True
(y2 - y1) * (x1 - x0) == (y1 - y0) * (x2 - x1)
"""


class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		x_0, y_0 = coordinates[0]
		x_1, y_1 = coordinates[1]

		for x, y in coordinates[2:]:
			if not ((y - y_1) * (x_1 - x_0) == (y_1 - y_0) * (x - x_1)):
				return False

		return True


if __name__ == '__main__':
	coords = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
	sol = Solution()
	print(sol.checkStraightLine(coords))
