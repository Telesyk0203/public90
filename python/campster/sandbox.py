# def convert(m):
#     return m*100
# convert(2)

# def area_of_circle(r):
# 	return r*r*3.14
    
# area_of_circle(30)

# def print_func(string, n=2):
# 	print (string * n)
# 	print()
# print_func('rerer!!!')

# def func1():
#     for i in range(10):
#         print(i)

# def func2():
#     i=100
#     func1()
#     print(i)

# def print_time():
#     print(time_left)

# time_left=30

# print_time()



# n= int(input('Введіть номер'))
# sum=0 

# for num in range(1,n+1,1):
# 	sum=sum+num
# 	print('Сума першого', n,'цифри це:', sum)

# L=[3,4,5]

# L=eval(input('Введіть список, будь ласка:'))
# print('Перший елемент з цього списку', L[0])

# L=[1,2,3]
# print(L)

# L=list(range(101,115))
# print(len(L))

# A=[2,4,6,8]
# B=[1,3,5,7]
# print(A+B)
# C=A+B
# print(C[:5])
# # C=[1,2,3]
# print (C*3)

# L=[2, 4, 6, 8, 1, 3, 5, 7]
# for i in range(len(L)):
#     print(L[i])
# L= [39,3,45,6,7,2,90,101,43,15]
# L.sort()
# print(L) 

# L.append(99)
# print(L)

# L=eval(input('Створіть список, будь ласка :'))
# print(L)
# L.reverse()
# print(L)
# L.insert(2,100)
# L.append(101)
# print(L)
# print(len(L))
# from time import sleep


# L=[[1,2,3],[4,5,6],[7,8,9]]
# for r in range(3):
#     for c in range(3):
#         print(L[r][c],end="")
#     print()

# count=0 
# for r in range(3):
#     for c in range(3):
#         count=count+1
# print(count)

# count=0 
# for r in range(3):
#     for c in range(3):
# 	    if(L[r][c]%2==0):
# 	      count=count+1
# print(count)

# lines =  [line.strip() for line in open('D:\git\public90\python\campster\example.txt')]
# print(lines)

# str='     hello everybody    '
# print (str.strip())
# 'hello everybody'
# s=open('D:\git\public90\python\campster\example.txt').read()
# print(s)
# f= open('D:\git\public90\python\campster\writing.txt', 'a+')
# #print(f)
# print('Hi! EvEryone.', file=f)
# sleep(2)
# print('Sory!!! ', file=f)
# f.close()

# import shutil
# shutil.copy('D:\\git\\public90\\python\\campster\\writing.txt', 'D:\\git\\public90\\python\\campster\\new_writing.txt')

# shutil.move('D:\\git\\public90\\python\\campster\\new_writing.txt', 'D:\\git\\public90\\python\\new_writing_test_example.txt')
# Якщо ми вкажемо не існуючу папку в шляху перемещення файлу то файл кий ми переміщяємо буде переіменований на назву неіснуючої папки , тому треба уважно вводити шлях переміщення файлу  

# Видалення окремого файлу або порожнього каталогу може бути виконано шляхом імпорту модуля ОS, тоді як модуль shutil використовується для видалення папки та всього її вмісту.
# import send2trash
# baconFile= open('D:\\git\\public90\\python\\bacon.txt', 'a')
# baconFile.write('Give PEACE!!!!')
# baconFile.close()
# send2trash.send2trash('D:\\git\\public90\\python\\bacon.txt')

# import zipfile
# newZip = zipfile.ZipFile('D:\\git\\public90\\python\\new.zip', 'w')
# newZip.write('D:\\git\\public90\\python\\new_writing_test_example.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()








# import zipfile,os
# exampleZip=zipfile.ZipFile('D:\\git\\public90\\python\\')
# exampleZip.namelist()
# spamInfo = exampleZip.getinfo('D:\\git\\public90\\python\\new.txt')
# spamInfo.file_size
# spamInfo.compress_size
# exampleZip.close()

# У першому рядку коду ми імпортуємо модуль zipfile, щоб мати змогу працювати з необхідними функціями. Далі ми створюємо exampleZip (який є об'єктом ZipFile) за допомогою функції ZipFile(), яку ми продовжимо використовувати в коді, та яка в каталозі посилається на файл example.zip.

# У об'єкта ZipFile є метод namelist(), який повертає список рядків для всіх файлів та каталогів, що містяться у ZIP файлі. Функція getInfo() повертає інформацію про файл, який міститься у папці ZIP, наприклад, про розмір вихідного файлу та розмір стиснутого файлу. Якщо об'єкт ZipFile представляє собою весь архівний файл, то об'єкт ZipInfo містить корисну інформацію про один файл в архіві.

# import zipfile, os
# os.chdir('D:\\git\\')# куди експортувати файл
# exampleZip = zipfile.ZipFile('D:\\git\\public90\\python\\new.zip') # який файл будемо відкривати
# exampleZip.extractall() #відкриваємо всі що є в архіві
# exampleZip.close()

# b=4
# c=0
# try:
# 	a=b/c
# except ZeroDivisionError:
# 	print('Error!')

# try :
#     a=eval(input('Введіть число:'))
#     print(3/a)
# except NameError:
#     print('Будь ласка , ввeдіть число.')
# except ZeroDivisionError:
#     print('Агов!!!Не можна ділити на 0')

# try:
#     datoteka = open('D:\\git\\public90\\python\\campster\\database.txt', 'a')
#     print("Hi everyone!!", file=datoteka) 
#     datoteka.write("Текст для введення в базу даних!!") 
#     datoteka.close()
# except NameError:
#       print ("Невідома база даних")
# except IOError:
#       print ("Помилка: не вдається записати текст в базу даних", datoteka)
# else:
#       print ("Текст успішно введено в базу даних", datoteka)
# raise Exception('Це повідомлення про помилку.')

# Отже, при відсутності блоків try та except на додачу до команди raise, яка зазвичай викликає винятки, програма просто аварійно завершить роботу та відобразить повідомлення про помилку.

# Часто код, який викликає функцію, а не сама функція, знає, як обробляти винятки. Таким чином, команда raise зазвичай знаходиться всередині функції, а блок try/except – всередині коду, який викликає функцію.

# Простий приклад використання raise:

def chkassert(num):
    assert type(num) == int
    return num**2

chkassert('a')


