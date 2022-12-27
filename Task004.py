#4. НЕОБЯЗАТЕЛЬНАЯ Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
with open('k.txt', 'r', encoding='utf-8') as file:
    k = int(file.readline())
    a, b, c = random.randint (1, 100), random.randint(0, 100), random.randint(0, 100)
    if b == 0 and c == 0:
        print(f'{a}*x^2')
    elif c == 0:
        print(f'{a}*x^2 + {b}*x')
    elif b == 0:
        print(f'{a}*x^2 + {c}')
    else:
        print(f'{a}*x^2 + {b}*x + {c}')
    

    