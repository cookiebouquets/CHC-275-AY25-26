""" 
Recursion.py

1) Recursion
2) Algorithmic Complexity 

Let's talk about functions (both in the math sense and in the cs sense)

Functions: Named procedures that take an (optionally) input and (optionally) produce
an output

f(x) = x^2 it takes x and outputs x*x

def foo():
    print(bar)
    
all this did was print "bar" when the function was called

functions are named procedures with repeatable steps. Every time we use a function
we called that "calling the function" 

foo() <- a function call 
    
    
Functions have these facts associated with them:
    1) They have their own local scope: variables that are declared inside of a function's
    body do not persist after the function call ends
    
    2) A function signature: name of the function, its parameters (inputs), return type
    
All a recursive function does is it calls the function within its own body.
"""

def foo(): #declared within the namespace of our program
    print("bar")
    foo() #I can now call it again within the body of its function
    
""" 
Recursive functions are just functions that call themselves within the body

If your recursive function doesn't exit, you'll get something called stack overflow

When you call the python program in your terminal 

    1) It creates the stack
    2) It creates the heap
    
The stack has a fixed size of memory (It occupies a fixed, limited amount
of memory on your computer's ram)

The heap was dynamically sized (so the size of the heap can expand or contract)

individual numbers/strings/etc are created on the stack
lists/dictionaries/2dlists/etc are created on the heap 

Every time you call a function, that function call gets put on the stack



- foo()5 <- print(bar) <- foo() 1
- foo()4 <- print(bar) <- foo() 2
- foo()3 <- print(bar) <- foo() 3
- foo2()2 <- print(bar) <- foo() 4
- foo1()1 <- print(bar) <- foo() 5


Some characteristics about stacks: LIFO <- the MOST RECENT function call 
is the one that gets removed from the stack first

How do we guarantee a recursive function ends? 

Base Case: Exit condition

Recursive Case: which repeats itself up until you reach the Base Case

For example: CountDown(n) is going to take a number n, and it'll print n and call
countdown(n-1) up until we get to n = 0

countdown(5) -> print 5 -> countdown(4) -> print 4 -> .... -> countdown(0) -> return

BaseCase: n = 0

Recursive Case: print n -> countdown(n-1) 
"""

def CountDown(n): #if I pass in 5,4,3,2,1
    #Base Case
    if n == 0:  #0
        return #ALWAYS EXITS THE FUNCTION
    
    #Recursive Case
    print(n) #5,4,3,2,1
    CountDown(n-1) #4,3,2,1,0
    
CountDown(5)

""" 
Recursion is really weird because we are implementing a repetition without actually using 
for loops or while loops. Recursion with a high degree of flexibility if you're good at it. 

Why use recursion over a for-loop or a while-loop? The problem details: 
    -Everything you can do with recursion can be reimplemented with for-loops and while-lopps
    -Even if that is the case, those solutions are a lot to come up with if the problem is inherently nonlinear
    
List() <- a linear data structure [1,2,3,4,5] <= you have a predefined notion of next
                                   n, n+1
                                   
sometimes the computational problems you work on don't have a generic version of next, or you're not
even working with a data structure at all, so you'll have to use a recursive solution

5! = 5 * 4 * 3 * 2 * 1 <= you find this a lot in probability

5! = 5 * 4!
         4 * 3 * 2 * 1
         
5! = 5 * 4 * 3!

The factorial has a recursive definition: !

x! = x * (x-1)!

Our base case is what: 

1! = 1

Recursive Case:
x * (x-1)!
"""

def factorial(x):
    #Base Case
    if x == 1:
        return 1
    
    #Recursive Case
    return x * factorial(x-1)

print(factorial(5))

""" 
So the factorial may not be a good of example for some people. Have you ever heard of the fibonacci sequence?

Fibonacci sequence is a sequence of numbers that goes roughly like this:

 0, 1, 1, 2, 3, 5, 8, 13, 21 .....
 
Generating the Fibonacci Sequence DEPENDS on the previous values of the fibonacci sequence. 

F(n) = F(n-1) + F(n-2) <= this is recursive: I'm calling F on the body of the function

Base Case:

F(0) = 0 and F(1) = 1

Recursive Case:

F(n) = F(n-1) + F(n-2)
"""

def fib(n): #Generate the n-th fibonacci number
    #Base Case
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    #Recursive Case
    return fib(n-1) + fib(n-2)

for n in range(10):
    print(fib(n))
    
""" 
Recursion does two things:

    1) nonlinear problems more tractable (more solvable)
    2) it provides a good representation on the logic of the program we're writing
    
Let's look at applications: 

a palindrome is a word that's spelled the same way forwards and backwards. We can implement this
recursively

racecar #palidrome(racecar)
r     r #if these are equal, call palidrome(aceca)
 a   a #if these are equal, call paindrome(cec)
  c c #if these are equal, call palidrome(e)
  
  e <= if e is by itself, we can infer that the previous calls succeeded, return True
  
noon #palidrome(noon)
n  n #palidrome(oo)
     #palidrome("") <= make sure we can work with even amounts of letters
    
Multiple Base Cases:
    n == 0
    n == 1
    Return True
    
Recursive Case
    if the endpoints the same, call palindrome on the substring with the endpoints removed
"""

def recursivePalindrome(word):
    #Base Case
    if len(word) == 1 or len(word) == 0:
        return True
    
    #Recursive Case
    if word[0] == word[-1]: #checking if the letter at the beginning and end are the same
        return recursivePalindrome(word[1:-1]) #call it on the substring with the endpoints removed
        
    #If the recursive check fails, the word is not a palindrome
    return False

print(recursivePalindrome("noon"))

""" 
All of these problems are linear: but what about nonlinear problems.

Problems in CS can really be broken down in 3 (maybe 4) categories
    - Searching Problems (information retrieval in large datasets)
    - Sorting Problems (sorting large datasets)
    - PathFinding (minimum cost paths in nonlinear datasets) 
        - GPS is a pathfinding algorithm, it finds the route that minimizing the amount of time
        on the road
    
The first two you can think of as being linear problems, but pathfinding is inherently nonlinear
    
"""

BOARD = [    #Entrance (0,0)
             [0,1,1,1,0,0,0],
             [0,1,0,1,1,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,1,0,0,1],
             [0,1,0,0,1,0,1],
             [0,1,0,0,1,0,0], #exit down here (len(board) -1, len(board[0]) -1)
    ]

""" 
How can we write a program that finds the only path from the top left to bottom right? 
    - a problem that is very very difficult to implement using for-loops and while-loops
    - but very easy to implement recursively 
    
No good notion as to what "next" means for a 2D-lists: Traverse across the row or Down the Column

So our recursive algorithm will effectively define what an optimal "next" is. <= this is what we're doing
tomorrow. 
"""