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
"""