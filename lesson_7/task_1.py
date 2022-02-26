"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

import random
from timeit import timeit

numbers = [random.randint(-100, 100) for _ in range(10)]


def bubble_insert(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


print(bubble_insert(numbers))
print(timeit("bubble_insert(numbers)", globals=globals()))  # 22.950116117


def bubble_insert_2(nums):
    n = 1
    count=0
    flag = True
    for j in range(len(nums) - n):
        if flag is False:
            return nums
        flag = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                flag = True
            count += 1
    return nums


print(bubble_insert_2(numbers))  # 22.840960919
print(timeit("bubble_insert(numbers)", globals=globals()))



# def bubble_insert_2(nums):
#     n = 1
#     while n < len(nums):
#         x = True
#         for i in range(len(nums) - n):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 x = False
#         if x == True:
#             break
#     return nums