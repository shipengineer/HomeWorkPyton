# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import math
spisok1 = [1, 2, 3, 4, 5, 6, 7, 1, 10]
proverka = [2, 3, 5, 9, 3]


def sumEven(mas):
    sum = 0
    for i in range(1, len(mas), 2):
        sum += mas[i]
    print(sum)


# sumEven(spisok1)
# sumEven(proverka)
# ____________________________________________________________________________________________________

# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])
# В скобках пример, как это работает!!!
proverka32 = [2, 3, 4, 5, 6]
proverka322 = [2, 3, 5, 6]


def parMult(mas):
    result = []
    count = len(mas)
    for i in range(int(count/2)):
        result.append(mas[i]*mas[int(len(mas)-i-1)])
    if len(mas)/2 % 1 > 0:
        result.append(mas[int(len(mas)/2)]**2)
    print(result)


# parMult(proverka32)
# parMult(proverka322)
# ____________________________________________________________________________________________________


# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
test1 = [1.1, 1.2, 3.1, 5, 10.01]


def maxDif(mas):
    mutable = [round(i % 1, 2) for i in mas if i % 1 != 0]
    print(max(mutable)-min(mutable))


# maxDif(test1)
# ____________________________________________________________________________________________________


# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# inputNumber = int(input("Введите число: "))


def binar(number):

    result = ""
    while number != 0:
        result = str(number % 2) + result
        number //= 2
    print(result)


# binar(inputNumber)
# ____________________________________________________________________________________________________


# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# testNumber = int(input("Число размера последовательности: "))
a = []


def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


def negativeFibonacci(num):
    result = []
    if num % 2 == 0:
        pn = -1
    else:
        pn = 1
    for i in range(-num, num+1):
        if i < 0:
            result.append(pn*fibonacci_of(-1*i))
            pn *= -1
        else:
            result.append(fibonacci_of(i))
    print(result)


negativeFibonacci(10)
