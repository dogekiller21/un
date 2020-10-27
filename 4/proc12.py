#Proc12

def SoftInc3(lst):
    return sorted(lst)

def inp():
    print('Введите 3 числа в список: ')
    lst = [int(input()) for i in range(3)]
    return lst

lst1 = ', '.join(map(str, SoftInc3(inp())))
lst2 = ', '.join(map(str, SoftInc3(inp())))
print(f'{lst1}\n{lst2}')


