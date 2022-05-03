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

# def chkassert(num):
#     assert type(num) == int
#     return num**2

# chkassert('a')

# class Primer:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         return self.a + self.b

# e = Primer(40,6)
# print(e.add())

# class Example:
#     def __init__(self, a,b):
#         self.a=a
#         self.b=b
    
#     def add(self):
#         return self.a+self.b

# e= Example (100,6)
# print(e.add())
        
# class Parent:
#     def __init__(self, a) -> None:
#         self.a=a
#     def method1(self):
#         print(self.a*2)
#     def method1(self):
#         print(self.a+'!!!!')

# class Parent:
#     def __init__(self, a):
#         self.a=a
#     def method1(self):
#         print(self.a*2)
#     def method2(self):
#         print(self.a+'!!!!')

# class Child(Parent):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def method1(self):
#         print(self.a*7)
#     def method3(self):
#         print(self.a + self.b)

# p=Parent('hi')
# c=Child('hi','bye')

# print('Parent method1:',p.method1())
# print('Parent method2:', p.method2())
# print()
# print('Child method1', c.method1())
# print('Child method2', c.method2())
# print('Child method3', c.method3())

# class Shark():
#     def swim(self):
#         print('The shark is swimming.')
    
#     def swim_backwards(self):
#         print('The shark cannot swim backwards, but can sink backwards.')

#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage")

# class Clownfish():
#     def swim(self):
#         print("The clownfish is swimming.")
    
#     def swim_backwards(self):
#         print("The clownfish can swim backwards.")

#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone.")

# sammy=Shark()
# sammy.skeleton()

# casey=Clownfish()
# casey.skeleton()
# from tkinter import *
# root = Tk()
# mainloop()
##################################
# from tkinter import*
# def change():
#    entry=int(entry.get()) 
#    output_lablel.configure(text='Дохід від  вбитих москалів:{:1f} $'.format(entry))
#    output_lablel=entry*100
#    entry.delete(0,END)

# root = Tk()
# message_lable=Label(text='Введіть кількість убитих москалів ', font=('Vernada',16))
# output_lablel=Label(font=('Vernada',22))
# entry=Entry(font=('Vernada',22), width=4)
# calc_button=Button(text='Натиснути', font=('Vernada', 18), command=change)
# message_lable.grid(row=0,column=0)
# entry.grid(row=0,column=1)
# calc_button.grid(row=0,column=2)
# output_lablel.grid(row=1, column=0,columnspan=3)
# mainloop()

################################
# marks = {'Physics':67, 'Maths':87}

# print(marks.get('Physics'))

#########################Поле введення###################
# За допомогою поля введення GUI допускає введення тексту. Наступний приклад демонструє, як створюється поле введення:
# import string


# entry = Entry()
# entry.grid(row=0, column=0)

# # Ми використовуємо grid для розміщення поля введення та інших елементів на екрані.

# # Щоб отримати текст з поля введення, ми використовуємо функцію "get". За замовчуванням ця функція повертає рядок, і якщо нам потрібні числові дані, ми можемо скористатися функцією eval або int, float. Тепер наведемо простий приклад отримання даних з поля введення, яке ми назвали entry:

# string_value = entry.get()
# num_value = eval(entry.get())

# # Якщо нам потрібно видалити текст з цього поля, ми можемо зробити це в такий спосіб:
# entry.delete(0,END)

# # Для введення тексту в поле ми використовуємо:
# entry.insert(0, 'hello')
# #############################Зображення######################
# # Мітки, кнопки та інші віджети можуть відображати зображення замість тексту. Використання зображень вимагає трохи підготовки. Спочатку нам потрібно створити об’єкт PhotoImage та дати йому ім’я:

# cheetah_image = PhotoImage(file='cheetahs.gif')
# # Тепер ми відобразимо зображення у віджетах:

# label = Label(image=cheetah_image)
# button = Button(image=cheetah_image, command=cheetah_callback())
#                # Одним із обмежень Tkinter є те, що можна використовувати лише зображення GIF. Якщо Ви хочете використовувати деякі інші типи файлів, одним із рішень є використання бібліотеки Python Imaging Library, за допомогою якої Ви можете конвертувати інші формати зображень у GIF.
 
score = [3,25,7.01,85.3,95.20,2,6,77,9]
score.sort()
print(score)


