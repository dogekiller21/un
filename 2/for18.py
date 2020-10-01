a = int(input('Введите число A '))
n = int(input('Введите целое число '))
r = 1
s = int(1)
for i in range(0, n):
    s *= a*-1
    r += s
print(r)
