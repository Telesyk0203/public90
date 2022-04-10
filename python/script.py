# PYTHON BASICS
#1. Creating Variables
# To create a variable(змінна), we need to give "name". Variable names need to be single words and ,therefore(внасідок цього),have no spaces.
city
#If we want a variable name with multiple words, we use `snake case`. Snake case means using "_" to connect the additional words.
home_city
#To help us understand what's inside a varіable we pick descriptive(описуючі назви) names.
# After creating and naming variable, we use the "=" sign(знак) to store a value(значення) inside it, like 
city="Poltava"
# The values we have been storing, like "Poltava" are `string`(рядок).Strings are words in double quotes.
"Ukraine"
# Strings can contain all sorts  of letters and symbols, including spaces, like
"Winter is coming!!!"
# With the spacial instruction "print()", we tell the computer to display a value in area called the `console`,also known as the shell.
print("We will win !!!")
# We can use "print()" to display variables like `greeting` too.
greeting="Hi everyone!!!"
print(greeting)
#________________________________________________________________________________
#2.Using Variables
# Variables are called variables because the values they store  can change. We can update `status` by using "=" and giving it new value. 
# We can update variables as often as we want. 
status = "Reading"
status = "Sleeping"
print(status)
# We can also give variables the values of other variables. Here , we can give the `new_status` variable the value of `default_option`
default_option= "upload"
new_status="download"

new_status=default_option
print(new_status)
# When we update a variable, it forgets its previous value. 
# We call adding string values(рядкові значення) an `expression`(вираз) as it creates asingle value. One string displays when we add "55" inside "print()"
print("Followers:"+"55")

from typing import Counter

name="THROLL"
greeting=name
print("3,2,1")
print("GO!!!!")
print("Taras Strikha!!!!")
print (greeting)
followes= "999"
print("Players of the HORDE:"+ followes)
Alians="Alians suck hord's dicks :"+"1000"
print(Alians)
print("You killed:")
number_of_kills=40
print(number_of_kills+1)
killed_dd= 24
killed_rdd= 16
total=(killed_rdd+killed_dd)
print("Total kills:")
print(total)
correct=True
print(correct)
status= False
print( not status)
orc=True
human=not orc
print(human) 
print(10==10)
print(9==10)
print( not killed_rdd==10)
print(10!=10)
result= 1!=2
print(result)
one= 1
two= 2
print(one == two)
print(one != two)

id_1="#4"
avarage_grade_1="A"
test_score_1=90
id_2="#5"
avarage_grade_2="A"
test_score_2=70
no_duplicates=id_1!=id_2
print("No duplicate enteries:")
print(no_duplicates)
same_average=avarage_grade_1==avarage_grade_2
print("Same average grade:")
print(same_average)
higher_score=test_score_1>test_score_2
print("id_1 has a higher score: ")
print(higher_score)

if True:
    print("Lok tar'o'gar!!!!!!!!")

greet= True
if greet:
    print("Асетавалена!!!!")
is_charged=False
if is_charged:
    print("Charged!")
print("Low battery!!! Alarm!!!")

answer="Taras"
if answer=="Taras":
    print(answer +" is correct!!!")

if answer!="military":
    print(answer+" is wrong!")
age=65
if age>=55:
    print("Discount applied!!!")

score=51
pass_grade=score>50
if pass_grade:
    print(pass_grade)
song="Король і шут!!!"
relay_times=365
if relay_times >=300:
    print("Моя улюблена група на цьому тижні:")
    print(song)

today="Sunday"
if today !="Saturday":
    print("Set alarm at 8:00")

availeble=False
if availeble:
    print("Yes it's done")
else :
    print("No no no !!!")

number=99
if number==1:
    print("It's one")
else:
    print("It's not one")

hour=5
if hour<12:
    print("good morning!!!")
elif hour<17:
    print("Good afternoon!!!")
else:
    print("good night!!!")

#Programs repaet the same lines of code over and again to build all sorts of things like the repeated elements in the app
# One way to repaet lines of code is to  write them over and over again, but it takes a really long time if we want to create larger programs.
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")
#  To build larger programs and websites, we repeat lines of code using a while loop
# while True: 
#                 # print("and again")
# Skip the code block of the "while" loop by setting the condition to False
while False:
                print("Skip me !")
# The loop runs its entire code block because "keep_going" is True at first, but doesn't run again "keep_going" to False
keep_going= True
while keep_going==True:
                print("and again")
                keep_going= False
                print("one more time")     
#Controlling While Loops
#Inside the block, we make the condition return "false" and stop the loop by incrementing the counter variable. Try it whith "counter +=1"
counter=32
while counter <= 44 :
                print(counter)
                counter+=1       
