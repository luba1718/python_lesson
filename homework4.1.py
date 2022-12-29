# 1. Вычислить число c заданной точностью d
# in Enter a real number: 9 Enter the required accuracy '0.0001': 0.000001
# out 9.000000
# in Enter a real number: 8.98785 Enter the required accuracy '0.0001': 0.001
# out 8.988

def num_d(real_numb):
    d = '0.000'
    d = int(len(d) - 2)
    accuracy_number = round(real_numb, d)
    return accuracy_number

n = float(input('Введите вещественное число: '))
t = num_d (n)
print(t)