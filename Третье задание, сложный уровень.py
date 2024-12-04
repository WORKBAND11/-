import math
n = int(input("Введите число n:" )) #вводим число n
k = int(input("Введите число k:" )) #вводим число л
divisor =  math.factorial(k) * math.factorial(n - k) #считаем делитель
C = math.factorial(n) / divisor #считаем итоговое выражение
print("Количество сочетаний n и k:", C) #и выводим ответик))

