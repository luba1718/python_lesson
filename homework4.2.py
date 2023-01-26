# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# in 54 out [2, 3, 3, 3]
# in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]

num = int(input("Введите число: "))
i = 2 
new_lst = []
old = num
while i <= num:
    if num % i == 0:
        new_lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old}: {new_lst}")