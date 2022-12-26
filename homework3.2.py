# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in 4 out [2, 5, 8, 10] [20, 40]
# in 5 out [2, 2, 4, 8, 8] [16, 16, 4]

from random import sample
def num_rand_list (count):
    if count < 0:
        print ("negative")
        return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums
def prod_elem(list_nums: list):
    new_list = []
    len_list = len(list_nums)
    for i in range(len_list //2):
        new_list.append(list_nums[i] * list_nums[len_list - i -1])
    if len_list % 2:
        new_list.append(list_nums[len_list // 2])
    return new_list
a_list = num_rand_list(int(input()))
print (a_list)
print (prod_elem(a_list))