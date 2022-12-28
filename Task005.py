#5. НЕОБЯЗАТЕЛЬНАЯ Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
#with open('first.txt', 'w', encoding='utf-8') as file:
 #   file.write('2*x^2 + 5*x + 5 + 5*x^3')
#with open('second.txt', 'w', encoding='utf-8') as file:
 #   file.write('7*x^2 + 1*x + 5')
with open('first.txt', 'r', encoding='utf-8') as file:
    first_list = file.read().split(' + ')
with open('second.txt', 'r', encoding='utf-8') as file:
    second_list = file.read().split(' + ')

some_dict1 = {}
for el in first_list:
    if '*' in el:
        some_dict1[el[el.index('*'):]] = el[:el.index('*')]
    else:
        some_dict1[''] = el
some_dict2 = {}
for el in second_list:
    if '*' in el:
        some_dict2[el[el.index('*'):]] = el[:el.index('*')]
    else:
        some_dict2[''] = el
res_list = []
for i in some_dict1:
    if i in some_dict2:
        res_list.append(str(int(some_dict1[i]) + int(some_dict2[i])) + i)
    else:
        res_list.append(some_dict1[i] + i)
for i in some_dict2:
    if i not in some_dict1:
        res_list.append(some_dict1[i] + i)
with open('res.txt', 'w', encoding='utf-8') as file:
    for i in range(len(res_list) - 1):
        file.write(str(res_list[i]) + ' + ')
    file.write(str(res_list[-1]))

