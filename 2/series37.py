k = int(input('Введите целое число K: '))

listlist = []
a = []
i = 1

while i <= abs(k):
    print('Введите в список минимум два числа, отличных от нуля(0 - незначимое число, означающее конец списка)')
    while True:
        b = int(input())
        a.append(b)
        if b == 0:
            if len(a) == 2:
                a.remove(0)
                print('Список не может содержать меньше двух чисел, отличных от нуля')
            else:
                break
    listlist.append(a.copy())
    a.clear()
    i += 1

print(listlist)

cnt_y = 0
cnt_v = 0
for elem in (listlist):
    j = 0
    for j in range(len(elem)-3):
        if elem[j] > elem[j+1]:
            j += 1
        else:
            break
    if elem[j] > elem[j+1]:
        cnt_y += 1

for elem in (listlist):
    j = 0
    for j in range(len(elem)-3):
        if elem[j] < elem[j+1]:
            j += 1
        else:
            break
    if elem[j] < elem[j+1]:
        cnt_v += 1
print('Количество убывающих списков: ', cnt_y)
print('Количество возрастающих списков: ', cnt_v)
print('Количество возрастающих и убывающих список: ', cnt_y+cnt_v)





























