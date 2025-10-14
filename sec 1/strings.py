""" 
Strings.py

the last thing we covered before the last large assignment was lists

lists were ordered sequences of elements that are bound together under one variable name where each
element was tied to its position by its index. 

I want to cover strings in deeper detail because the data type that is returned from input() is what? 

when we take in keyboard input, it comes in a string and then we process our input to make it align
with what we're expecting it to be. 

money = input() <= this was supposed to be a numerical value and then we typecast it into its appropriate
data type. 




money = input("Enter your value: ") #just running this code block is highly unsafe. 
money = int(money) #If we don't a type in a number, we get a value error and our program crashes 


Any minor typo from our bank program effectively causes the program to crash 

- type error
- value error 

A large part of this unit goes into the processing stage of our keyboard input 

we call processing our strings "parsing" 

we "parse" our input.

there are some facts about strings that are supposed to be mindblowing to you: 
    -is a string an ordered sequence of elements?
    "hello" <= h comes before e and we could say that "h" was at index 0. 
    
    -strings behave very similarly to lists in python. 
    
    -strings are ordered sequences of individual characters where each character has its own index.
    
How do we traverse a list?
    - for-each loop
    - for-i loop
    - while loop
"""

mystr = "hello"
print("for each loop")
for char in mystr: #for each loop
    print(char) #Should print out every single individual character in my string
    
print("for-i loop") #For-i loop
for i in range(len(mystr)):
    print(mystr[i])
    
    
""" 
So most things that are list behaviors are also string behaviors
    - for loops work
    - len() works
    - square bracket operators work 
    
Let's talk about what kinds of annoying things can happen while our bank program is running
"""


    
""" 

You should be familiar with this design pattern at this point. 

While you're running the program, what possible annoying things could happen with this design pattern?

string equality checking is EXACT. 

"deposit" =/- " deposit" =/= "deposit " =/= "Deposit"

python has a range of functions dedicated to parsing string inputs so that keyboard input does not have
to be this exact.

the first thing we can fix is trailing and leading whitespace

" deposit" <= we can strip the whitespace before the text. 

.strip() <= will strip all leading and trailing whitespace from the string
"""

mystr = "      hello"
print(mystr)
mystr = mystr.strip() #This will remove all trailing and leading whitespace
print(mystr)


    
""" 
other things we can do with strings is chain functions together. 

chained functions evaluate left to right. 

This is already a fantastic change to our program because .strip() removes the possibility from the user
to have that very common typo. 

having a bunch of or's is not the best way to reconcile possibly pressing shift. 

two functions in python that either force the string to be entirely lowercase or force the string
to be entirely uppercase 

.lower() <= forces the string to be lowercase
.upper() <= forces the string to be uppercase
"""


mystr = "      Hello"
print(mystr)
mystr = mystr.strip().lower() #so i chained .strip and .lower together to remove whitespace
                              #and also force the string to be entirely lowercase
print(mystr)

print("1. Deposit")
print("2. Withdraw")
print("3. Transfer")
print("4. Quit")

option = input("Select your option: ").strip().lower() #input evaluates first, then strip, then lower
if option == "deposit": 
    print("Deposit sequence")
elif option == "withdraw": 
    print("withdraw sequence")
elif option == "transfer": 
    print("Transfer sequence")
elif option == "quit": 
    print("Quit sequence")
    
""" 
Just adding these two functions to our input dramatically increases the quality of our program. 
"""

print("the next error we got a lot")


""" 
we get a type error in code block above. type errors are dramatically worse than whiffing a string match
because the program halts and exits. we lose the changes we make to the state of the program when the program
halts. 

If we ran the program again we'd be back to our initial conditions. Value errors also crash the program. 
We need some way to make sure money is a numeric value before we even try to typecast. 

"""

money = input("enter value: ") #by having a typo where i include an alphabetical character, we now get an entirely different error
if money.isnumeric(): #<= this evaluates whether money is a numerical value
                      #only run the codeblock below if money is a number
    money = int(money) #we just typecast money to an integer 
    val = money + 5 #this shouldnt run because these datatypes don't match
    print(val)
else:
    print("That is not a number!")

""" 
So by wrapping our typecasting sequence inside of an if statement, we catch the possible error 
and now our program no longer halts in this scenario. 

So now we have a more sophisticated way of parsing our keyboard input rather than just praying the 
user types in the correct values. 

The concept of wrapping our typecasting inside an if-statement <= error/exception handling. 
"""