"""
1337. The K Weakest Rows in a Matrix
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].


Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
from typing import List

"""
1337. K Слабейших Рядов в Матрице
Условие:
Дана матрица m x n из единиц (солдаты) и нулей (гражданские). В каждой строке все единицы стоят левее всех нулей.
Ряд i слабее ряда j если:
В ряду i меньше солдат, чем в ряду j
Или солдат поровну, но индекс i < j
Вернуть индексы k слабейших рядов, отсортированных от слабого к сильному.
"""
"""
Задача состоит из двух частей:
Часть 1 — Подсчёт солдат в строке. Строка — это отсортированный массив [1,1,1,0,0]. Как эффективно найти количество
единиц в отсортированном массиве? Есть два способа — простой O(n) и умный O(log n). Подумай — какой паттерн применяется
для поиска в отсортированном массиве?
Часть 2 — Выбор k наименьших элементов. Есть список пар (количество солдат, индекс строки). Нужно взять k наименьших.
Здесь тоже два подхода — простая сортировка O(m log m) и структура данных для k наименьших элементов O(m log k).

Декомпозиция на подзадачи
Подзадача 1 — Научиться считать количество солдат в одной строке (сначала простым способом — sum)
Подзадача 2 — Применить это ко всем строкам и создать список пар (кол-во солдат, индекс строки)
Подзадача 3 — Правильно отсортировать этот список с учётом условия задачи
Подзадача 4 — Вернуть первые k индексов
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for i, row in enumerate(mat):
            result.append((sum(row), i))

        return [row[-1] for row in sorted(result)[:k]]


if __name__ == '__main__':
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    k = 3
    sol = Solution()
    print(sol.kWeakestRows(mat, k))
