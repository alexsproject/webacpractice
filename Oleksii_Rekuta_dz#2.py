"""
# 1. Дано два списки чисел. Знайдіть усі числа, які входять як до першого, так і до другого
# списку і виведіть їх у порядку зростання.

import random

a = [random.randint(0, 10) for i in range(random.randint(1, 10))]
b = [random.randint(0, 10) for j in range(random.randint(1, 10))]
print(a)
print(b)
res = list(set(a).intersection(set(b)))
res.sort()
print(res)

# --------------------------- #
# 2. Напишіть скрипт Python для сортування (за зростанням та зменшенням) словника за значенням.

students = {'Igor': 'Ivanov',
            'Marina': 'Andreeva',
            'Alex': 'Makarov',
            'Eugenia': 'Stepanova'}
# sort by ascending
ascending = students.items()
ascending = list(ascending)
ascending.sort()

# sort by decreasing
decreasing = students.items()
decreasing = list(decreasing)
decreasing.sort(reverse=True)

print(dict(ascending))
print(dict(decreasing))

# --------------------------- #
# 3. Напишіть програму на Python для суми всіх елементів словника.
string_maps = {1: 2,
             3: 4,
             5: 6}
keys = string_maps.keys()
values = string_maps.values()

# sum of keys
sum_keys = 0
for i in keys:
    sum_keys += i

# sum of values
sum_values = 0
for j in values:
    sum_values += j

print(sum_keys + sum_values)

# --------------------------- #
# 4. Напишіть перевірку, чи є рядок паліндромом. Паліндром - це слово або фраза,
які однаково читаються зліва направо та праворуч наліво.

some_string = input('Enter some world: ')
if some_string == some_string[::-1]:
    print("It's Palindrome!")
else:
    print("It's Not palindrome :(")

# --------------------------- #
# 5. Користувач вводить кількість секунд.Зробіть так, щоб число секунд відображалось
# у вигляді дні:години:хвилини:секунди.

sec = int(input('Count of seconds: '))
day = sec // 86400
hours = (sec % 86400) // 3600
minutes = ((sec % 86400) % 3600) // 60
second = ((sec % 86400) % 3600) % 60
print("It's: ", day, ':', hours, ':', minutes, ':', second, sep='')

# --------------------------- #
# 6. Ви приймаєте від користувача послідовність чисел, розділених комою.
Складіть список і кортеж із цими числами.

num = input('Enter number separate by comma: ')
some_list = num.split(',')
print(some_list)
print(tuple(some_list))

# --------------------------- #
# 7. При заданій цілій кількості n порахуйте n + nn + nnn. (n=5 => 5+55+555)

num = int(input('Enter num: '))
str_num = str(num)
num2 = str_num + str_num
num3 = str_num + str_num + str_num
res = num + int(num2) + int(num3)
print('Result:', res)

# --------------------------- #
# 8. Напишіть програму, яка приймає два списки та виводить усі елементи першого, яких немає у другому.

first_input = input('Enter elements separate by comma: ')
second_input = input('Enter elements separate by comma: ')
first_list = set(first_input.split(','))
second_list = set(second_input.split(','))
first_list.difference_update(second_list)
print(first_list)

# --------------------------- #
# 9. Знайдіть з рандомного списку всі числа які діляться на 15. (В один рядок)

import random

a = [i for i in [random.randint(-20, 40) for j in range(20)] if i % 15 == 0]
print(a)

# --------------------------- #
# 10. Юзер вводить текст. Вам потрібно зробити словник в якому ключами є
слова того тексту , а значеннями відповідно кіл-ть тих слів.

s = input('Enter your string: ').split(' ')
string_maps = {}
for i in s:
    string_maps[i] = s.count(i)

print(string_maps)

# --------------------------- #
# 11. Перевірити, чи є в послідовності дублікати

s = input('Enter some string: ').split(' ')
for char in s:
    if s.count(char) > 1:
        print('Yes')
        break
else:
    print('No!')

# --------------------------- #
# 12. Автомобіль подолав відстань s км через населений пункт за t хв. Визначити,
чи не порушив водій правил дорожнього руху, якщо швидкість автомобіля при цьому не повинна перевищувати 60 км/год.

s = int(input('Enter distance >>> '))
t = int(input('Enter time in min >>> '))
v = s / t
if v > 1:
    print('Stop! You have violated!')
else:
    print('All ok.')
print(v)

# --------------------------- #
# 13. Порахувати кіл-ть додатніх чисел в списку (в один рядок)

import random

nums = [random.randint(-20, 20) for i in range(15)]
count = 0
for i in nums:
    if i > 0:
        count += 1
print(nums)
print('Count of positive num -', count)

# --------------------------- #
# 14. Напишіть програму, яка запропонує користувачеві ввести десяткове число у межах від 1 до 10.
Програма повинна вивести версію римського числа. Програма має враховувати ситуацію,
якщо введене число є за межами діапазону від 1 до 10.

n = int(input('Please enter number from 1 to 10 >>> '))
if n > 10 or n < 1:
    print('Error! Should be 1 to 10')
