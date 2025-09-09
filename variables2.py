""" 
Computer programs are not just us typing in the code and having the python interpreter run the thing. 

Programs typically have user interaction. In this class, we are typically concerned with input and output from the keyboard into the terminal

In python, getting keyboard input is actually incredibly easy. There's a built in function called "input()"

What input() does is 
    - prints a prompt into the terminal 
    - waits for keyboard input into the terminal
    - takes that keyboard input and saves it into variable 
"""

print("Welcome to calvert hall!")
name = input("What is your name? ")
#Variable = input(<prompt>) 
gradyear = input("What year do you graduate? ")
standing = input("What is your class standing? ")
email = input("What is your email? ")
#I have an extra space at the end of my input prompt strings. The reason why we do this is python doesn't place trailing whitespace automatically
print(f"My name is {name}, I graduate in {gradyear}, my class standing is {standing}, and my email is {email}")

""" 
I was very particular with the data types I wanted you to ask for input of. All of those variables were effectively strings.

What about numerical data types?
"""
#10 for x and 5 for y 
x = input("What is num1: ")
y = input("What is num2: ")
x = int(x)
#This changes the datatype of x into an integer
y = int(y)
#This changes the datatype of y into an integer

#we should expect z = 15 
z = x + y 
#This will become an integer because its int + int
print(z)
#this should be 15

""" 
Recall this fact:
    - Variables carry three pieces of information
        - The name of the variable
        - its attribute (data)
        - The data type 
        
    - Input specifically returns strings
    
    we want x and y to be ints, but they got returned as strings. To fix this, we do something called typecasting
    
    typecasting = changing the datatype of a variable (as long as the result is valid)
"""