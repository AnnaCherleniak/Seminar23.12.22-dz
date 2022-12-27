#2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

with open('N.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    some_list = []
    for i in range(2, n):
        if n % i == 0:
            some_list.append(i)
            n /= i
    print(some_list)