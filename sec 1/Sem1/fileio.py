""" 
Fileio.py


The last couple things we did: 
    1) string parsing - we took in some complicated string as a keyboard input and manipulated it so that it is in a format we like
    2) Try-except - allow us to gracefully handle runtime errors
    
These two things naturally lead into File input/output 

File input/output - the act of reading and writing existing information into a file that exists outside our .py file. 
                  - Reading/Writing save data into a memory card. 
                  
Most files are just raw text with some structural overhead associated with them
    - .docx <= microsoft word files are just textfiles that have word formatting attached to them 
    - .csvs/xlsx <= spreadsheets which are just text files where each cell is separated by commas and newlines
    - .txts <= just text files
    - .jsons <= formatted text files 
    
When we read in data from a file, we are expecting just raw string data to come in. 


to open a file, we need to make a file object
"""

file = open("names.txt","r") #the parameters are filename,mode 
                             #r = read mode, w = write mode, x = overwrite 

""" 
How open works: It stores all of the contents of the file inside of the computer's ram. And we call storing that data in the ram
as being buffered or "input stream" 
"""

buffer = file.readlines() #read the buffer into a list
print(buffer) #print it
file.close() #close the file

""" 
You need to cd into the directory where your file lives

cd notes
cd cycle 5

\
What the hell is that \n? 

\n is an example of a escape sequence. Whenever you make a new line in any text document, you are implicitly adding a \n
to the end of that line. \n corresponds to new line

There are a bunch of characters that are reserved in python that you probably want to be able to type inside of a string

I saved my data inside of a list called buffer because it's unstructured data. We need to preprocess this data so that it is 
actually useful. 
"""

#Start preprocessing my data

names =  []
grades = [] #make empty lists
for line in buffer:
    line = line.strip() #Removing all excess whitespace, still good because we want to remove \n
    line = line.split(",") #split our line by the comma 
    #line is now a list of two objects where line[0] is the name, line[1] is the grade
    names.append(line[0])
    line[1] = int(line[1])
    grades.append(line[1])

#there is a string function that takes a string and splits it into a list of substrings based on 
#some separator we specify 
#what are the possible indices of a list with two objects? 
#how do i typecast line[1] into an integer? 
print(names) 
print(grades)
""" 
The routine for reading in data from a file:
    1) we create an empty list called buffer
    2) we create a file object and readlines() into buffer
    3) we preprocess the data and put the processed data inside the appropriate variables at the end. 
    
Now on the right, my names.txt is formatted:
    name,GPA
    name,GPA
    name,GPA

This is a common way of storing information: this is how .csvs are stored. 

Our goal for preproccessing:
    2 lists: Names and Grades
    Data type for Name: String
    Data type for Grade: int
    
we want to preprocess 'John,98\n' -> John 98  


Basically the routine is 
    1) Open your file, load the data into a buffer
    2) You parse your buffer using some preprocess routine (dependent on the data of the file)
    3) Then you use the data for the program
    4) How do we save the result of our program back into the file? 
    
We need to be careful when we save our data back into the file because it needs to be in the format that 
our preprocessor likes. Effectively, saving our data needs to be the functional inverse of our preprocessing step 
"""



#you need to be careful with write mode
line = "hello world"
#file.write(line) #maybe we expect this to be appended to the end of the file


""" 
We need to be careful with write mode because our contents get overwritten
entirely as a result of opening in write mode 

What format should my lines be when we feed it back into names.txt?

"{name},{grade}\n" <= this is the structure of our file so we need to construct our line accordingly.


1) I know that the lists are parallel, for-i is probably useful here
2) I'll need to use fstrings in order to place our variables into the line
"""


#names.append("Oden")
#grades.append(21) #This record was not previously in our file



file = open("names.txt","w") #w is write mode 
buffer =[]
for i in range(len(names)):
    line = f"{names[i]},{grades[i]}\n" #I need to put in the new line escape sequence at the end
    buffer.append(line)
  
#how do i get the last element of buffer? 
#I can do it two ways: -1 or I can do len(buffer) -1

buffer[-1] = buffer[-1].strip()

file.writelines(buffer)
file.close()


""" 
Having to write an entire post processing routine for a file we know exists kinda sucks. We are introducing a 
large amount of risk because leaving a file open is inherently unsafe. Leaving something open while you're writing
to the disk is unsafe because of potential outages, crashes, etc. 

r = read mode
w = write mode
a = append mode
"""

try:
    name = input("Enter your name: ").strip()
    grade = input("Enter your grade: ")
    grade = int(grade)
except Exception as e:
    print(e)
else: 
    file = open("names.txt","a")
    line = f"\n{name},{grade}" #I'm putting a newline escape sequence at the START rather the end because this is appended
    #to the end of the file
    file.write(line)
    file.close()


""" 
we know that there are three blocks for try except
    - try (which the attempts the code block below)
    - except (runs if a certain exception comes up)
    - finally (which runs no matter what)
    - else (If the try passes, run this codeblock)
    
we can open a file in read mode
we can write the file in write mode
we can append to a file in append mode

what happens if I open a file in write mode that does not previously exist? 
    - python will make that file in your folder and THEN you'll be in write mode. 
    
I want to write a grade report program that outputs the average GPA into a file with the current date
"""

#This routine should create a file called nov42025, write the line specified below, and close the file
date = "Marc52026"
file = open(date,"w") #This should create a file called Nov42025
avg = sum(grades)/len(grades) #this calculates the average gpa
line = f"The average GPA on {date} is {avg}"
file.write(line)
file.close()

""" 
So now that we can read and write to a file, we are capable of saving our progress for any program 
We are also able to export information from runtime into a file for reference later.

"""