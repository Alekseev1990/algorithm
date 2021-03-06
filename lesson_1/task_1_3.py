"""
Задание 3.
Для этой задачи:
придумайте 2-3 решения (обязательно с различной сложностью)
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

import heapq, operator

a = {'a': 100, 'b': 250, 'c': 90, 'd': 300, 'e': 150}

result = sorted(a.items(), key=operator.itemgetter(1), reverse=True)[:3]  # O(N log N) сортировка
print(result)


print(heapq.nlargest(3, a.items(), key=operator.itemgetter(1)))


