k = int(input('Введите целое число K: '))

listlist = []
def listB():
    a = []
    while True:
        b = int(input())
        a.append(b)
        if b == 0:
            if len(a) == 2:
                a.remove(0)
                print('Список не может содержать меньше двух чисел, отличных от нуля')
            else:
                return a

def dec_lists(list):
    cnt = 0
    for elem in (list):
        j = 0
        for j in range(len(elem) - 3):
            if elem[j] > elem[j + 1]:
                j += 1
            else:
                break
        if elem[j] > elem[j + 1]:
            cnt += 1
    return cnt

def inc_lists(list):
    cnt = 0
    for elem in (list):
        j = 0
        for j in range(len(elem) - 3):
            if elem[j] < elem[j + 1]:
                j += 1
            else:
                break
        if elem[j] < elem[j + 1]:
            cnt += 1
    return cnt

for i in range(0, abs(k)):
    print('Введите в список минимум два числа, отличных от нуля(0 - незначимое число, означающее конец списка)')
    a = listB()
    listlist.append(a.copy())

print(listlist)

cnt_y = dec_lists(listlist)
cnt_v = inc_lists(listlist)

print('Количество убывающих списков: ', cnt_y)
print('Количество возрастающих списков: ', cnt_v)
print('Количество возрастающих и убывающих список: ', cnt_y+cnt_v)





























