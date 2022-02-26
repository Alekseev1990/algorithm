"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""

x = [63, 43, 23, 123, 26, 4784, 34, 13]


def min_in_list(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
        return lst[i]


print(min_in_list(x))


def min_in_list2(lst2):
    low = lst2[0]
    for i in lst2:
        if i < low:
            low = i
    return low


print(min_in_list2(x))
