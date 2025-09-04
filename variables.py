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

the python interpreter its stupid: it doesn't remember what it printed out, it doesn't remember
the results of mathematical operations unless you tell it to. 

"""
sum = num + x
#This should be the same result as 10 + 5 
print(sum)

