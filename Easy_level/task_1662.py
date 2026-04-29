"""
1662. Check If Two String Arrays are Equivalent
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""
from typing import List

"""
Условие:
Даны два массива строк word1 и word2. Верни True, если оба массива представляют одну и ту же строку, иначе False.
Массив представляет строку, если элементы массива, склеенные по порядку, образуют эту строку.
Примеры:

["ab", "c"] и ["a", "bc"] → True, потому что оба дают "abc"
["a", "cb"] и ["ab", "c"] → False, потому что "acb" ≠ "abc"
"""
"""
Время O(n)где n — суммарная длина всех символов. Проходим по каждому символу один раз
Память O(n)создаём две новые строки в памяти
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

if __name__ == '__main__':
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    sol = Solution()
    print(sol.arrayStringsAreEqual(word1, word2))


"""
1. Почему мы пишем именно `"".join(...)` с пустой строкой, а не, например, `" ".join(...)`? - это разделитель. все символы были бы разделены пробелом
2. Что вернёт функция `join` если передать ей пустой массив `[]`? И как это повлияет на наше решение? - пустую строку. если два джоина с пустыми массивами то всегда будет тру
3. Constraints говорят что суммарная длина символов `<= 10³`. Как ты думаешь — это подсказка о том, что решение не обязано быть супер-оптимальным? Почему? - да, до этого значения выполнится очень быстро

## Все три ответа верные! ✅
Небольшие уточнения для закрепления:
**По ответу 1** — точно. `" ".join(["ab", "c"])` дало бы `"ab c"`, а не `"abc"`. Разделитель вставляется **между** элементами.
**По ответу 2** — верно. И это важно: поConstraints гарантировано что `word1.length >= 1` и `word1[i].length >= 1`, значит пустых массивов в этой задаче **не будет**. Но ты правильно подумал в правильном направлении — это называется **edge case** мышление. Хорошая привычка.
**По ответу 3** — верно. `10³ = 1000` символов максимум. Это очень маленький input. Даже O(n²) решение отработало бы мгновенно. Constraints — это всегда подсказка о допустимой сложности алгоритма. Запомни это правило:
```
n <= 10³    → сойдёт даже O(n²)
n <= 10⁵    → нужно O(n log n) или O(n)
n <= 10⁶+   → только O(n) или O(log n)
```
"""