'''
Задача 32:
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше
заданного максимума)
'''

import random

my_list = [random.randint(-100, 100) for i in range(10)]
print(my_list)
for _ in range(len(my_list)):
    max_i = int(input("MAX= "))
    min_i = int(input("MIN= "))
    mas_i = []
    if max_i >= min_i:
        for i in range(len(my_list)):
            if max_i >= my_list[i] and min_i <= my_list[i]:
                mas_i.append(i)
    print("Кол-во:", len(mas_i))
    print("Индексы:", mas_i)


