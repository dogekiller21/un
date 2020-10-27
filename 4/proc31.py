#Proc31

def IsPalindrom(num):
    word = str(num)
    if word == word[::-1]:
        return True
    return False

print(IsPalindrom(input('Введите число: ')))


