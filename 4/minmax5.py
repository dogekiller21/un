#Minmax5

def maxP(lst):
    max_i = 0
    max_p = 0
    for i in range(len(lst)):
        if lst[i] > max_p:
            max_i = i+1
            max_p = lst[i]
    return max_i, max_p

def inpD(num):
    print(f'Введите данные для детали номер {num + 1}')
    m = int(input('m = '))
    v = int(input('v = '))
    return m/v

a = [inpD(i) for i in range(int(input('Введите число деталей: ')))]

print(', '.join([str(elem) for elem in a]))
i, p = maxP(a)
print(f'Материал детали под номером {i} имеет наибольшую плотность, равную {p}')


