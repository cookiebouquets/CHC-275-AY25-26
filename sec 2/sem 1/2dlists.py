"""
2DLists.py

In the first semester we only really dealt with one data structure: A kind of storage procedure that 
stores a bunch of variables under one name 
    - List
    
In the second semester we are going to work with two new data structures
    - 2D List
    - Dictionary 
    
Recall things about 1D Lists:
    - Mutable (they can change in length)
    - Yes 
    - How do we get single elements out of a list? square brackets
    mylist[i] <- i is an index 
    - what is the starting index of a list: 0
    - .append(val) <=adds things
    - .remove(val)
    - .pop(index)
    
2D lists are practically the same thing with one change: rather than storing individual values
inside the list, we are just storing lists inside of those lists. 
    
"""

grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

""" 
Now instead of one list containing a bunch of numbers, I have a single list, containing multiple lists
inside of it. This is a natural thing to consider 
    - Spreadsheets are laid out in this way
    - 2D games are laid out in this way 
    
to get a single value out of a 2D list
"""

print(grid[0][0]) #pulling stuff out of a 2Dlist is the same thing as pulling something out a 1D list

""" 
the syntax is grid[row][col]
"""

grid2 = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

print(grid2[1][2]) #prints 9

"""
 The way 2D lists grow is from:
 
    -top to bottom, then left to right.
    
Different than a regular coordinate plane because [0][0] is really the "origin". 

for-each loop
for-i loop
while loop

In terms of traversing a 1D list:
    1) for-each loop: easiest to use, the trade off was num is a going to be copies of the elements
    of the list, so we can't directly modify the list
    2) for-i loops: not as easy to use, but we can directly access the list so we have more flexibility
    3) while loops: have the most flexibility because our exit condition doesn't strictly involve the list
    but it's up to you to figure out what the exit conditions are. 
"""

"""nums = [1,2,3,4]

for num in nums: #this is a for each loop
    num = num + 2
print(nums) #still prints 1,2,3,4

for i in range(len(nums)): #this is a for-i loop
    nums[i] = nums[i] + 1
    
print(nums)

i = 0
while i < len(nums): #while loop
    i = i + 1
    pass"""
    
""" 
How many looping statements do we think we need fort a 2D list? 
    3? 
    2? = the justification for 2 is an outer loop that traverses the rows and an inner loop that traverses the columns
"""

for row in grid2: #this grabs every row in the grid
    for num in row: #this pulls out the numbers in an individual row
        print(num)
    
""" 
For-each loops are the most natural again. But it's not clear what exactly is happening under the hood. I need two counting variables

i,j
"""

for i in range(len(grid2)): #this is the amount of rows from 0-2
    for j in range(len(grid2[0])): #pull out any single row, in this case it doesn't matter because every row is the same 
        #size
        print(f"({i},{j}) = {grid2[i][j]}", end = " ") 
        #print statements are terminated by a \n <- which stands for new line. print also a second parameter called end which
        #just replaces the \n  
    print()
    
""" 
For nested loops, 
    i = 0,
        j = 0
        print
        j = 1
        print
        j = 2
    i = 1,
        j = 0
        print
        j = 1
        print
        j = 2
"""

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

""" 
we're going to implement tic-tac-toe over the next couple classes 

a printBoard(board) function
a placeMarker(board,player)
a checkWinner(board) 
"""


print(board)

def printBoard(board):
    """
    prints out a tictactoe board in a nice way
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|",end = "")
            print(board[i][j], end = "|")
        print()
    
printBoard(board)