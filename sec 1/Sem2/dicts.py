#dicts.py

""" 
We've only ever used one data structure so far:
    - A list
    - 2D list 
    
2D Lists as lists of lists. 

What uniquely determines an element in a list? If I were to get an element
from a list, what piece of information within the list identifies that object?
    - Its position (index) inside of the list

That might not be the best way to uniquely identify an object. There are other ways
to naturally order objects.

    - We can order people:
        - Birthdate (index) 
        - Class year (not necessarily an index because there's no difference within
        the groups)
        - By the order they walked in the room (which is basically another index)
        - Identify them by their names 
        
Lists in python are ordered sequences of objects and the index uniquely identifies
each object 
   
   
[1,2,3,1] 

We might want to identify things by other attributes: Dictionary 

In other languages, they might not be called dictionaries, hashmaps/hash tables

The way dictionaries work is you have a list of UNORDERED objects, and they are differentiated
by their key 

{(key:value), (key:value), (key:value)}

Objects in dictionaries are key:value pairs
"""

products = {"oranges":0, "apples":5, "pears":10, "grapes":8}
#to make a dictionary in python, you would use the curly braces at variable 
#creation

""" 
In my products dictionary, I'm going to create a bunch of key:value pairs that 
correspond to products and their quantities

when we create a dictionary, we can fill the dictionary with key:value pairs
by using <key>:<value> 

EVERY KEY REQUIRES A VALUE. How do you think I would retrieve a value from a dictionary?

I can retrieve information using the square bracket operator as usual
"""

print(f"Oranges: {products["oranges"]}")

""" 
list[index], dict["key"]

As opposed to lists where the position uniquely identifies every object, in a dictionary, it is the key that uniquely identifies
every object. 


"""

productsList = [0,5,10,8] #same values as the products dictionary
print(productsList[0]) #i don't know what this values correspond to? 

productsList.pop(0)
print(productsList[0]) #5

""" 
Using the position as a unique identifier might not be the best idea in some circumstances because what happens
when an item gets added or removed from the list? All of the positions change

if index 0 is SUPPOSED to correspond to oranges, and for some reason .pop gets called on the list, then our indices
no longer match up with our table of contents.

Dictionaries circumvent this problem by having very verbose indentifiers for objects. The existence of dictionaries
directly solves the problem from lab 2 involving banks, because in that lab we had two parallel lists, so if one list
becomes unaligned with the other, we will end up having a lot of problems. 

Rather than having two parallel lists, one for the name and one for the balance, we couldve instead had 

A SINGLE DICTIONARY, where the key was the name and value the balance


There are some rules you need to know about dictionaries (about keys):
    - what things can be keys?
        - Keys MUST be immutable: They can't change 
            - Strings
            - integer values
            - Floating point values
        - the technical reason why this is: 
            - Dictionaries are also called hashmaps, so how it works is the data is fed into a hashing function based on the key
            so if the key changes, the output of the hashing function also changes (https://en.wikipedia.org/wiki/Hash_function)
    - Can you have duplicate objects inside of a dictionary? 
        - The answer is YES for values but NO for keys
            - Having a single key map to two things breaks a certain mathematical principle about functions: 
                - This breaks the vertical line test 
                
How do we add things into a dictionary? in a list we would use .append(), but for dictionaries this wont work because
we need to also specify a key   
"""

products["bananas"] = 15
#the syntax is <nameofdict>[<new key>] = <new value> this is completely different syntax than before
print(f"bananas: {products["bananas"]}")
#what if I tried to redeclare my key and point it to a new thing
products["bananas"] = 10
print(f"bananas: {products["bananas"]}")
#because having one key mapping to two objects breaks the VLT, the natural way to deal with this kind of operation
#is to just overwrite the value at that key

""" 
Do all of my keys need to be the same data type? The answer is no,
"""

products[1] = 60
print(f"1: {products[1]}")

""" 
What happens if we print the entire dictionary? We are going to get all of the keys and their corresponding values
"""

print(products)

""" 
What about looping statements? If you know what happens you're a genius, but otherwise its fine. For looping statements over
dictionaries, there are two natural options:

1) Keys
2) Values
"""

for x in products: 
    print(products[x])
    
""" 
For loops over dictionaries explicitly returns the keys. So if I wanted the value, how would I change that print statement?
knowing that x is now a key.

Remember if you want the values out of a dictionary you need to use square brackets. for-each loops behave strangely for dictionaries

There are two helper functions baked into dictionaries that allow you to make the "shallow" copies of the values/keys

Let's say you were a teacher, and you wanted to see if a curve would dramatically affect the mean of a test 
"""

test = {"john":60,"mark":75}

""" 
test.values()
<dict.values() <- returns a list of the values inside of the dictionary
"""
average = 0
for grade in test.values():
    average += grade + 5
    
average= average/2
print(average)
print(sum(test.values())/len(test.values()))

print(test)

""" 
dict.keys() gives you the keys
"""

for name in test.keys():
    print(name)
    
""" 
What about the values? Would there be a natural restriction on values? No, anything can be a value

INCLUDING:
    - lists
    - Another dictionary
"""

testdict = {1:"hello",2:True,3:[1,2,3],4:{"foo":1,"bar":2}}

print(testdict)