#Like this program repeating statemants to display The Amarican Flag.
first_counter=0
while first_counter<5:
                print("**********-------------------")
                first_counter+=1
second_counter=0
while second_counter <4:
                print("-----------------------------")
                second_counter+=1  
#In "for" loop we can specify how many times we would like our loop to run with the "range()" statement
for i in range(5):
                print("Happy Birthday!!!!")
# Adding a number like "6" inside "range()" means it'll loop overthe block 6 times, from 0 to 5 
for i in range(6):
                print(i)

#The variable before "in", in this case,"i",is the counter variable. It counts what repetition of the loop we're currently on.
for i in range(3):
                print(i)
                print("For loops are great!")
#We'll piece together different parts of a link to  give users a 50 % discount when signing up whith the link. 
base="www.homeflix.com"
coupon="signup/coupon"
discount=50
amount=4

for num in range(amount):
                print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")
#ORGANIZING DATA
# _________________________
# 1.Grouping Data in  Lists 
#
# Rather than creating a variable for each new piece of data, we can collect related data inside a "list" using "[" and  "]"
todo=["Read", "Workout", "Code"]
print(todo)
#_____________________________
#2. Changing Data in Lists
#
# Let's dig depper into maniging lists and how to update the data inside them, like how temperature data might change throughout the day
# Lists can store any piece of data, be it string(рядок), boolean(логічне значення), float(число з комою) or integer(ціле число) like 17
# Every element in a list has a numbered position called index. 
#                                                     [ _ , _ , _ , _ ] 
#                                                       0   1   2   3
#                                                           INDEX
# To access element 20, code the list name temparatures followed by the INDEX of the element between square brackets [1]
temparatures = [17, 20, 26, 24]
print (temparatures [1])
# To change the third temperature value in the list, access it through temparatures [2], then use = to assign it a new value like 25.
# Despite (недивлячись на те що ) having four elements in the list, we access the LAST INDEX by using 3 here , since (починаючи, беручи) the counting starts at zero. 
temparatures = [17, 20, 26, 24]
temparatures[2]=25
print (temparatures)
#__________________
# 3. Updating Lists
# 
# Lets learn how to add and remove values in a list . Like in this app, which uses a list to manage user's score data. 
# To add the value 25  to a list ,  we code the list name followed by period "." , then the instruction `append(25)`.
# We can see the result here by coding "print(scores)"
scores = [24, 23]
scores.append(25) 
print(scores) 
# We add value to a specific index whith "insert()". By coding "insert(0, 30)",we'll add the value  to the start of the list.
#The index we want to insert the value at comes first, then the value.
# Whith  both "append()" and "insert()", we can add just one element at a time. 
scores = [24, 23]
scores.insert(0, 30) 
print(scores) 
# To remove the LAST element of a list , we code the list name "score" , a pariod ".",  and the instruction "pop()"
scores = [30, 24, 23]
scores.pop() 
print(scores) 
# To remove a value at a specific index, w ea dd the index we want to remove in parentheses, like pop(1)
scores = [30, 24, 23]
scores.pop(1) 
print(scores) 
#The removed value can be stored inside a variable too. We can see it here when we code "print(removed)"
scores = [30, 24, 23]
removed = scores.pop(1) 
print(removed)
# ______________________
#4.Looping overlist
#There's an easy way to loop through all the elements of list by using a "for" loop
#To loop through the elements in the 'final_scores' list, we write "for", a variable like 'score', the word "in", and the list 'final_scores'
# The loop will run for as many elements as there are in the list. We'll see four elements in the console here by coding "print(score)"
final_scores= [17,22,34,13]
for score in final_scores:
    print(score)
# The variable before "in" holds the value of the list element the loop is currently on . Here, we'll use 'artist'  for the variable.
artists= ["Zandalar", "Amani"]
for artist in artists:
    print(artist)
    print("______________")
