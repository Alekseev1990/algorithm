

@time_measure
def dict_del(n):
    return my_dict.pop(n)           # O(1)


@time_measure
def lst_del(n):
    return my_lst.pop(n)            # O(n)


@time_measure
def lst_change():
    for i in range(len(my_lst)):    # O(n)
        my_lst[i] = 100             # O(n)
    return


@time_measure
def dict_change():
    for i in my_dict.keys():        # O(n)
        my_dict[i] = 100            # O(1)
    return


print('Время на удаление элемента из списка -', lst_del(9999997))
print('Время на удаление элемента из словаря -', dict_del(9999997))
print('Время на изменение элемента из списка -', lst_change())
print('Время на изменение элемента из словаря -', dict_change())

# Список - 0.05 сек и 3.29 сек, словарь - 0.0 сек и 2.8 сек соответственно. Операции со словарем быстрее, потому




import re

def fourletters(names):
    result = re.findall(r'\b[a-zA-Z]{4}\b', names)
    count = len(result)
    return count

# print(fourletters("Inili Dori Maordris"))
#
#
# import re
#
# def fourletters(names):
#     result = re.findall(r'\b[a-zA-Z]{4}\b', names)
#     count = len(result)
#     return count
#
#
# names = input()
# print(fourletters(names))


#
# Реализуйте функцию get_total_time
#
# def get_total_time(heroes, n):
#     sum = 0
#     for i in heroes:
#         if n == 1:
#             sum += i
#         elif n == 2:
#             if heroes[0] > heroes[1] and heroes[0] > heroes[2] + heroes[3]:
#                 return heroes[0]
#             elif heroes[0] + heroes[1] < heroes[2]:
#                 return heroes[0] + heroes[2]
#     return sum


# print(get_total_time([1,2,3], 2))

# def broken_device(x, y):
#     ans = 0
#     while y > x + 1:
#         if y % 2 == 0:
#             y += 1
#             x += 1
#         else:
#             y /= 2
#     return ans + x - y
#
# print(broken_device(5, 7))

def broken_device(x, y):
    count = 0
    if x == 0:
        return 1
    elif y > x:
        count += 2
        print(count), broken_device((x - 1) * 2, y)
    else:
        count += 1
        return count, broken_device(x - 1, y)

print(broken_device(5, 8))





#     while y > x + 1:
#         count += 2
#         broken_device((x - 1) * 2, y)
#         print(count)
#         if x > y:
#             count += 1
#             print(count)
#
# (broken_device(2, 4))