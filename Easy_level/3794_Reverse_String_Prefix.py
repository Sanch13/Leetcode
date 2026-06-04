"""
3794. Reverse String Prefix
You are given a string s and an integer k.
Reverse the first k characters of s and return the resulting string.

Example 1:
Input: s = "abcd", k = 2
Output: "bacd"

Explanation:​​​​​​​
The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

Example 2:
Input: s = "xyz", k = 3
Output: "zyx"

Explanation:
The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

Example 3:
Input: s = "hey", k = 1
Output: "hey"

Explanation:
The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
1 <= k <= s.length
"""
"""
Задача: Разворот префикса строки
Дана строка s и число k.
Разверни первые k символов строки s и верни результат.
Примеры:

"abcd", k=2 → "bacd" (перевернули "ab" → "ba")
"xyz", k=3 → "zyx" (перевернули всю строку)
"hey", k=1 → "hey" (один символ — не меняется)
"qwerty", k=3 → "ewqrty"
"qwertyuio", k=4 → "rewqtyuio"
"""
"""
Шаблон решения
Эта задача — классический пример шаблона "Two Pointers" (два указателя).
Жизненная аналогия: представь очередь из людей. Тебе нужно переставить только первых k человек в обратном порядке. Остальные стоят и ждут — ты их не трогаешь.
Суть шаблона Two Pointers:
Ставишь два указателя — один в начало, другой в конец нужного участка — и двигаешь их навстречу друг другу, меняя элементы местами.
"a  b  c  d"
  ↑     ↑
left   right

Декомпозиция на подзадачи
Подзадача 1 — Выдели нужный участок:
Определи, какие символы строки ты будешь разворачивать, а какие — оставишь нетронутыми. Как бы ты разбил строку на две части?
"""


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        left = 0
        right = k - 1

        arr = list(s)
        while left <= right:
            arr[left], arr[right] = arr[right] , arr[left]
            left += 1
            right -= 1

        return "".join(arr)


if __name__ == '__main__':
    s = "hey"
    k = 1
    sol = Solution()
    print(sol.reversePrefix(s, k))


    assert sol.reversePrefix(s="qwerty", k=3) == "ewqrty" , "Fail Test"
    assert sol.reversePrefix(s="qwertyuio", k=4) == "rewqtyuio" , "Fail Test"
    assert sol.reversePrefix(s="qwertyuio", k=5) == "trewqyuio" , "Fail Test"
