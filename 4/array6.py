#Array6

n = int(input('Введите N = '))
a = int(input('Введите A = '))
b = int(input('Введите B = '))

lst = [a,b]

for i in range(n):
    lst.append(sum(lst))

print(lst)


