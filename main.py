
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
print ('Task2')
count=0
x=0
number= int(input('Введите 10цифр'))
for i in range(10):
    number%=10
    if number==5:
        count+=1
print ('Количество цифр 5 равно',count)