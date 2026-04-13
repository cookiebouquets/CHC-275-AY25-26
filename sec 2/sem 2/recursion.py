""" 
Recursion.py


Let's talk about functions:
    - f(x) = x^2, it takes an input x and multiplies it by itself. 
    - Named procedures that we can call to perform some subtask in our program 
        - Evaluate step by step from start to finish
"""

def foo(x):
    if x % 2 == 1:
        return "Odd"
    if x % 2 == 0:
        return "Even"
    
""" 
Function ends after either the function body ends or when a value is returned. What recursion does is it allows us to have repetition in our program
without having any for-loops/while-loop 

A recursive function is a function that calls itself within the body of the function 
"""

def bar():
    print("hello") #printing hello
    bar() #calling bar again within the body of bar
    
""" 
Running this function just prints hello infinitely. This is a rabbit hole that gets very deep very quickly.

The question is: how do we make it so the program doesn't run forever? We need something called an exit condition (base case)

Every single recursive function can broken down into two pieces:
    - Base Case (This ends the function call)
    - Recursive Case (repeats until you hit the base case)
    
For a recursive function to end, your recursive case HAS to be able to reach the base case

"""

def countdown(n):
    #print every value from 10-1
    
    #base case
    if n == 0:
        return 
    
    #recursive case
    print(n)
    countdown(n-1)
    
countdown(10)

""" 
Typically every single recursive function can be implemented iteratively (for-loops), so the question is: why do we care at all about implementing procedures recurisvely

Answer: a lot of the time, procedures that are hard to implement with for-loops are much easier to implement with recursion

Factorial in math

5! = 5 * 4 * 3 * 2 * 1 <= this procedure can be easily implemented recursively, and its a little to understand iteratively


is 5! equivalent to 5 * 4!
                        4 * 3 * 2 * 1
                        
is 5! equivalent to 5 * 4 *3!
                           3 * 2 * 1

5! = 5 * 4 *3 * 2!


1! = 1

x! = x * (x-1)!

Base Case: 1! = 1

Recursive Case:  x * (x-1)!
"""

def factorial(x):
    """
    It multiplies x by every value less than x 
    """

    if x == 1:
        return 1
    
    return x * factorial(x-1)

print(factorial(5))

""" 
Fibonacci Sequence: 
    0, 1, 1, 2, 3, 5, 8, 13, 21 .....
    
The Fibonacci Sequence is defined by a function called the Fibonacci function. 

F(n) = F(n-1) + F(n-2)

Base Cases:

F(0) = 0 and F(1) = 1

Recursive Case:

F(n) = F(n-1) + F(n-2)

"""

def fibonacci(n):
    #Base Cases
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    #Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print()
for i in range(11):
    print(fibonacci(i), end = " ")
    
""" 
Palindrome, we can also do it recursively

RacecaR
R     R
 a   a
  c c
   
   e
   
In terms of palindrome, what could be a good basecase? len(word) =1

RacecaR
 AcecA
  CeC
   e
   
Recursive Case could just be checking the endpoints of each subword (where a subword is the endpoints of previous subword) 
"""

def palindrome(word):
    #base case
    if len(word) == 1 or len(word) == 0: #len word == 1 for odd letters and len  word == 0 for even letters
        return True
    
    #Recursive Case
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
                            #this gives second letter through second to last letter
    else: 
        return False
    
print()
print(palindrome("moom"))


word = "racecaR"
print(word[::-1])
    
""" 

"""