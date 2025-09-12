""" 
Running the calculator program probably shouldn't involve doing all four operations at once

It would be nice if we could select one thing from a list of options and just do that operation

IF we select one thing 
    something should happen
ELSE IF we selecting some other thing
    something else should happen
    
We want some sort of branching logic. 

Vocab:

boolean = True or False  

Conditional = Some statement that can be evaluated to a truth value 

5 + 5 = 10
    True
    
It's rainy today
    True
    
There's a lot of traffic on 695
    True
    
5 + 10 = 9
    False
    

The logic behind branching:

1) Some conditional we want to check the truth value of
2) After we check the truth value, 
    a) do A
    b) or do B
    

"""


""" 
% <= This is called the modulus operator 

A % B (A mod B) = divides A by B, but the result is the remainder 

10 % 7 = 3 
5 % 2 = 1 

Checking divisibility rules:
    1) If you have a remainder of 0, then A is divisible by B 
    2) Checking if a number is even or odd
        a) A mod 2 == 0
"""

""" 
if <conditional statement>:
    <tabbed over code block> 
    
I used two equals signs. 

1) = <- this is variable assignment 
2) == <- equality checking 

Everything that is tabbed over only runs as a result of the conditional evaluating to a true value 
"""




""" 
whitespace in python (tabs, hitting the space bar) denotes scope 

If you expect things to work correctly, then everything has to have the same amount of white 
space before it


What if we want something to happen as a result of the if-statement failing? 

else


if <conditional>:
    <tabbed over code block>
else: 
    <tabbed over> 
    
else is your fail condition, it only runs if the if-statement fails 
"""

"""
if 10 % 2 == 0:
    #This will run if the if is correct
    print(f"{x} is divisible by 2")
    print("Test")
else:
    #This will run if the if is false
    print("This is not a part of the if statement")

"""

"""
if x % 2 == 1:
    #This will run if the if is correct
    print(f"{x} is divisible by 2")
    print("Test")
    
#This will always run
print("This is not a part of the if statement")
"""

""" 
if <conditional>:

else:

if <something>:

else if <something else>:

elif <- contraction of else and if.

"""

 
x = 10
#Try changing x = 3, 4, 5 
if x % 5 == 0:
    print(f"{x} is divisible by 5")
elif x % 2 == 0:
    print(f"{x} is divisible by 2")
else: 
    print(f"{x} is not divisible by by 5 or 2")
    
""" 
If we tried a number that was divisible by both 5 and 2, only the first condition runs. 

Maybe this isn't what we want. 

What happens in the backend:
    1) Once the if statement is evaluated, the python intrepeter skips all other parts 
    of the if-elif chain and just goes to the next line. 
"""
x = 10
if x % 5 == 0:
    print(f"{x} is divisible by 5")
    
if x % 2 == 0:
    print(f"{x} is divisible by 2")
else: 
    print(f"{x} is not divisible by by 5 or 2")
    
    
    
    
""" 
We can have multiple conditions inside of one if statement

if <conditional>:
    <code block>
    
if <condition 1> and <condition 2>: #1 and 2 MUST be satisified
    <code block>
    
if <condition 1> or <condition 2>: #1 or 2 MUST be satisifed 
    <code block>
"""

x = 10

if x > 5 and x > 15:
    print(f"{x} is greater than 5 and 15")
    
if x > 5 or x > 15:
    print(f"{x} is greater than 5 or 15")
    
    
#Two new keywords, AND and OR
#and needs BOTH conditions satisified, or needs only ONE condition satisified 

""" 
These are really weird examples 

- equality checking == 
- greater than > 
- Less than < 
greater than or equal to >=
less than or equal to <= 

How can we adapt this into a program that makes sense? Let's say we want to write a program that prints something different 
if you are a freshman, sophomore, junior, or senior 

we want to write a program that does something new whenever we type in a different thing on an individual run of the program
    - variables
    - inputs
    - if else statements
"""

year = input("Enter your year: ") #This has to be freshman, sophomore, junior or senior

if year == "freshman":
    print("your grade level is 9")
elif year == "sophomore": 
    print("Your grade level is 10")
elif year == "junior":
    print("your grade level is 11")
elif year == "senior":
    print("Your grade level is 12")

"""
something extremely tricky happens with strings. Equality checking with strings is extremely strict. for equality checking, the strings
HAVE to match exactly.

"freshman" != "Freshman" 
"freshman" != "freshman "
"freshman" != " freshman"
"freshman  " != "freshman "

Lets think back to our calculator 
"""