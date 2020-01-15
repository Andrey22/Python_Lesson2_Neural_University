'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print ('Task1')
for i in range(5):
    i+=1
    print(i,'00000')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# print ('Task2')
# count=0
# for i in range(10):
#     number = int(input('Введите 1 из 10 цифр'))
#     if number==5:
#         count+=1
# print ('Количество цифр 5 равно', count)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# print ('Task3')
# countnum=0
# for i in range(101):
#     countnum+=i
# print (countnum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print ('Task4')
countnum = 1
for i in range(1,11,1):
    countnum*=i
print (countnum)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print ('Task5')
number1 = int(input('Введите число'))
while number1>0:
    x = number1
    x%=10
    print (x)
    number1//=10

'''
Задача 6
Найти сумму цифр числа.
'''
print ('Task6')
number1 = int(input('Введите число'))
sum=0
while number1>0:
    x = number1
    x%=10
    sum+=x
    number1//=10
print (sum)
'''
Задача 7
Найти произведение цифр числа.
'''
print ('Task7')
number1 = int(input('Введите число'))
multi=1
while number1>0:
    x = number1
    x%=10
    multi*=x
    number1//=10
print (multi)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# print ('Task8')
# number = int(input('Введите число'))
# while number>0:
#     x = number
#     x%=10
#     number //= 10
#     if x == 5:
#         print ('Yes')
#         break
# else:
#     print ('No')
'''
Задача 9
Найти максимальную цифру в числе
'''
print ('Task9')
number = int(input('Введите число'))
max=0
while number>0:
    x = number
    x%=10
    number //= 10
    if x > max:
        max=x
print (max)
'''
Задача 10
Найти количество цифр 5 в числе
'''
print ('Task10')
count=0
number = int(input('Введите число'))
while number>0:
    x = number
    x%=10
    number //= 10
    if x == 5:
        count+=1
print (count)