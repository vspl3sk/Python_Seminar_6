# 1. Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший
# общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший
# общий делитель для списка натуральных чисел. Ввод чисел продолжается
# до ввода пустой строки.

# Входные данные
# 36
# 12
# 144
# 18
# Выходные данные
# 6

# def NOD( a, b): 
#     if a > b:
#         temp = b 
#     else: 
#         temp = a 
#     for i in range(1, temp + 1): 
#         if(( a % i == 0) and(b % i == 0 )): 
#             gcd = i 
#     return gcd 
# x = int(input(" Введите первое число: ") ) 
# y =int(input(" Введите второе число: "))   
# num = NOD(x, y) 
# print("НОД двух чисел: ") 
# print(num)

# Не хватило времени для реализации алгоритма на несколько чисел, в ближайшее время исправлю

# 2. Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует
# выпадению Решки. Напишите программу, которая подсчитывает наибольшее
# количество подряд выпавших Решек.

# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского
# алфавита "О" и "Р".
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные Выходные данные
# ОРРОРОРООРРРО 3
# ООООООРРРОРОРРРРРРР 7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР 31

# s = input()
# count, m = 0, 0
# for i in s:
#     if i == 'Р':
#         count += 1
#         if count > m:
#             m = count
#     elif i != 'Р':
#         count = 0
# print(m)