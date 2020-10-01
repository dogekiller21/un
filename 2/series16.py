k = int(input('Введите целое число K: '))
a = []
print('Вводите числа в список(0 всегда будет последним числом списка)')
while True:
    b = int(input())
    a.append(b)
    if b == 0:
        break

for i in range(len(a)):
    if a[i] > k:
        b = a[i]

print(b)



