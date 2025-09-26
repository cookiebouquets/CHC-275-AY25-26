""" 
lists2.py

just to reiterate, for-loops make COPIES of elements in lists, while loops directly access those there. 

There is a way to traverse a list using a for-loop while also directly accessing those elements. 


lists have 
    1) a name
    2) the elements
    3) an index
    
indices = 0,1,2,...,len(list) -1 <= possible values of our indices. 

our indices are also technically a list of numbers. 

rather than writing a for-loop that traverses the elements of the list. (this makes copies of the elements of the list)

we could traverse the list of the indices. There is a function in python called range() <= returns a list of numbers from 0 up to the number 
specified - 1

"""

mylist = [1,2,3,4,5]

print(mylist)

for i in range(len(mylist)): #this pulls out indices 
        #range returns a list of numbers from [0-4]
        mylist[i] = mylist[i] + 5
    
""" 
for num in mylist: #for-loop makes copies
    num = num + 5
    
this pulls out elements     
"""
print(mylist)

""" 
for i in range() loop <= for-i loops

for num in list loop <= for-each loops

In other programming languages, lists are typically fixed <= you cant add things to the list. In python, of course, we can add things.

"""

#<name of list>.append(<element>) adds elements

mylist.append(15) #<this adds the number 15 to the list
print(mylist)

#to remove things from a list, there are two ways. 

mylist.pop(0) #<= mylist.pop removes element at the specified index
print(mylist)

mylist.remove(9) #<= mylist.remove() removes specified element 
print(mylist)

"""" 
list functions:
    1) .append()
    2) .remove() removes specified element
    3) .pop() removes element at specified index. 
"""

""" 
mean.py

to the calculate the mean of the list, 
    1) add up all the values
    2) divide by how many things there are
    
what list function tells us how many things there are? len(<name of list>)

1) create a variable called sum = 0
2) do a for-loop over a list of numbers (this is how you add up all of the numbers)
3) make a variable called mean = sum divided by the size of the list
4) print the mean


nums = [46,92,10,98,57,12,77,99,31,19,62,41,81,40,56,97,74,13,85,16,69,32,36,27,2,24,25,71,20,4,45,84,37,86,91,75,55,67,60,1,21,100,44,70,9,94,29,26,90,82,11,66,17,47,38,42,3,43,95,6,89,87,51,28,63,23,65,22,5,61,64,58,39,30,50,72,14,59,48,76,18,53,49,96,15,34,7,78,93,83,68,79,80,33,88,35,8,73,54,52

the answer is 50.5
"""