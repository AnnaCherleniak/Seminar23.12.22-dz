#5. НЕОБЯЗАТЕЛЬНАЯ Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
#with open('first.txt', 'w', encoding='utf-8') as file:
 #   file.write('')
#with open('second.txt', 'w', encoding='utf-8') as file:
 #   file.write('')
with open('first.txt', 'r', encoding='utf-8') as file:
    first_list = file.read().split(' + ')
    print(first_list)
with open('second.txt', 'r', encoding='utf-8') as file:
    second_list = file.read().split(' + ')
    print(second_list)


some_dict1 = {}
for el in first_list:
    if '*' in el:
        some_dict1[el[el.index('*'):]] = el[:el.index('*')]
    else:
        some_dict1[''] = el
print(some_dict1)
some_dict2 = {}
for el in second_list:
    if '*' in el:
        some_dict2[el[el.index('*'):]] = el[:el.index('*')]
    else:
        some_dict2[''] = el
print(some_dict2)
res_list = []
for i in some_dict1:
    if i in some_dict2:
        res_list.append(int(some_dict1[i]) + int(some_dict2[i]))
        if i != '':
            res_list.append(i)
    else:
        res_list.append(int(some_dict1[i]))
        if i != '':
            res_list.append(i)
for i in some_dict2:
    if i not in some_dict1:
        res_list.append(int(some_dict1[i]))
        if i != '':
            res_list.append(i)
print(res_list)


some_list1 = []
for el in first_list:
    if '*' in el:
        some_list1.append(int(el[:el.index('*')]))
        some_list1.append(el[el.index('*'):])
    else:
        some_list1.append(int(el))
#print(some_list1)
some_list2 = []
for el in second_list:
    if '*' in el:
        some_list2.append(int(el[:el.index('*')]))
        some_list2.append(el[el.index('*'):])
    else:
        some_list2.append(int(el))
#pint(some_list2)
