# Задача 26:  Напишите программу, которая на вход
# принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
import math


def degree(a, b):
    if b == 1:
        return a
    if b != 1:
        return (a * degree(a, b - 1))

numberA = int(input("введите число А:   "))
numberB = int(input("введите число В:   "))

print(f"A = {numberA}; B = {numberB} -> {degree(numberA, numberB)}")

