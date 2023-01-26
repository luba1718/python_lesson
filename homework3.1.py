# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in 5 out [10, 2, 3, 8, 9] -> 22, 
# in 4 out [4, 2, 4, 9] -> 8

from random import sample

def num_rand_list (count: int):
    if count < 0:
        print ("negative")
        return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums
def sum_odd_pos( list_nums: list):
    sum_nums = 0
    for i in range(0, len(list_nums), 2):
        sum_nums += list_nums[i]
    return sum_nums
a_list = num_rand_list(int(input()))
print(a_list)
print(sum_odd_pos(a_list))