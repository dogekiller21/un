#Array16

def inp_lst():
    n = int(input('Введите N: '))
    lst = [int(input(f'Число номер {i+1} = ')) for i in range(n)]
    return lst

def new_lst(lst):
    count = 0
    cnt = 0
    new_list = []
    for i in range(1, len(lst) * 2 + 1):
        if i % 2 != 0:
            new_list.append(lst[cnt])
            cnt += 1
        else:
            new_list.append(lst[len(lst) - count - 1])
            count += 1
    return new_list

print(new_lst(inp_lst()))

