k = int(input('Введите целое число K: '))
c = 'Таких чисел нет'

def inputA():
    b = int
    a = []
    while b!=0:
        b = int(input())
        a.append(b)
    return a

def src(list, int):
    print(list)
    for i in range(len(list)):
        if list[i] > int:
            a = i+1

    return a

print('Вводите числа в список(0 всегда будет последним числом списка)')
a = inputA()
b = src(a, k)
print(b)




