print("Работу выполнил: Поляков Максим Александрович\n"
      "Группа: ИС-29\n"
      "Задание: Определение емкости участка цепи A-B\n"
      "Участок цепи псевдографикой\n")

print("A  1    2    3     \n"
      "━━┫┣━━━┫┣━┳━┫┣━┓   \n"
      "     ┏━━━━┻━━━━┫   \n"
      "━━┫┣━┻━┫┣━━━┫┣━┛   \n"
      "B  4    5    6     \n")

data = []
while len(data) < 6:
    number = input(f"Введите значение {len(data)+1}: ")
    try:
        data.append(float(number))
    except ValueError:
        print("Некорретное значение")

result = (data[0] * data[1] * data[5] /
          (data[1]*data[5] + data[0]*data[5] + data[0]*data[1]))
print(f"Общая емкость цепи: {result:.3f}")