#________________________
#5. Deciding with Lists
#Let's find out how we can count the elements in lists and use them with "if" statements(вираз, твердження)
# We use the "len()" instruction with the list name in parentheses to get the number jf elements in a list.
users =["Taras", "Oksana", "Vlad"]
print(len(users)) 
# We can store the lenght of a list in a variable, like here with 'number_of_users'
users =["Taras", "Oksana", "Vlad", "Ira"]
number_of_users = len(users)
print(number_of_users)
# If we use "len()" on an empty list it'll return "0". We can see it here when we display("print") the 'number_of_users' variable.
# We can use list lenght to create conditional statemants(вираз з умовою) based on the number of elements like here with "len(tasks)>0"
tasks = ["Почистити зуби", "Вмитися","Сходити в туалет", "Зробити фізичну зарядку"]
if len(tasks)>0:
# PYTHON BASICS
#1. Creating Variables
# To create a variable(змінна), we need to give "name". Variable names need to be single words and ,therefore(внасідок цього),have no spaces.
city
#If we want a variable name with multiple words, we use `snake case`. Snake case means using "_" to connect the additional words.
home_city
#To help us understand what's inside a varіable we pick descriptive(описуючі назви) names.
# After creating and naming variable, we use the "=" sign(знак) to store a value(значення) inside it, like 
city="Poltava"
# The values we have been storing, like "Poltava" are `string`(рядок).Strings are words in double quotes.
"Ukraine"
# Strings can contain all sorts  of letters and symbols, including spaces, like
"Winter is coming!!!"
# With the spacial instruction "print()", we tell the computer to display a value in area called the `console`,also known as the shell.
print("We will win !!!")
# We can use "print()" to display variables like `greeting` too.
greeting="Hi everyone!!!"
print(greeting)
#________________________________________________________________________________
#2.Using Variables
# Variables are called variables because the values they store  can change. We can update `status` by using "=" and giving it new value. 
# We can update variables as often as we want. 
status = "Reading"
status = "Sleeping"
print(status)
# We can also give variables the values of other variables. Here , we can give the `new_status` variable the value of `default_option`
default_option= "upload"
new_status="download"

new_status=default_option
print(new_status)
# When we update a variable, it forgets its previous value. 
# We call adding string values(рядкові значення) an `expression`(вираз) as it creates asingle value. One string displays when we add "55" inside "print()"
print("Followers:"+"55")

from typing import Counter

name="THROLL"
greeting=name
print("3,2,1")
print("GO!!!!")
print("Taras Strikha!!!!")
print (greeting)
followes= "999"
print("Players of the HORDE:"+ followes)
Alians="Alians suck hord's dicks :"+"1000"
print(Alians)
print("You killed:")
number_of_kills=40
print(number_of_kills+1)
killed_dd= 24
killed_rdd= 16
total=(killed_rdd+killed_dd)
print("Total kills:")
print(total)
correct=True
print(correct)
status= False
print( not status)
orc=True
human=not orc
print(human) 
print(10==10)
print(9==10)
print( not killed_rdd==10)
print(10!=10)
result= 1!=2
print(result)
one= 1
two= 2
print(one == two)
print(one != two)

id_1="#4"
avarage_grade_1="A"
test_score_1=90
id_2="#5"
avarage_grade_2="A"
test_score_2=70
no_duplicates=id_1!=id_2
print("No duplicate enteries:")
print(no_duplicates)
same_average=avarage_grade_1==avarage_grade_2
print("Same average grade:")
print(same_average)
higher_score=test_score_1>test_score_2
print("id_1 has a higher score: ")
print(higher_score)

if True:
    print("Lok tar'o'gar!!!!!!!!")

greet= True
if greet:
    print("Асетавалена!!!!")
is_charged=False
if is_charged:
    print("Charged!")
print("Low battery!!! Alarm!!!")

answer="Taras"
if answer=="Taras":
    print(answer +" is correct!!!")

if answer!="military":
    print(answer+" is wrong!")
age=65
if age>=55:
    print("Discount applied!!!")

score=51
pass_grade=score>50
if pass_grade:
    print(pass_grade)
song="Король і шут!!!"
relay_times=365
if relay_times >=300:
    print("Моя улюблена група на цьому тижні:")
    print(song)

today="Sunday"
if today !="Saturday":
    print("Set alarm at 8:00")

availeble=False
if availeble:
    print("Yes it's done")
else :
    print("No no no !!!")

number=99
if number==1:
    print("It's one")
else:
    print("It's not one")

hour=5
if hour<12:
    print("good morning!!!")
elif hour<17:
    print("Good afternoon!!!")
else:
    print("good night!!!")

#Programs repaet the same lines of code over and again to build all sorts of things like the repeated elements in the app
# One way to repaet lines of code is to  write them over and over again, but it takes a really long time if we want to create larger programs.
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")
#  To build larger programs and websites, we repeat lines of code using a while loop
# while True: 
#                 # print("and again")
# Skip the code block of the "while" loop by setting the condition to False
while False:
                print("Skip me !")
# The loop runs its entire code block because "keep_going" is True at first, but doesn't run again "keep_going" to False
keep_going= True
while keep_going==True:
                print("and again")
                keep_going= False
                print("one more time")     
#Controlling While Loops
#Inside the block, we make the condition return "false" and stop the loop by incrementing the counter variable. Try it whith "counter +=1"
counter=32
while counter <= 44 :
                print(counter)
                counter+=1       
