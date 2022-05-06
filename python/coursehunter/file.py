from asyncio import format_helpers
from errno import ERANGE
from operator import le, ne
from posixpath import split
from re import T, X
from statistics import median_low
from time import sleep
from tkinter import E
from turtle import numinput, st


print ('Hello  world')

dict
{'alex':'123', 'anna':'564'}

bool
True
False

set
{ }
x='None'
print(type(x))
print(x)


import math
a=15
b= 11
c= 9 

p = (a+b+c)/2

s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)

x=int(True)
print(x)
#1 цифрове значення True Правда
y= int(False)
print(y)
# 0- цифрове значення False Брехня

a= [] # пустий список в булевому значення означає False
print(bool(a))
# False

b=[1,2,4] # заповнений список буде мати булеве значення True
print(bool(b))
# True

print(1<2 and 2<3)# True всі умови мають бути виконані при застосуванні оператора "and"
print(1<2 or 2>3) #True одна із умов має бути виконана при застосуванні оператора "or"

'''
Для роботи з рядками та лапки 
'''
text= str('Слава Україні !!!')
print(type(text))
print(text)
print(text[0]+text[4]) # Вивести перший символ та четвертий разом
print(text[-1]+text[0]*2) # Вивести останній останній символ рядка з першим подвоєним індексом 0(нуль) разом 
print(text[:6]*3) # Вивести перші шість символів рядка три рази підряд разом
print(text[::3]) # Вивести всі символи з кроком (3) три разом 
 
'''
Функції рядків
'''
x= 'some long and awesome TEXT'
print(len(x)) #  Кількість символів у рядку
print(x[len(x)-1]) # Вивести останній символ з довжини рядка
print(x[len(x)-4:len(x)])  #Вивести останні 4 елементи від довжини рядка
print(x.count('o')) #Вивести кількість букви "о"
print(x.find('o')) # Знайти перший індекс букви "о"
print(x.find('o',3,7)) # Знайти номер індексу букви "о" з 3 по 7 індекс
print(x.find('o',7)) # Знайти номер індексу букви "о" з 7 індексу і до кінця рядка
print(x.find('and')) # Знайти номер індексу з якого починається  фраза "and"
print(x.find('abc')) # Якщо фраза не знаходиться у виводі буду -1

print(x.capitalize()) # Вивести рядок з великої літери

print(x.upper()) # Вивести увесь рядок у верхньому регістрі

print(x.lower()) # Вивести увесь рядок у нижньому регістрі

print('Old text: '+x)
upper_cased=x.upper()
lower_cased=x.lower()
print(upper_cased.isupper()) # Перевірочна функція що всі елементи знаходяться у вехньому регістрі результат "True"

print(lower_cased.islower()) # Перевірочна функція що всі елементи знаходяться у нижньому регістрі результат "True" 

print(x.isupper()) #Якщо помилки під час превірки то виводиться занчення "False"

print('xxx777'.isalnum()) # Перевірка чи рядок складається ТІЛЬКИ з літер та чисел . Відповідь "True"

print('xxx777!'.isalnum()) # Перевірка чи рядок складається ТІЛЬКИ з літер та чисел . Відповідь "False"
print('xxx777'.isalpha()) # Перевірка чи рядок складається ТІЛЬКИ з  чисел . Відповідь "False"
print('xxx'.isalpha()) # Перевірка чи рядок складається ТІЛЬКИ з  чисел . Відповідь "True"

x=str('hello') # Змінна рядок "hello"
print(type(x)) # Перевірка типу змінної
print(x.startswith('he')) # Перевірка чи рядок починається на "he" Відповідь "True" 
print(x.endswith('lo')) # Перевірка чи рядок закінчується на "lo" Відповідь "True"

split=x.split('l') # Змінна зі знаком розділювачем "l"
print(type(split)) # Тип змінної "str"
print(x.split('l')) # Вивести результат функції "split"

some_data= '14;45;65;76;87;98;901' # Змінна рядок 
print(some_data.split(';'))# Розділюємо елементи рядка задопомогою розділювача ";"


