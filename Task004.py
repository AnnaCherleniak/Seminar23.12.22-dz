#4. НЕОБЯЗАТЕЛЬНАЯ Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

with open('k.txt', 'w', encoding='utf-8') as file:
    k = int(input())
    f_List = []
    for i in range(k, -1, -1):
        a = random.randint(0, 100)
        if a > 0:
            if i == 1:
                f_List.append(str(a) + '*x')
            elif i == 0:
                f_List.append(str(a))
            else:
                f_List.append(str(a) + '*x^' + str(i))
    for i in range(len(f_List) - 1):
        file.write(str(f_List[i]) + ' + ')
    file.write(str(f_List[-1]))
    

    