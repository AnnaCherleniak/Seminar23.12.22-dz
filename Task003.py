#3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

with open('numbers.txt', 'r', encoding='utf-8') as file:
    numbers = file.readline().split()
    some_list = []
    for el in numbers:
        if int(el) not in some_list:
            some_list.append(int(el))
    print(some_list)