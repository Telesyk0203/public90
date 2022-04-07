<<<<<<< HEAD
# PYTHON BASICS
#1. Creating Variables
# To create a variable(змінна), we need to give "name". Variable names need to be single words and ,therefore(внасідок цього),have no spaces.
#city
#If we want a variable name with multiple words, we use `snake case`. Snake case means using "_" to connect the additional words.
#home_city
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
# When expression contain(містить) variables, they use the values in the variables, which we can see when adding "Followers:" to `followers`
followers="3850"
print("Followers:" + followers)
# Since(оскільки) expression become values, we can give them to variables like values, like here where we'll code `lable` to display the expression
label= "Posts:"+ "15"
print(label)
# We'll encounter(зустрічаємось з, стикаємось) many other kinds of values in Python ,too. Like `numbers`, which have no double quotes around them.
# Numbers make it easier to keep track of `numeric data`. 
#We can create expression with numbers, too. Here, we can numbers together with `+1`
number_of_app = 5+1
print(number_of_app)
#We use the `*` sign to multiply(помножити) numbers. We'll turn 0.5 thr `/` sign to divide(поділити) числа.
percent = 0.5 * 100
print(percent)
# We can use variables with numder for calculatrions, too. We'll see it in action by adding `1` to number_of_steps.
number_of_steps=70
print("You're on step:")
print(number_of_steps+1)
# Since expression become values, we can store calculation results in variables, like here where "total" contains "private+public"
private=30
public=97
total= private+public   
print("Total posts:")
print(total)
#_________________________________________________________________________________________________________
#True and False
 # True is great for situations like checking if a feature is on or if data is available. We can see it here when we set "powered_on" to True.
powered_on=True
# We can store True in a variable just like a string or number.
correct=True
print(correct)
# False is another special value and the opposite of True
status=False
=======
# PYTHON BASICS
#1. Creating Variables
# To create a variable(змінна), we need to give "name". Variable names need to be single words and ,therefore(внасідок цього),have no spaces.
#city
#If we want a variable name with multiple words, we use `snake case`. Snake case means using "_" to connect the additional words.
#home_city
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
# When expression contain(містить) variables, they use the values in the variables, which we can see when adding "Followers:" to `followers`
followers="3850"
print("Followers:" + followers)
# Since(оскільки) expression become values, we can give them to variables like values, like here where we'll code `lable` to display the expression
label= "Posts:"+ "15"
print(label)
# We'll encounter(зустрічаємось з, стикаємось) many other kinds of values in Python ,too. Like `numbers`, which have no double quotes around them.
# Numbers make it easier to keep track of `numeric data`. 
#We can create expression with numbers, too. Here, we can numbers together with `+1`
number_of_app = 5+1
print(number_of_app)
#We use the `*` sign to multiply(помножити) numbers. We'll turn 0.5 thr `/` sign to divide(поділити) числа.
percent = 0.5 * 100
print(percent)
# We can use variables with numder for calculatrions, too. We'll see it in action by adding `1` to number_of_steps.
number_of_steps=70
print("You're on step:")
print(number_of_steps+1)
# Since expression become values, we can store calculation results in variables, like here where "total" contains "private+public"
private=30
public=97
total= private+public   
print("Total posts:")
print(total)
#_________________________________________________________________________________________________________
#True and False
 # True is great for situations like checking if a feature is on or if data is available. We can see it here when we set "powered_on" to True.
powered_on=True
# We can store True in a variable just like a string or number.
correct=True
print(correct)
# False is another special value and the opposite of True
status=False
>>>>>>> 0a561cb385807e3ba107454766433f41c85fba8b
print(status)