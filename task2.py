# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))

def func_with_map(string):
    tp = tuple(map(str, string.split()))
    tt=list()
    for i in tp:
        tt.append(i.split('='))
    return tuple(tuple(c for c in s) for s in tt)

string = 'house=дом car=машина men=человек tree=дерево'    
print(func_with_map(string))