'''
Форматування рядків
'''
x='10'
y='cold'
forecaste= 'Weather: temperature +{} and it\'s {}'.format(x,y) # 
print(forecaste) # Форматування рядка задопомогою змінних "х" та "у"
wrong_forecaste= 'Weather: temperature +{1} and it\'s {0}'.format(x,y)
# Форматування рядка задопомогою змінних "х" та "у"
print(wrong_forecaste)
anotherFormat_forecaste=f'Another_Weather: temperature +{x} and it\'s {y}'#Форматування рядка задопомогою змінних "х" та "у" КОРОТКИЙ ЗАПИС
print(anotherFormat_forecaste)
'''
Списки , типи даних "list"
'''
new_list=[1,2,3,4] #Елементи списку
mix_list=[12, 3.14, 184, 'text'] # Змішані типи даних в списку
print(len(new_list))
print(mix_list[-1]) # Вивести останній елемент списку
print(mix_list[1])# Вивести другий елемент списку
print(mix_list[2:]) # Зріз від другого індексу
female_name=['anna', 'iryna', 'nataliya', 'oksana']
male_name= ['vlad', 'roman', 'alex', 'taras'] 
print(female_name + male_name)
female_name[0]='irukha' ## Заміна елемента на індексу "0" в списку female_name
male_name[0]='vladusyk'# Заміна елемента на індексу "0" в списку male_name
print(female_name + male_name)
female_name.append('anna') # Додаваня елементу в кінець списку female_name
male_name.append('vlad_junior')# Додавання елемету в кінець списку male_name
female_name.insert(3,'valentyna') #Додаваня елементу на третій "3" індекс списку female_name
male_name.insert(3,'volodymyr')#Додаваня елементу на третій "3" індекс списку male_name
print(female_name)
print(male_name)
print(female_name.index('oksana')) # Вивести номер індексу "оксана" зі списку  female_name
print(male_name.index('roman'))# Вивести номер індексу "роман" зі списку  male_name
male_name.index('taras', 0, 9) # Знайти індекс елементу "тарас" в діапазоні з "0" по "3" індекси 

pop_del= female_name.pop() # Виделення останнього елементу списку (.pop()  по замовчуванню)
print(pop_del) # Вивести видалений елемент списку 
print(female_name) 
male_name.pop(3) # Видалити елемент списку на третьому "3" індексі
print(male_name.pop(3))
print(male_name)
female_name.clear() #Видалити всі елементи списку
print(female_name)


list_number=['33','22','11','44']
print(list_number)
list_number.sort() # Сортування елементів списку
print(list_number)
list_number.sort(reverse=True)# Сортування елементів списку в зворотному порядку . Аргумент reverse не змінює порядок просто виводить інформацію  
print(list_number)
list_alpha=['rwerwre', 'ewrwe', 'ofl', 'abab','v', 'bb', ]
print(list_alpha)
list_alpha.sort() #Сортування по списку алфавіту
print(list_alpha)

'''
Словник , тип даних  dict
'''
# Тип даних "dict" це тип ключ:значення , тобто привведенні ключа ми можемо швидко занйти значення 
# У словнику не можу бути два однакових ключа 

students={
    'taras':300,
    'vitaliy':258,
    'oleg':159,

}
print(students)
print(students['taras'])#Вивід значення ключа "тарас" відповідь "300"
print(students.get('oleg'))#Вивід значення ключа "oleg" відповідь "159"

students['ivan']= 266 # Додавання нового ключ :значення в dict 
print(students)
students['ivan']= 401 # Зміна значення в ключі "ivan"
print(students)
students.setdefault('max') # Задаєм ключ "max" без значення
print(students)
students.pop('oleg') # Видалення ключа "oleg" , значення також потім удаляється 
print(students)
print(students.keys()) # Вивести тільки ключі dict "students"
print(type(students.keys())) # Вивести тип даних students.keys()
key_list_students= list(students.keys()) # Створити змінну яка буде мати тип даних  "list"(список) словника "students"
print(type (key_list_students))
print(key_list_students)

print(students.values()) # Вивести значення типу даних словник "students "

print(type(students.values())) # Вивести тип даних значення в словнику "students"

print('taras' in students) # Запит на виведення чи є ключ "" у словнику "students"

print ('alex' not in students) # Запит чи відсутній ключ "alex" у словинику "students"

