"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

from hashlib import md5


def unique_str(string: str):
    len_str = len(string)
    hash_code = set()
    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            if i != j and string[i:j] != string:
                hash_code.add(md5(string[i:j].encode()).hexdigest())
                print(string[i:j])
    # print(hash, f'Количество элементов:  {len(hash)}')


unique_str("трали-вали")