#algorithms.py

""" 
Complexity Theory: Theory of computation

We need a way to reason about how to compare different programs that do the same effectively. Complexity Theory is a subfield of computer science/math that formalizes 
performance of computer algorithms

Understanding complexity theory at a basic level opens up the entire CS degree to you if have a good backbone on this stuff:
    - Finite State Automata Theory <- you need complexity Theory
    - Analysis of Algorithms <- you need complexity theory
    - Parallel Processes <- you need complexity theory 
    - Programming Language Theory <- you need complexity theory 
    
Thought Question: Let's say we're running the same piece of code on two separate computers with very different system specifications:
    - Should we expect this piece of code to run in the same amount of time on both computers even though its the same piece of code? No
        - You could have a super computer on one end and your laptop on another end 
        - We can't use time as an objective measure to compare algorithms/programs 
        
Complexity Theory more or less solves this hardware specification problem by introducing a formal mathematical system to analyze algorithms

Axioms = Rules for computation/mathematics

Axioms of Complexity Theory:
    1) Every program can be distilled into 3 things
        i) The size of the input of the program
            ex) the size of a list, the size of a database, etc., either measured in the amount of objects or the amount of bytes the input takes up on RAM
        ii) The size of the output of the program
            ex) linear/binary search the output is a single number (corresponds to the index at which the target was found)
        iii) A runtime complexity of the algorithm: The computational cost of running that algorithm 
        
    You can have effectively two of the same program if i-iii all match. How can we have a hardware agnostic measure of computational cost? There's one natural choice for this
    
    2) Computational Cost is measured in something called a Computational Unit (CU)
        i) A single line of code being executed = 1 CU
        ii) A "concept" of code being executed 
            for linear search/binary search the comparison is the "concept" 
            

Three things at play here: 

    1) The input size
    2) How many CUs used
    3) We place algorithms into buckets based on 1 and 2
    
For computer algorithms we typically use the WORST case to measure performance of algorithms: 
    - For a lot of algorithms: The best case is trivial
        ex) the best case for linear search is that the target is at index 0. 

    - A lot of the time, the input size is in the millions or billions
    
Let's call n = len(input). We're going to call O() <- big-O notation, and this corresponds to how many CUs were used to calculate the worst case of an algorithm 


linear search: 

n = 1000

Worst Case: 

The worst case is being at index = n-1 = the end of the list

We can say that linear search has a runtime complexity 

    O(n) = size of the list = n CUs used in the worst case

y = x <- this is a line 

CU = n <- this is also a line 

We can say something much more powerful than just linear search has runtime complexity of O(n) 

for-loops ALL HAVE A RUNTIME COMPLEXITY OF O(n). 

But what about nested for-loops?
"""

def linearSearch(list,target):
    
    #it finds the index of the target
    curr = 0
    for i in range(len(list)): #takes at least 1 execution and at most len(list) executions
        curr = i
        if list[i] == target:
            return i, curr
        
    return "not found"


def nested(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
            
            
#How can we analyze the runtime complexity of nested(n)?
#n corresponds to input size 


""" 
How many pairs are going to print for nested?

n = 2,  4
n = 3,  9
n = 4,  16
.
.
.
n, n^2

nested for-loops have a runtime complexity of O(n^2)

Every time we add an extra nested loop, we are raising the power of n

for a triple nested loop O(n^3)


is the cost of O(n^2) > O(n)? Yes

O(n^2) is SLOWER than O(n)


"""

def nested2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)


def binarySearch(list,target,curr_iter):
    mid = len(list)//2
    #Base Case
    if list[mid] == target:
        return target, curr_iter
    
    #Recursive Case:
    if list[mid] < target:
        return binarySearch(list[mid:],target,curr_iter+1)
    
    if list[mid] > target:
        return binarySearch(list[:mid],target,curr_iter+1)


""" 
[1...100]

I wanted to find 87.

Step 1:[1...100] 50 to 87. 50 < 87, we throw away everything less than 50

Step2: input [50...100] comparing 75 to 87, 75 < 87 so we throw away away everyting less than 75

Step 3: input [75 ... 100] 87 to 87, so we're done


at step 1: input size is n
at step 2: input size is n/2
at step 3: input size is (n/2)/2

At every step, binary search HALVES the search space. The inverse of this mathemaatically is 

2^x = this doubles at every step 1,2,4,8,16,32.

The inverse is Log_2(x), Everything is computer science is base 2,

Binary Search has a runtime compexity of O(log n)

O(log n) < O(n) < O(n^2)


1. O(n^2)
2. O(n)
3. O(log n)
4. O(1)

If no loops are usedd (or if the algorithm doesn't depend on the size of the input),we say that algorithm runs in constant time, O(1). 

Searching/sorting/pathfinding

dictionary lookups are notoriously fast in computer science. Searching a Dictionary is O(1) because of the hash function. What about other more complicated runtimes

O(n!) <- this is horrible 
O(n log n) is in between O(n^2) and O(n).

You might've heard of a problem P = NP <- this is a complexity theory problem.
"""

def foo(n):
    print("hello")
    
print(5*4*3*2*1 > 5^2)