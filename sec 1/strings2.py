""" 
strings2.py


last class we really concerned ourselves with parsing string input

because keyboard input comes in as a string, we really want to be able to determine the format of the keyboard input
to avoid things like
    -value errors
    -type errors
    -random typos that cause our program to stop working
    
value and type errors cause the program to halt, our program gets reset to initial conditions <= catastrophic failure

typos from string matching <= not so bad of a failure 


.strip() <= removes all leading and trailing whitespace
.lower/.upper() <= forces the string to be entirely uppercase or lowercase
isnumeric() <= returns true if the string is a number 

in that same breath, we're going to cover a couple more string functions that help with parsing input.

"""

option = input("Enter a list of names separated by spaces")
print(option)

""" 
Sometimes keyboard input comes in a stream of data that is split by some delimiting string of character

option is a list of names that is deliminated by spaces


"""

names = option.split() #.split() defaults to white delineation, so we create a list of names based on the prompt
print(names) #So now our list of names is an actual list (in terms of python) rather than a string 

""" 
So in an applied sense how is this useful outside of this contrived example i've created? 

messages are sent over ethernet wires as bitstreams <= data streams of binary numbers 

001101101010110100100101010 

we need some way to determine when one message starts and one message ends, if you take cybersecurity essentials

messsages are bookended by what are called sentinel bit patterns

0110101 <= what determines when a message starts and stops 
"""

bitstream = "0110101Hello0110101World0110101How0110101are0110101you" 

msg = bitstream.split("0110101")
print(msg) #should be a list corresponding to each word inside my bitstream

""" 
If you ever get into socket/network programming then these concepts will definitely come up again because bitstreams
come in as a layer 2 service where each messasge is split by special bit patterns 
"""

mystr = "Hello#How#Are#You"
msg = mystr.split("#")
print(msg)

""" 
if splitting is the forward direction of decomposing strings, we probably want some way to compose strings from a list
of substrings 

.join() <= but the behavior of .join() is really weird 

<the character you want to delimit the string by>.join(<list of substrings>)
"""

space = " " #< a string with a space in it

fruits = ["apples","oranges","pears","mangoes"]

combined = space.join(fruits) 
print(combined) #a single string where each fruit is delimited by a space

""" 
.split() and .join() as functional inverses of each other 

the example above is not actually how you write something like this.

I had to create a whole variable that was just a single space <= this feels kinda stupid. 

in python, i can call functions on strings that don't have a variable name associated with it. 
"""

combined = "".join(fruits) #This is the more "natural" way to perform the same task 
print(combined) #What happens when I call .join on an empty string?

""" 
If i call .join on an empty string, then all it does is concatenate the strings together with no delineation 
"""

""" 
Recall this fact about strings
"""

sum = 5 + 4
print(sum)

str1 = "hello"
str2 = "world"
concat = str2+str1
print(concat)

""" 
string concatenation with the + is not commutative, so switching the order of addition reverses the string 
"""