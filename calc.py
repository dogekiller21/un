import math

print('Инструкция:')
print('Чтобы узнать сумму двух чисел, введите между ними (+)')
print('Чтобы узнать сумму двух чисел, введите между ними (+)')
print('Чтобы узнать разность двух чисел, введите между ними (-)')
print('Чтобы узнать произведение двух чисел, введите между ними (*)')
print('Чтобы узнать частное двух чисел, введите между ними (/)')
print('Чтобы возвести число в степень, введите (Число ^ Степень)')
print('Чтобы получить процент от числа, введите (Число {Процент%})')
print('Чтобы вычислить корень из числа, введите (Число # СтепеньКорня)')
print('Чтобы вычислить синус числа, введите (sin Число)')
print('Чтобы вычислить косинус числа, введите (cos Число)')
print('Чтобы вычислить тангенс числа, введите (tg Число)')
print('Чтобы сбросить текущее значение, введите c после числа \n')


op = ['+', '-', '*', '/', '^', '#']
trig = ['sin', 'cos', 'tg']
r = None

#Проверка, может ли быть строка переделана в число
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#Функции для подсчетов
def plus(first_num, second_num):
    return float(first_num) + float(second_num)

def minus(first_num, second_num):
    return float(first_num) - float(second_num)

def multiply(first_num, second_num):
    return float(first_num) * float(second_num)

def divide(first_num, second_num):
    return float(first_num) / float(second_num)

def exp(first_num, second_num):
    return float(first_num) ** float(second_num)

def root(first_num, second_num):
    return float(first_num) ** (1/(float(second_num)))

def percent(first_num, second_num):
    return float(first_num)/100 * float(second_num)

def sin(num):
    return math.sin(float(num))

def cos(num):
    return math.cos(float(num))

def tan(num):
    return math.tan(float(num))

#Подтягивание функций к переданным этой функции спискам
def count(lst):
    count_ops = {'+': plus,
                 '-': minus,
                 '*': multiply,
                 '/': divide,
                 '^': exp,
                 '#': root,
                 '%': percent,
                 'sin': sin,
                 'cos': cos,
                 'tg': tan}
    if len(lst) == 3:
        first_num, operation, second_num = lst
        a = count_ops[operation](first_num, second_num)
        if a % 1 != 0:
            return float(a)
        else:
            return int(a)
    if len(lst) == 2:
        operation, num = lst
        a = count_ops[operation](num)
        if a % 1 != 0:
            return float(a)
        else:
            return int(a)

#Перевод из (100 10%) в (100 % 10)
def percent_remove(target):
    a = list(target[1])
    del a[-1]
    a = ''.join(a)
    del target[-1]
    target.append('%')
    target.append(a)
    return target

#Замена (1 sin) на (sin 1)
def trig_replace(lst):
    if lst[0] in trig:
        return lst
    else:
        lst[0], lst[1] = lst[1], lst[0]
        return lst

#Ввод действий и передача их в руки функциям для подсчета
def inp():
    global r
    while True:
        a = []
        if r is not None:
            a.append(str(r))
            a.extend(input(f'{r} ').split())
            if len(a) != 1 and (a[1] == 'c' or a[1] == 'с'):
                r = None
                continue
            elif len(a) != 1 and (a[1] == 'thx'):
                print('Special thx 2 Nikolay Samedov')
                continue
        else:
            print('Введите математическое выражение')
            a = input('').split()
            if len(a) == 1 and (a[0] == 'thx'):
                print('Special thx 2 Nikolay Samedov')
                continue
        if len(a) == 2:
            if a[0] in trig or a[1] in trig:
                if is_number(a[1]) or is_number(a[0]):
                    a = trig_replace(a)
                    r = count(a)
                    continue
            if list(a[1])[-1] == '%':
                r = count(percent_remove(a))
                continue
        if len(a) == 3:
            if a[1] in op:
                if is_number(a[0]) and is_number(a[2]):
                    r = count(a)
                    continue
                else:
                    print('2 numbers and operation b/t expected')
            else:
                print('Math operation is out of range')
        else:
            print('3 values expected (or sin/cos/tg *value*)')


#Бесконечный цикл основной функции
while True:
    inp()