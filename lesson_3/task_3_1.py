"""
Задание 1.
Реализуйте:
a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.
b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.
ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def sep():
    print('-' * 50)


lst = []
dct = dict()


def benchmark(func):

    def time_func(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start

    return time_func


@benchmark
def my_list(n):
    for i in range(n):  # O(n)
        lst.append(i)   # O(1)


@benchmark
def my_dict(n):
    for i in range(n):  # O(n)
        dct[i] = i  # O(1)


print("Время заполнение списка: ", my_list(10000000))  # 0.169, 0.200 время исполнения
print("Время заполнение словаря: ", my_dict(10000000))  # 0.170, 0.209 время исполнения

#  При одинаковой линейной О-нотации, время заполнения списка быстрей, так как в него добавляется только элемент,
#  в словарь же попадает пара ключ:значение, что отображается на объеме данных и, соответственно, скорости.
sep()


@benchmark
def my_list_b():
    for i in range(len(lst)):
        # O(1) в списке хранятся значения, значит операция будет выполняться определенное кол-во раз
        lst[i] = 1  # O(1)
    return


@benchmark
def my_dict_b():
    for i in range(len(dct)):
        # O(1) в словаре хранятся значения, значит операция будет выполняться определенное кол-во раз
        dct[i] = 1  # O(1)
    return


@benchmark
def pop_my_lst_b():
    for i in range(len(lst)):  # количество элементов не изменилось
        return lst.pop(i)  # O(N)


@benchmark
def pop_my_dict_b():
    for i in range(len(dct)):  # количество элементов не изменилось
        return dct.pop(i)  # O(1)


print("Время изменения списка: ", my_list_b())  # 0.102, 0.131 1.018 время исполнения
print("Время изменения словаря: ", my_dict_b())  # 0.135, 0.141 1.545 время исполнения 1.545
print("Время удаления элементов списка: ", pop_my_lst_b())  # 0.0009 время исполнения
print("Время удаления элементов словаря: ", pop_my_dict_b())  # 0.0  время исполнения

# При одинаковой О-нотации, время изменения и удаления словаря меньше, так как в списке нужно обработать каждый индекс
# Удаление элементов быстрей происходит из словаря, так как встроенная функция pop у словаря имеет константную
# сложность, а у списка линейную.


