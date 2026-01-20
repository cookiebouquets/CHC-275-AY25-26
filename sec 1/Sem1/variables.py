""" 
I am going to do what is live coding.

live coding = I type my thoughts out along with code snippets that correspond to what i'm describing

what you need to do during instructional days = write the code snippets and run the code and ssee if it
works the way you expect 

At this point, we shouldve made a file called hello.py and got it to print hello world by doign

print("Hello world")

some background 

python is two things

    1) its a programming language: a way to write instructions to our computer for it to follow. 
    2) its a program: 
        i) when you install python on a computer, you are installing what is called the python interpreter
        
python interpreter: 
    1) looks at your file, and line by line converts the python syntax into a way your can understand
    the instructions
    
if you have programming experience in a different language, C, C++, etc., this is weird because 
we don't have to compile our programs into executable <= if this means nothing to you right now, dw about iot

The first thing we want to learn about are variables

variables in a programming language are effectively the same thing as a variable in math

    - numbers
    - strings of text
    - a true/false value, etc.
    
Variables are named places in memory that store attribute

    - numbers
    - strings of text
    - a true/false value, etc.
    
    
<variable name> = <attribute>
"""

num = 5
""" 
This creates a variable, named num, and its attribute is the number 5 
"""

""" 
print(<variable name>) 
"""

print(num)
x = 10
print(x)

""" 
We can do basic four function arithmetic

adding + 
subtracting - 
multiplying *
dividing /
"""

print(num + x)
print(x - num)
print(num * x)
print(x / num)

""" 
This is great that we can print these things out, but its not exactly useful

the python interpreter is stupid: it doesn't remember what it printed out, it doesn't remember
the results of mathematical operations unless you tell it to. 

"""
sum = num + x
#This should be the same result as 10 + 5 
print(sum)

""" 
A big thing in computer science philosophy: make sure you are constantly updating variables that you want to be updated. 

What kids have struggled with in the past is workign in a sequential train of thought

x = value
do something to x -> save it back into x
x = value + some operation done to it 
"""

x = 5
y = 10
z = 0
#z is our working variable, we save results of operations into z
#We want to take the average of x and y 
z = x + y 
#working variable set to the sum of x and y
print(z)
#So Z is already set to 15, we just to divide z by 2, but we also need to set it back into itself 
z = z/2 #this is something that would not happen in a math class, but its perfectly valid in programming

#because the equals sign in programming is a variable assignment and not a test of equality 
print(z) 

""" 
That is more or less what I have to numerical operations. Let's talk about in strings

Data types:
    - Numerical Data Types:
        - integers (whole numbers and negative)
        - floating point (decimal numbers)
    - Strings
        - collections of individual characters that come together and are stored under one variable name
        - JUST PLAIN TEXT
"""

name = "Jack Basmaci"
        #To create a string, it's imperative that you put double quotations around the string
        #Single quotations are good too, but they have to be matching
        
occupation = 'Teacher'
        #As long as you match between double or single it should be okay. 
        
print(name)
print(occupation)
#Great, printing them out works exactly the way we want them to. What about putting our name inside of 
#another string? 

#We can print variables inside other strings of text in python using something called f-strings
 
""" 
f-strings are short for format strings, basically they allow us to specify different formatting requirements
inside of a print statement 

We want to print: "my name is ______ and my occupation is _____"
"""
print(f"My name is {name}, and my occupation is {occupation}")
    #This techinque is called f-strings 
    
""" 
f-strings are good, but there are times where we want to do math operations on our strings 

concatenation: combining two strings together 

"""

first = "Calvert"
second = "Hall"
school = first + second
        #You can concatenate strings by calling the + sign between your two strings
        #This is important because sometimes we want to create new strings with lists of individual characters
        #Particularly when we want to do a palindrome program 
print(school)

school = second + first
       #String concatenation is not commutative, if we reverse the strings in our additiion
       #The output also gets reversed
print(school)

""" 
Within this class, numerical data and string data are our most common data types. 

We're gonna a whole cycle dedicated to weird things you can do with strings later on. 
"""