""" 
exceptionhandling.py

So october is more or less done this week, we're probably going to have 1-2 more large problem sets. 

It's time to start thinking about semester projects. Rather than having an exam in this class, we have 
a semester project instead. 
    - one of every single concept we covered so far in the year
        - while loops, for loops
        - lists
        - if-else conditionals
        - strings, inputs, typecasting, etc. 
        
    -typically people in the past have done 1 of 3 things:
        - a text based game that runs in the terminal
            - the oregon trail
        - they researched how to use some third party library in python
            - games built with pygame 
            - weather app
        - made some sort of utility program that is relevant to cyber security/computer science
            - traceroute <= very common networking diagnostic tool, he implemented it in python
              by learning how to use the request package
              
    third party packages are fair game, the importing and use of packages is incredibly easy. its easy to 
    import things like pandas, scikit-learn, tensorflow, etc. 

working in partners is ok

the last unit was spent on parsing string data, we manipulated keyboard input to make sure that the input
was valid and easy to use inside our programs
    - .lower() to make string matching easier
    - .strip() to remove whitespace
    - .isnumeric() which checks if a string has numerical values before we typecast 
    
All of these functions are relevant to the concept of exception handling


x = "some value"
x = int(x) #this is going to cause the program to crash because of a type error
print(x + 5)


we got around this by wrapping the whole thing inside of an if-statement. 

Except Handling = the method of gracefully dealing with runtime errors in our program.

It's easy to write good and complete syntax in python because its not strongly typed. It means 
I don't have to declare data types, in languages like java, the compiler needs to know the data type
of every variable at compilation time. So not having to declare data types allows for weird errors to 
happen

By design, python NEEDS to have some sort of built in feature to allow graceful exception handling 
because exceptions happen all the time. 

"""


""" 
I'm  writing a basic division program
"""


""" 
I'm going to introduce two new keywords

try: 

except: 
"""
try: 
    x = input("Enter num 1: ")
    y = input("enter num 2: ")
    x = int(x) #value error if not a number
    y = int(y)
    quotient = x/y 
    print(quotient)
    #Dividing by zero is no good. 
except ValueError: 
    print("x and y must be numbers")
except ZeroDivisionError:
    #you can catch multiple exceptions 
    print("y must be nonzero")
except TypeError:
    print("variables must be integers")
except Exception as e: 
    #capture exceptions that i'm not expecting and print that exception out
    print(e)
finally: 
    #executes codeblock no matter what
    print("Thanks for using the calculator ")
    
    
    
""" 
try: 
    code block
except <exception>: 
    code block

python attempts to execute the codeblock underneath the try keyword, and if it runs into a runtime error,
it jumps to an except codeblock 

to perform similar behavior, we would need to do a really clunky isnumeric() check before typecasting 

we can catch multiple kinds of exceptions inside one try-except code block 

what about errors that we don't expect to happen? 

try: attempts to executes the code block below, if an exception is thrown, jump to except block
except <exception>: if try fails and throws an exception, the except is matched to the corresponding except keyword and executes
that code block
finally: after all trys and excepts are executed, codeblocks after finally are executed no matter what 


What I want you to do: 
    - Rewrite four function calculator, but have every arithmetic operation in a try-except block to make sure
    we don't have runtime errors
    
    
to install packages:

python3 -m pip install <packagename>
"""
