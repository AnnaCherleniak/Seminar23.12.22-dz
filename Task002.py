#2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
import math
with open('N.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    some_list = []
    for i in range(2, math.ceil(n**0.5) + 1):
        if n % i == 0:
            some_list.append(i)
            n /= i
    print(some_list)
