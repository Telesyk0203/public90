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
#Organizing Data 
# Rather than creating a variable for each new piece of data, we can collect related data inside a "list" using "[" and  "]"
todo=["Read", "Workout", "Code"]
print(todo)
