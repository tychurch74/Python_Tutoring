
#Comments--------------------------------------------------------------------------------------------------------------------
#Comments are simply notes that the program ignores and is a way to provide explaination about your program.

#Single line comments start with the number sign (hashtag)

'''
multi line
comments 
start and end 
with 3 quotation marks
'''

#Variables:------------------------------------------------------------------------------------------------------------------
#python variables can be named anything, they just can't contain any spaces. Example:

x = 3
y = 4
python_variable = 69

#variables can be changed at any time. Example:
x = 2
y = 3
python_variable = 96

#variables can equal other variables. Example:
x = y

#variables can equal the result of an equation. Example:
z = x + y
math = 32 * 32

#variables can equal words and phrases. Example:
hello_world = "Hello World!"


#Strings--------------------------------------------------------------------------------------------------------------------
#the variable example above showed what is called a string. A string is simply anything you don't want to assign a value to.


#The terminal---------------------------------------------------------------------------------------------------------------
#the terminal is simply the window that shows the output of your program. You can use print() to output anything to the terminal
print(hello_world)
print(python_variable)
#when you run this program you'll see the phrase Hello World followed by 96

#The program can also receive input from the terminal. Example
user_input = input("Say anything!: ")
print("User said:")
print(user_input)

#You can include variables in a string as well. Example:
print(f"f string plus user input: {user_input}")


#Loops----------------------------------------------------------------------------------------------------------------------
#a for loop essentially runs the same code over and over again for a set number of times

#the following loop basically says for i numbers between 1 and 5 (not counting 5) run this code
for i in range(1,5):
    #remember to single indent (tab)
    print(f"loop number:{i}")









