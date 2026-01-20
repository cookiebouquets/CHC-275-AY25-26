""" 
looping.py

What we know so far in terms of control structures: 
    - sequential (line by line evaluation)
    - branching (if-elif-else)
    - repetition (repeating code blocks over and over again)
    
We're going to some basic repetition. 

There are three ways of doing repetition
    - While loop (what we're doing today)
    - For loop (requires knowledge of lists)
    - Recursion (something we're not going to see until the second semester)
    
We only really know about
    - variables
    - input/output
    - typecasting
    - conditional statements
    
for while loops, they only require conditionals. so we can do repetition with the tools we already have. 

the reason why we want to do repetition is there are times where we want to calculate something over and over and over again to the point
where manually coding it in is unreasonable. 
"""
"""
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
"""
#Right now if we wanted to print 10 numbers, we would need 10 print statements. 
#This is already unreasonable. We can use while loops to do this 

""" 
How a while loop works:

while <exit condition>: 
    <code block>
    
    1. exit condition is checked
    2. if it's not met, execute code block
    3. jump back to 1

"""


""" 
It printed 1's over and over and over again until you hit something called stack overflow. 

stack overflow: Your computer allocates a certain amount of ram to a python program.

    When a python program is ran, your computer allocates two things:
        1) Stack: A fixed size amount of memory (limited amount of memory for a program/memory budget) 
        2) Heap: A dynamic sized amount of memory (blank check for a memory budget)
        
    function calls (prints, inputs, etc.) go on the stack. If you do it over and over and over again, then
    you will run out of memory on the stack and the program will crash. <= this is a stack overflow.

to avoid a stack overflow for a while loop, you NEED to meet the exit condition. 
""" 

""" 
The good about while loops is the conditional does NOT have to rely on a number. 

I can do the same on string matching.

Context: I want to write a program that loops over and over again until I type the word "quit"
The program will print out option 1 2 or 3 depending on what the user types in. 
"""

""" 
x = 1
while x <= 10: 
    #all numbers from 1 to 10
    print(x)
    #Two ways, one is a contraction, the other is like how it actually
    #x = x + 1 #The first way
    x += 1 #This is the shortcut
"""

""" 
To do this, you usually have some sort of check variable set to a boolean. 
"""

check = False

while check == False:
    option = input("Enter your option 1 2 or 3. type quit to exit: ")
    if option == "1": 
        print("option 1")
    elif option == "2": 
        print("option 2")
    elif option == "3": 
        print("option 3")
    elif option == "quit": 
        check = True

""" 
You have to be careful with the tabs, if you don't want something within the scope of a while loop, it 
needs to be outside of the while loop in terms of tab level 



"""