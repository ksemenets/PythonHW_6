# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
min_num = int(input("введите минимальное число "))
max_num = int(input("введите максимальное число "))
num_list = [randint(0, 20)for i in range(20)]
print(num_list)

index_list = list()
for i in range(20):
    if min_num < num_list[i] < max_num:
        index_list.append(i)
print(index_list)