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
    print(f'Введите данные для фигуры номер {num + 1}')
    m = int(input('a = '))
    v = int(input('b = '))
    return 2*(m+v)

a = [inpD(i) for i in range(int(input('Введите число прямоугольников: ')))]

print(', '.join([str(elem) for elem in a]))
i, p = maxP(a)
print(f'Ппямоугольник под номером {i} имеет наибольший периметр, равный {p}')


