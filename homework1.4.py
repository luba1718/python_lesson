# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

quater = int(input())

if quater == 1:
    print ("x > 0, y > 0")
elif quater == 2:
    print ("x < 0 < y")
elif quater == 3:
    print ("x < 0, y < 0")
elif quater == 4:
    print ("x > 0 > y")
else:
    print("нет такой четверти")