elif n < 4:
    print('I' * n, sep='')
elif n == 5:
    print('V')
elif n < 9:
    print('V' + (n-5) * 'I', sep='')
elif n == 9:
    print('IX')
elif n == 10:
    print('X')

# --------------------------- #
# 15. Перевести число, введене користувачем, у байти або кілобайти в залежності від його вибору.
# Користувач вводить значення у мегабайтах і, відповідно, вводить напрямок переведення:
B (у байти) або KB (у кілобайти).

mb = int(input('Enter count of Mb >>> '))
choice = input('Get Bytes (enter "B") or Kbytes (enter "KB")? >>> ')
if choice not in ['B', 'KB']:
    print('Error! Enter "B" or "KB".')
elif choice == 'B':
    print("It's -", mb * 1000000, 'B')
elif choice == 'KB':
    print("It's -", mb * 1000, 'KB')

# --------------------------- #
# 16. Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0.
Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено три пари вхідних значень
коефіцієнтів, а у вихідних даних - відповідні повідомлення про кількість коренів або їх відсутність.

import math

a, b, c = float(input('Enter a >>> ')), float(input('Enter b >>> ')), float(input('Enter c >>> '))
d = b**2 - 4*a*c
print(d)
print(math.sqrt(16))
x1 = 1
x2 = 1
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
elif d == 0:
    x1, x2 = -(b/(2*a))
elif d < 0:
    x1 = 'відсутній'
    x2 = 'відсутній'

print('X1 =', x1, '\nX2 =', x2)

# --------------------------- #
# 17. Дано ціле число k (1 ≤ k ≤ 365). Визначити, яким буде k-й день року: вихідним (субота або неділя)
або робочим, якщо 1 січня - понеділок.

k = int(input('Enter numb of day >>> '))
if k % 7 == 0:
    print("It's weekend - Sunday")
elif (k < 7 and k % 6 == 0) or (k > 7 and (k - 6) % 7 == 0):
    print("It's weekend - Saturday")
elif (k < 7 and k % 5 == 0) or (k > 7 and (k - 5) % 7 == 0):
    print("It's work day - Friday")
elif (k < 7 and k % 4 == 0) or (k > 7 and (k - 4) % 7 == 0):
    print("It's work day - Thursday")
elif (k < 7 and k % 3 == 0) or (k > 7 and (k - 3) % 7 == 0):
    print("It's work day - Wednesday")
elif (k < 7 and k % 2 == 0) or (k > 7 and (k - 2) % 7 == 0):
    print("It's work day - Tuesday")
elif (k < 7 and k % 1 == 0) or (k > 7 and (k - 1) % 7 == 0):
    print("It's work day - Monday")

# --------------------------- #
# 18. Визначити, чи увійде в конверт з внутрішніми розмірами a і b мм прямокутна листівка з розмірами с і d мм.
Для розміщення листівки в конверті необхідний проміжок в 1 мм з кожної сторони. Значення сторін листівки
і конверту - цілі числа.

a, b = int(input('Enter envelope width >>> ')), int(input('Enter envelope length >>> '))
c, d = int(input('Enter letter width >>> ')), int(input('Enter letter length >>> '))
if a > c and b > d:
    print('Yes! You can send the letter.')
else:
    print('Sorry! Your letter is too big.')

# --------------------------- #
# 19. Напишіть функцію для отримання всіх можливих двозначних комбінації літер із рядка цифр (від 1 до 9).
Для розв’язування задачі використайте словник:
string_maps = {
      '1': 'abc',
      '2': 'def',
      '3': 'ghi',
      '4': 'jkl',
      '5': 'mno',
      '6': 'pqrs',
      '7': 'tuv',
      '8': 'wxy',
      '9': 'z'}.
#       Вхідні дані - 12
#
#       Вихідні
#       ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
#

string_maps = {
      '1': 'abc',
      '2': 'def',
      '3': 'ghi',
      '4': 'jkl',
      '5': 'mno',
      '6': 'pqrs',
      '7': 'tuv',
      '8': 'wxy',
      '9': 'z'}


def double_combinations(some_dict):
    user_keys1, user_keys2 = input('First key - '), input('Second key - ')
    res_lst = []
    for i in some_dict.get(user_keys1):
        for j in some_dict.get(user_keys2):
            res_lst.append(i + j)
    return res_lst

x = double_combinations(string_maps)
print(x)


# --------------------------- #
# 20. Напишіть функцію для перевірки, чи є рядок «панграмою» чи ні. Примітка.
# Панграма - фраза, вислів або текст в якому присутні всі літери абетки принаймні по одному разу.
Наприклад: «How vexingly quick daft zebras jump» (30 літер), «The five boxing wizards jump quickly» (31 літера),
 «Cwm fjord bank glyphs vext quiz» (26 літер), «The quick brown fox jumps over the lazy dog» (35 літер).

some_str = input('Enter your text >>> ').upper()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
lst_from_str = []
for i in some_str:
    if i in alphabet:
        lst_from_str.append(i)

