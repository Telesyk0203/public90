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
# We use the "len()" instruction with the list name in parentheses to get the number of elements in a list.
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
