""" 
lists.py

At this point we know how to do these things:
    - Do basic arithmetic with variables
    - Take in keyboard input with input()
    - Typecast stuff into the appropriate data types
    - Branching control structures using if-elif-elses
    - Repetition control structures using while
    
If we wanted to aggregate a bunch of related pieces of data (variables), how would we do that?
"""

var1 = 1
var2 = 2
#^doing this for large amounts of data (n > 3) starts to become unwieldly quickly 

""" 
We are storing a bunch of related data points in separate references in memory. This sucks.

We want a way within our programming language to store a bunch of related information inside one
reference (address). 

lists = ordered linear structures that store variables.

lists ARE VARIABLES (so everything you know about creating variables still applies here)


"""

#<name of the list> = [<member attributes>]

mylist = [5,10,15,20]
#^all multiples of five stored in a list.

print(mylist)
#Just prints the entire list, including square brackets. 

""" 
I really want to know, how do we access certain elements inside our list? We made our list using square 
brackets, we can access things using the same square brackets. To access things in a list: 

<name of the list>[<index of the attribute you want>]

index = the position the element resides inside the list.
"""

print(mylist[0])

""" 
counting in computer science does NOT START FROM 1. Counting in computer science starts from 0. 

so really, the first element is mylist[0].

manipulating things inside lists still works the same way we expect it to relative to variables. 
"""

print(mylist[0] * mylist[1])
     #5 * 10
     

sum = mylist[0] + mylist[3]
print(sum)

""" 
what happens if we try to print an element that is not there?
"""
mylist = [5,10,15,20]
          #0,1,2,3
#print(mylist[4]) #We get a list index out of range. We tried to access a place in memory 
#not allocated to anything in particular. 
print("negative element")
print(mylist[-1])

""" 
negative indices traverse the list backwards.

So if you have experience in java, c, c++, c#, whatever different language you use, you would think
list attributes all have to be the same data type. lists in python can have mixed data types
"""

mylist2 = [1,10,True,"Hello"] #This is a valid list
print(mylist2)

""" 
You need to be very careful when you have mixed datatypes inside of a list

the reason why we can 1 to True is because True is really the number 1
"""

#print(mylist2[0] + mylist2[3]) #I should get a type error here 

""" 
The natural way to be manipulating lists is through traversal.

traversal = some sort of looping statement that goes over either 
    1) a subset of the list
    2) the entire list
    
    goes through = accessing each element in the subset or the entire list 
    

the only looping statement we know is with a while loop.

while <condition>:
    <code block>
    
The typical idiom <= style

is by using a variable that we call an iterator.

the iterator will correspond to each index of our list
"""

mylist = [5,10,15,20,25]
          #0,1,2,3

#if we had an iterator, we want the iterator to be equal to the values 0,1,2,3
#we typically name iterators i

i = 0 #This is going to be our iterator 
print("individual elements")
while i <= 3:
    print(mylist[i])
    i = i + 1 #we call this incrementing our iterator by 1
    #we should access every element inside our list now

#This example is a level of abstraction already much deeper than what we've encountered so far 

""" 
There are some modifications we need to do to this example. We are making a ton of assumptions that we
can't make. 

    1) we're assuming the list is always going to be size 4. 
    2) we're assuming the last index is going to be 3. 
    
the list might change size. There is a function in python that we can use that rectifies this 
assumption that we're making. 

len(<name of list>) <= this returns the size of the list
"""
print("printing size")
#print(len(mylist))
#This printed the number 5. If we want to use len() to help us find the last element of our list
#just do len() - 1

""" 
We can traverse a list using a while loop <= we know we can do this.

There is a second way to do repetition in programming that i have not mentioned yet. 

while loops
for loops <- I waited to teach this because for-loops in python are ingrained into the list structure. 

for loops do effectively the same thing as a while loop WITH THESE EXCEPTIONS:
    1) <place holder name> will become a temporary variable corresponding to an element inside the list
    2) for-loops traverse the list, but they don't edit the actual contents of the list
        num is A COPY of the elements of thel ist 
    
for <some placeholder name> in <name of list>:
    <code block>
"""
mylist = [5,10,15,20,25,30,35]
#for loop
print("for loop example")
for num in mylist: #for-loop makes copies
    num = num + 5

print(mylist)


#while loop
i = 0
while i <= len(mylist) - 1: #This structure will traverse the entire list regardless of how the list 
    mylist[i] = mylist[i] + 5 #evolves throughout the program's runtime. #while loops access member attributes
    i = i + 1
    
print(mylist)