lst_from_str.sort()

if lst_from_str == alphabet:
    print('Yes')
else:
    print('No')

# --------------------------- #
# 21. дано кількість голів n та лап m серед курчат та кроликів на фермі. Скільки курчат і кроликів на фермі?

n, m = int(input('Enter count of heads >>> ')), int(input('Enter count of legs >>> '))
rabbit = m / 2 - n
chicken = 2 * n - m / 2

print(chicken, '- count of chicken.\n', rabbit, '- count of rabbit')

# --------------------------- #
# 22. Дано натуральне число n (1 ≤ n ≤ 9999), що визначає вартість товару в копійках.
Подайте вартість у гривнях і копійках. Якщо у результаті виходить 0 копійок,
то замість цього значення необхідно записати порожній рядок.

n = int(input('Enter count of pennies >>> '))
hrn = n // 100
pennies = n % 100
if pennies == 0:
    print("It's", hrn, "UAH")
else:
    print("It's", hrn, "UAH", pennies, "pennies.")

# --------------------------- #
# 23. Дано трицифрове ціле число. Визначити суму першої і останньої цифр числа і порівняти її із
значенням другої цифри числа. Відповідно вивести повідомлення: >, < і =.

n = input('Enter num: ')
separate_n = []
for i in n:
    separate_n.append(i)

sum_frst_lst = int(separate_n[0]) + int(separate_n[-1])
middle_num = int(separate_n[1])
if sum_frst_lst > middle_num:
    print(sum_frst_lst, '>', middle_num)
elif sum_frst_lst < middle_num:
    print(sum_frst_lst, '<', middle_num)
elif sum_frst_lst == middle_num:
    print(sum_frst_lst, '=', middle_num)

# --------------------------- #
# 24. Напишіть програму, у яку вводяться трицифрове ціле число і цифра.
Необхідно визначити, чи входить у число введена цифра.

n1 = input('Enter first num >>> ')
n2 = input('Enter second num >>> ')
if n2 in n1:
    print('Yes!', n2, 'in', n1)
else:
    print('No :(')

# --------------------------- #
# 25. Дано трицифрове ціле число. Визначити кількість однакових цифр у записі числа і вивести значення цієї кількості.

n = input('Enter num: ')
separate_n = []
count = 0
for i in n:
    separate_n.append(i)
    if separate_n.count(i) > 1:
        count = separate_n.count(i)

print('Count of repeat', count)

# --------------------------- #
# 26. Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число. (2358 -> *35*)

n = input('Enter num: ')
separate_n = []
for i in n:
    if int(i) % 2 == 0:
        separate_n.append('*')
    else:
        separate_n.append(i)

print(separate_n[0] + separate_n[1] + separate_n[2] + separate_n[3], sep='')

# --------------------------- #
# 27. Дано натуральне число n (n ≤ 9999). З’ясувати,
чи різні усі чотири цифри цього числа (з урахуванням чотирьох цифр). Наприклад,
в числі 5623 усі цифри різні, в числі 0012 - ні.

n = input('Enter num: ')
separate_n = []
for i in n:
    separate_n.append(i)
    if separate_n.count(i) > 1:
        print('No! Number', i, 'repeated')
        break

print('Yes! All number are different.')

# --------------------------- #
# 28. Напишіть програму, у якій до введеного числа додаються написи: «гривень» (hryven),
«гривня» (hryvnia), «гривні» (hryvni), згідно з правилами українського правопису.
#     10001 hryvnia
#     516 hryven
#     2022 hryvni

n = int(input('Enter num: '))
end_n = n % 10
end_n = str(end_n)
if end_n in '056789':
    print(n, 'hryven')
elif end_n in '1':
    print(n, 'hryvnia')
elif end_n in '234':
    print(n, 'hryvni')

# --------------------------- #
# 29. Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n,
з якої слід починати відлік.
#     Вхідні дані: 5
#     Вихідні дані:
#     5
#     4
#     3
#     2
#     1
#     Start!

import time
n = int(input('Enter sec >>> '))
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print('Start!')

# --------------------------- #
# 30. Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку
# n, m (Створити цю строку в один рядок , якщо то можливе)

n, m = int(input('Enter number >>> ')), int(input('Enter count of repeat >>> '))
print(str(n) * m)

# --------------------------- #
# 31. Є список будь-яких чисел. Зробити словник в якому будуть два ключі "+" і "-" ,
значенням ключа "+" - сума всіх додатніх елементів , "-" - від'ємних

import random
some_list = [random.randint(-20, 20) for i in range(10)]
print(some_list)
res_dict = {}
positive = 0
negative = 0
for i in some_list:
    if i >= 0:
        positive += i
        res_dict['+'] = positive
    elif i < 0:
        negative += i
        res_dict['-'] = negative

print(res_dict)

# --------------------------- #
# 32. Напишіть програму для створення таблиці множення (від 1 до 10) для введеного цілого числа n.
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

n = int(input('Enter num >>> '))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)
"""
