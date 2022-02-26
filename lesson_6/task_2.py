"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
import memory_profiler
from copy import deepcopy
from memory_profiler import profile

# @profile
# def calculate():
#     s = input("Введите операцию (+, -, *, / или 0 для выхода): ")
#     if s not in ('+', '-', '*', '/', '0'):
#         print("Неизвестная операция"), calculate()
#     elif s == '0':
#         print("Вы вышли из калькулятора")
#     else:
#         a = input()
#         b = input()
#         if a.isdigit() and b.isdigit():
#             a = int(a)
#             b = int(b)
#             if s == '+':
#                 print(f'Ваш результат {a + b}'), calculate()
#             elif s == '-':
#                 print(f'Ваш результат {a - b}'), calculate()
#             elif s == '*':
#                 print(f'Ваш результат {a * b}'), calculate()
#             elif s == '/' and b != 0:
#                 print(f'Ваш результат {a / b}'), calculate()
#             else:
#                 print("На 0 делть нельзя"), calculate()
#         else:
#             print("Введите число")
#             return calculate()
#
#
# print(calculate())

@profile
def rev_digit(num, res=''):
    if num == 0:
        return print(res)
    else:
        print(num % 10, end='')
        rev_digit(num // 10)


rev_digit(120300040)

# Проблема заключается в том, что профилировщик вызывается столько же раз, сколько выполняется рекурсия.
# В конкретном примере, с числом 120300040 замерщик вызывается 9 раз, по количеству цифр.
# Чтобы сократить количество расчетов, можно использовать декоратор и обернуть функцию, что позволит замерить
# ее результат в целом, а не пошаговое исполнение


@memory_profiler.profile
def wrapper(recursive_func, arg):
    result = recursive_func(arg)
    return result


print(wrapper(rev_digit, 120300040))


