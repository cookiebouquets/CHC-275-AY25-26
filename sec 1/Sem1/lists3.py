""" 
lists3.py



When we think about aggregating (collect data under one title) data, so we don't typically
store all descriptive variables under one column
"""

mylist = ["John Cardinal",12,88,"CardinalJ26@chcstudent.com"]

""" 
This doesn't make sense to do because we are storing every record about the student in one list. If we
try to manipulate the list in any meaningful way we might get a type error. 

1) We can make a bunch of separate lists
2) (second semester) we can make a 2D lists
"""

names = ["John","Paul","Luke"]
gradelevels = [12,11,10]
GPAs = [90,74,65] 

""" 
A thought question is: What piece of information is shared across all three lists to make sure 
that the records corresponding to each student gets matched up with each other? 

The index logically links all of the related information together across all of the lists. 
"""

#print(f"Student records for {names[0]}. Gradelevel: {gradelevels[0]}. GPA: {GPAs[0]}")

""" 
What if I wanted to print out every single detail about a student for all students? 

is it

    -while loop
    -for each loop <= not 
    -for i loop? <= this makes the most sense because the piece we really want to iterate over 
    is the indices. 
"""

""" 
Which list goes inside len? does it even matter which list we put in? 

It doesn't really matter (as long as each list has the same size)
"""


for i in range(len(names)): #doesn't matter which list you are taking the length of 
    print(f"Student records for {names[i]}. Gradelevel: {gradelevels[i]}. GPA: {GPAs[i]}")
    


