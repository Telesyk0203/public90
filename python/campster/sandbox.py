
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
L=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(3):
    for c in range(3):
        print(L[r][c],end="")
    print()

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
s=open('D:\git\public90\python\campster\example.txt').read()
print(s)