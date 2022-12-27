#1. Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
with open('d.txt', 'r', encoding='utf-8') as file:
    d = file.readline()
    for i in range(len(d)):
        if d[i] == '.':
            c = len(d) - 1 - i
    print(round(math.pi, c))

 