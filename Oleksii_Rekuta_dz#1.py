'''
Task #1
Дані два цілих числа. Виведіть значення найменшого.
'''
# a, b = int(input('Enter first number: ')), int(input('Enter second number: '))
# if a < b:
#     print('The smaller number is', a)
# else:
#     print('The smaller number is', b)

'''
# Task #2
Задано дві клітинки шахівниці. Якщо вони пофарбовані в один колір, виведіть слово YES, 
а якщо в різні кольори - то NO. Програма отримує на вхід чотири числа від 1 до 8 кожне, 
що задають номер стовпця та номер рядка спочатку для першої клітини, потім для другої клітини.
'''
# y1 = int(input('Enter the column number of the first cell: '))
# x1 = int(input('Enter the row number of the first cell: '))
# y2 = int(input('Enter the column number of the second cell: '))
# x2 = int(input('Enter the row number of the second cell: '))
# if (y1 + y2 + x1 + x2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

'''
# Task #3
Якщо вводиться температура в градусах за шкалою Цельсія, вона переводиться в температуру за шкалою Фаренгейта. 
Або навпаки: температура за Фаренгейтом переводиться в температуру за Цельсієм.
'''
# variant = input('Enter "F" for degrees Fahrenheit or enter "C" for degrees Celsius: ')
# if variant == 'F':
#     degrees = int(input('Enter degrees: '))
#     print(degrees, 'degrees Fahrenheit is', (degrees - 32) * 5/9, 'degrees Celsius')
# elif variant == 'C':
#     degrees = int(input('Enter degrees: '))
#     print(degrees, 'degrees Celsius is', (degrees * 9/5) + 32, 'degrees Fahrenheit')
# else:
#     print('Please enter "F" or "C"')

'''
# Task #4
Зі списку випадкових чисел,визначити та вивести на екран непарні числа.
'''
# import random
# lst = []
# for i in range(5):
#     lst.append(random.randint(0, 100))
# print('Our random list -', lst)
# print('The odd numbers are:')
# for i in range(len(lst)):
#     if lst[i] % 2 != 0:
#         print(lst[i])

'''
# Task #5
Вводиться ціле число, що означає код символу за таблицею ASCII. Визначити, 
це код англійської літери або будь-який інший символ.
'''
# num = int(input('Enter your number from 0 to 255: '))
# if 90 >= num >= 65:
#     print('This is an English letter code!')
# else:
#     print('This is a code for a different character.')

'''
# Task #6
Вводяться два цілих числа. Перевірити чи ділиться перше на друге. Вивести на екран повідомлення про це, 
а також залишок (якщо він є) та приватне (у будь-якому випадку).
'''
# a, b = int(input('Enter number a: ')), int(input('Enter number b: '))
# if a % b != 0:
#     print('"A" is not divided by "B", the remainder is:', a % b, '\nPrivate:', a // b)
# else:
#     print('"A" is divided by "B", the private is:', a // b)

'''
# Task #7
По черзі вводиться 5 цифр, вивести їхню суму (скориставшись for)
'''
# sum_num = 0
# for i in range(5):
#     num = int(input('Enter number: '))
#     sum_num += num
# print('The sum of the numbers is:', sum_num)

'''
# Task #8
Дано два цілих числа A і B. Виведіть усі числа від A до B включно, в порядку зростання, 
якщо A < B, або в порядку убування інакше.
'''
# a, b = int(input('Enter number a: ')), int(input('Enter number b: '))
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

'''
# Task #9
Циклом for вивести ромб
'''
# for i in range(1, 10):
#     print(' ' * (9 - i), '* ' * i)
# for i in range(8, 0, -1):
#     print(' ' * (8 - i), ' *' * i)

'''
# Task #10
Порахувати суму числового ряду від 0 до 14 включно. Наприклад, 0+1+2+3+…+14;
'''
# num = int(input('Enter your number: '))
# sum_str = 0
# for i in range(num+1):
#     sum_str += i
# print(sum_str)

'''
# Task #11
Перемножити всі парні значення в діапазоні від 0 до 436
'''
# num = int(input('Enter your number: '))
# sum_str = 1
# for i in range(1, num+1):
#     if i % 2 == 0:
#         sum_str *= i
# print(sum_str)

'''
# Task #12
Задається випадкове речове число. Визначте максимальну цифру цього числа. Приклад виконання: 56.457 -> 7
'''
# num = float(input('Enter your number: '))
# result = 0
# num *= 10000
# while num != 0:
#     last_digit = num % 10
#     num = num // 10
#     if last_digit > result:
#         result = last_digit
# print(int(result))

'''
# Task #13
Факторіалом числа n називається число 𝑛! = 1∙2∙3∙…∙𝑛. Створіть програму, яка обчислює фактор 
введеного користувачем числа. (Цикл!)
'''
# num = int(input('Enter your number: '))
# total = 1
# for i in range(num):
#     i += 1
#     total *= i
# print(total)

'''
# Task #14
Використовуючи вкладені цикли та функції print('*', end=''), print(' ', end='') та print() 
виведіть на екран прямокутний трикутник.
'''
# for i in range(1, 10):
#     print(' ' * (9 - i), '* ' * i)

'''
# Task #15
Користувач робить внесок у розмірі N $ строком на роки під 11.5% річних 
(кожний рік розмір його вкладу збільшується на 11,5%. Ці гроші додаються до суми вкладу, 
і на них наступного року також будуть відсотки). Написати програму , де користувач вводить аргументи a та years, 
і порахувати суму, яка буде на рахунку користувача через роки.
'''
# attachment = float(input('Enter your attachment: '))
# years = int(input('Enter the number of years: '))
# result = 0
# for i in range(years):
#     result += attachment + attachment * (11.5/100)
#     attachment += attachment * (11.5/100)
# print(result)

'''
# Task #16
Користувач запроваджує рік. Визначити він високосний чи ні.
'''
# x = int(input('Enter year: '))
# if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
#     print('Leap yer!')
# else:
#     print('Not Leap.')

'''
# Task #17
Напишіть програму, яка запитує три цілі числа a, b і x і виводить True, якщо x лежить між a і b, інакше - False.
'''
# a, b, x = int(input('Enter a: ')), int(input('Enter b: ')), int(input('Enter x: '))
# if a < b:
#     if a <= x <= b:
#         print('True')
#     else:
#         print('False')
# else:
#     if a >= x >= b:
#         print('True')
#     else:
#         print('False')

'''
# Task #18
Дано чотири дійсні числа: x1, y1, x2, y2. обчисліть відстань між точкою (x1, y1) та (x2, y2). 
Вважайте чотири дійсні числа та виведіть результат роботи цієї функції.
'''
# x1, y1, x2, y2 = int(input('Enter x1: ')), int(input('Enter y1: ')), int(input('Enter x2: ')), int(input('Enter y2: '))
# if x2 > y1:
#     print(x2 - y1)
# elif x1 <= x2 < y1: # Intersection of segments
#     print(0)
# elif x1 > y2:
#     print(x1 - y2)

