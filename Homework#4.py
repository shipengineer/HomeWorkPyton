# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
import random
import math
import sympy


def roundPi(d):
    count = len(d)
    pi = str(math.pi)
    print(pi[:count])


# roundNumber = input("Укажите сколько знаков после запятой (Пример: 0.0001) : ")
# roundPi(roundNumber)
# ____________________________________________________________________________________________________

# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def SimpMult(num):
    result = [1]
    i = 2
    mutable = num
    while i <= num:
        if num % i == 0:
            if i not in result:
                result.append(i)

            num //= i
        else:
            i += 1
    print(f'Простые множители числа {mutable} : {result}')


# Nnum = int(input("Введите число для разложения на простые множители: "))
# SimpMult(Nnum)
# ____________________________________________________________________________________________________

# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def onceTime(mas):
    print(set(mas))


# row = [1, 2, 3, 45, 3, 1, 99, 98, 99]
# onceTime(row)
# ____________________________________________________________________________________________________

# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0


def generateEql(k):
    power = ""
    for i in range(k+1):
        constant = random.randint(0, 11)
        if constant != 0 and i < k-1:
            power = power + f"{constant}*x**{k-i} + "
        elif constant != 0 and i == (k-1):
            power = power + f"{constant}*x + "
        elif constant != 0:
            power = power + f"{constant}"
    with open('file 44(1).txt', 'w') as data:
        data.write(power)


# generateEql(10)

def sumEql():
    with open('file 44(1).txt', 'r') as data:
        eql1 = data.readline()

    with open('file 44(2).txt', 'r') as data:
        eql2 = data.readline()

    # print(eql1+eql2)

    print(sympy.simplify(f'{eql1} + {eql2}'))


sumEql()