'''
Кортежи або tuple тип даних 
'''
#Кортежи це не змінний тип даних , дуже схожий на тип даних "list"
a=(12,'a', True) # Форма запису кортежа (tuple)
print(type(a)) # Перевірка типу даних змінної "а"
print(a)
print(a[1]) #Вивести елемент кортежа під індексом "1"
b=list(a) # Зміна типу даних "tuple" на тип даних "list"
print(type(b)) 
c=tuple(b) #Зміна типу даних "list" на тип даних "tuple"

'''
Множина тип даних set
'''
# Множина тип даних set є  набором унікальних елементів даних тобто не повторюється 
first_set  =  {'Alex', 'Taras', 'Oleg', 'Alex'} # Тип даних типу "set" або множина 
print(type(first_set))
print(first_set) # Виводить тільки унікальні послоідовності тобото "Alex" буде виведений 1 раз а не два .
second_set={'Antony', 'Sara', 'Alex', 'John'}
third_set= first_set.union(second_set) # Об'єднання двох унікальних множин в одну  
print(third_set)
fourth_set=first_set.intersection(second_set) # Виводить однакові елементи даних які є в першій і в другій множині (перехрестя)
print(fourth_set)
fifth_set=first_set.difference(second_set) # Виділяє(виводить) з first_set різницю між першою і другою множиною  
print(fifth_set) 
print(first_set-second_set)#  Різниця між першою і другою множиною 

set1={1,2,3}
set2={1,2,3,4,5}
print(set1.issubset(set2)) # Перевіряє чи перша множина є підмножиною другої множини 
print(set2.issuperset(set1)) # Перевіряє чи для другої множини перша множина є підмножиною 
# Індексування в тип даних set  не підтримується !!!!!!!!!!

'''
Логічні оператори : if (якщо) , elif(або якщо ), else(в решті випадках)

'''
# Призначені для розгалудження програми

print('Введіть  кількість балів курсанта: ')
x=int(input())
if 90<= x <100: # Якщо ця умова виконується
    print('Це оцінка : Відмінно') 
elif 90>x>=70 : # Або якщо ця умова виконується
    print('Це оцінка : Добре')
elif 70>x>=50 : # Або якщо ця умова виконується
    print('Це оцінка : Задовільно')
elif 50>x>=0 :# Або якщо ця умова виконується
    print('Це оцінка : Незадовільно')
else : # Усі інші варіанти
    print('Введіть правильні дані ') 

'''
Цикл "for"
'''
# Цикли дозволють виконувати циклічні операції що повторюються 
# Цикл for  є основним циклом  для роботи с колекціями 
#  Конструкція for циклу :
                    # for x in iterable:
                        # дія з x 
            # дe x локальна змінна рівна елементу послідовності itetable
numbers= [1,2,3,4,5] # Список 
for j in numbers:# Цикл (виконуємо) ітеруємо  локальну змінну j  в списку numbers
    print(j)# Виводимо на екран перелічені елементи списку через змінну j
    print(j**2) # Вмвести в квадрат елементів списку
# Функція range() створює ітерабальний (послідовний) діапазон
numbers=range(1,33)# Створюємо список діапазаном від 1 до 32(включно)
print(numbers)
new_list=[]# створюємо новий пустий список 
for i in numbers:
    new_list.append(i)# Додаєм в новий пустий список кожний елемент по черзі зі списку numbers 
print(new_list)

for i in range(1,16):# Цикл в діапазоні списка від 1 до 15 
    sleep(1)
    if i % 2 == 0:# Якщо елемент списку поділити на 2 і залишок буде рівний нулю (0)
        print(f'{i} це парне число ') #  То виводть 
    else : # Всі інші варіанти 
        print(f'{i} це не парне число')

# Використвоуємо функції типів ітерабельних даних для маніпуляцій з об'єктами цих типів.
#  Використовуємо оперетори if , elif, else для розгалудження логіки в циклі 
#  Функція enumerate() додає лічильник до кожного об'єкту , використовуєм у подальших розрахунках 
# 
# Використовуєм tuple(кортеж)-unpacking для розпаковки tuple на призначення (timecode 06:20) 
#  Для розпаковки словника Dict використовуєм  tuple(кортеж)-unpacking так як результат циклу for при проходженні словника tuple(timecode 08:20)
# Для читання словника використвуєм функцію items()
# Для читання тільки значень словника використвовуєм функцію values()