#Like this program repeating statemants to display The Amarican Flag.
first_counter=0
while first_counter<5:
                print("**********-------------------")
                first_counter+=1
second_counter=0
while second_counter <4:
                print("-----------------------------")
                second_counter+=1  
#In "for" loop we can specify how many times we would like our loop to run with the "range()" statement
for i in range(5):
                print("Happy Birthday!!!!")
# Adding a number like "6" inside "range()" means it'll loop overthe block 6 times, from 0 to 5 
for i in range(6):
                print(i)

#The variable before "in", in this case,"i",is the counter variable. It counts what repetition of the loop we're currently on.
for i in range(3):
                print(i)
                print("For loops are great!")
#We'll piece together different parts of a link to  give users a 50 % discount when signing up whith the link. 
base="www.homeflix.com"
coupon="signup/coupon"
discount=50
amount=4

for num in range(amount):
                print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")
#ORGANIZING DATA
# _________________________
# 1.Grouping Data in  Lists 
#
# Rather than creating a variable for each new piece of data, we can collect related data inside a "list" using "[" and  "]"
todo=["Read", "Workout", "Code"]
print(todo)
#_____________________________
#2. Changing Data in Lists
#
# Let's dig depper into maniging lists and how to update the data inside them, like how temperature data might change throughout the day
# Lists can store any piece of data, be it string(рядок), boolean(логічне значення), float(число з комою) or integer(ціле число) like 17
# Every element in a list has a numbered position called index. 
#                                                     [ _ , _ , _ , _ ] 
#                                                       0   1   2   3
#                                                           INDEX
# To access element 20, code the list name temparatures followed by the INDEX of the element between square brackets [1]
temparatures = [17, 20, 26, 24]
print (temparatures [1])
# To change the third temperature value in the list, access it through temparatures [2], then use = to assign it a new value like 25.
# Despite (недивлячись на те що ) having four elements in the list, we access the LAST INDEX by using 3 here , since (починаючи, беручи) the counting starts at zero. 
temparatures = [17, 20, 26, 24]
temparatures[2]=25
print (temparatures)
#__________________
# 3. Updating Lists
# 
# Lets learn how to add and remove values in a list . Like in this app, which uses a list to manage user's score data. 
# To add the value 25  to a list ,  we code the list name followed by period "." , then the instruction `append(25)`.
# We can see the result here by coding "print(scores)"
scores = [24, 23]
scores.append(25) 
print(scores) 
# We add value to a specific index whith "insert()". By coding "insert(0, 30)",we'll add the value  to the start of the list.
#The index we want to insert the value at comes first, then the value.
# Whith  both "append()" and "insert()", we can add just one element at a time. 
scores = [24, 23]
scores.insert(0, 30) 
print(scores) 
# To remove the LAST element of a list , we code the list name "score" , a pariod ".",  and the instruction "pop()"
scores = [30, 24, 23]
scores.pop() 
print(scores) 
# To remove a value at a specific index, w ea dd the index we want to remove in parentheses, like pop(1)
scores = [30, 24, 23]
scores.pop(1) 
print(scores) 
#The removed value can be stored inside a variable too. We can see it here when we code "print(removed)"
scores = [30, 24, 23]
removed = scores.pop(1) 
print(removed)
# ______________________
#4.Looping overlist
#There's an easy way to loop through all the elements of list by using a "for" loop
#To loop through the elements in the 'final_scores' list, we write "for", a variable like 'score', the word "in", and the list 'final_scores'
# The loop will run for as many elements as there are in the list. We'll see four elements in the console here by coding "print(score)"
final_scores= [17,22,34,13]
for score in final_scores:
    print(score)
# The variable before "in" holds the value of the list element the loop is currently on . Here, we'll use 'artist'  for the variable.
artists= ["Zandalar", "Amani"]
for artist in artists:
    print(artist)
    print("______________")
#________________________
#5. Deciding with Lists
#Let's find out how we can count the elements in lists and use them with "if" statements(вираз, твердження)
# We use the "len()" instruction with the list name in parentheses to get the number jf elements in a list.
users =["Taras", "Oksana", "Vlad"]
print(len(users)) 
# We can store the lenght of a list in a variable, like here with 'number_of_users'
users =["Taras", "Oksana", "Vlad", "Ira"]
number_of_users = len(users)
print(number_of_users)
# If we use "len()" on an empty list it'll return "0". We can see it here when we display("print") the 'number_of_users' variable.
# We can use list lenght to create conditional statemants(вираз з умовою) based on the number of elements like here with "len(tasks)>0"
tasks = ["Почистити зуби", "Вмитися","Сходити в туалет", "Зробити фізичну зарядку"]
if len(tasks)>0:
    print("Закінчи вранішні процедури")