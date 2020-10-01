n = int(input('Введите натуральное число больше 2: '))

#проверка на дурака
if n <= 2:
    while n <= 2:
        print('Введено число меньше или равное 2')
        n = int(input('Введите натуральное число больше 2: '))

seq = [1, 2, 3]

for i in range(3, n):
    a = seq[i-1] + seq[i-2] - 2*seq[i-3]
    seq.append(a)

seq = list(map(str, seq))   #перевод чисел в строку
print(', '.join(seq))
