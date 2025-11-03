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