""" 
strings are lists (iterable) 

we can do for-loops over strings

for-loops pull out one character at a time 


"""
str1 = "hello"
str2 = "world"
print(str1 + str2)
print(str2 + str1)


reverse = "" #<= this is the empty string 
letter1 = "a"
letter2 = "b"



print( letter1 + letter2 + reverse) #ab
print(letter2 + letter1 + reverse) #ba 

""" 
approach 1: 


after we save the word backwards into reverse using for-loop, the empty string, and concatenation, 

all we need to do is what? we can check equality with an if-statement 

1) input your word into a variable
2) reverse the word, save it into reverse
3) check if word == reverse

approach 2: two-pointer 

we know that strings are lists: 

mylist[index] <= something like this pulls out the element of a list

racecar
r     r
 a   a
  c c
   e
   
   
what is the index of the first item in a list? 0
what is the index of the last item in a list? -1, len(list) -1


while loop and a counting variable, the counting variable corresponds to the indices of the letters
in the word

and exit the loop as soon as the word is no longer a palindrome 
"""