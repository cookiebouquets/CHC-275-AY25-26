#Binary.py

""" 
We're going to talk about number systems, particularly Binary and Hexadecimal number
systems

Binary Numbers = Sequences of 1s and 0s. Computers are digital electronics, so 
they only really have two states that they can compute at a time, which is 
    - high = 1
    - low = 0
    
Everything we see on a computer is really some sort of representation of a string
of binary characters that gets translated into a representation we can understand.

.exe's = binary files because the binary numbers is what the computer reads to understand
instructions
    
Well, electronics typically represent current through sine waves, computers and
electronics use something called modems to interpret frequencies of analog waves
as digital signals 

Historically why do we use binary instead of literally anything else? 
    - When electronics were being developed, we could only differentiate high and 
    low signals using vacuum tubes, which are huge and loud. 
    
When I say a number is represented in a certain Base, that just means the amount
of digits you have to work with 

Base 10: 0-9 
Base 16: 0-15 (where after 9, we use letters A-F) <= Hexadecimal
Base 2: 0-1

We need to talk about how to interpret these numbers

Each position in base 10 corresponds to a power of 10

573 <= 500 + 70 + 3

3 * 10^0 = 3 * 1
7 * 10^1 = 7 * 10
5 * 10^2 = 5 * 100

So in base 10, every position in a multi-digit number corresponds to that digit 
multiplied by some power of 10.

How can we extrapolate what happens with Binary Numbers (Base 2)

1001 1101 <- 1 * a power of what? 2

0001 <= 0 * 2^3 + 0 * 2^2 + 0*2^1 + 1*2^0 = 1 * 1 = 1
0010 <= 0 + 0 + 1*2^1 + 0 = 2
0011 <= 0 + 0 + 1*2^1 + 1*2^0 = 2 + 1 = 3

Binary numbers are the sum of the "1's" in the position that corresponds to that power.

Let's try translating two numbers to binary and adding them together

5 = 4 + 1, 2^2 + 2^0
3 = 0011

5 + 3 = 8
0101 + 0011 = 1000 we know it HAS to be this, luckily binary addtion works the exact same way 
as it does in base 10

1 + 1 = 0 (but we carry over a 1 to the next place over)
1 + 0 = 1
0 + 1 = 1
0 + 0 = 0

111  
0101
0011
____
1000

How do we convert large decimals to binary? Thankfully there is an easy repeatable procedure to work this
out. We need modulus to be able to work this out. 

10 % 2 <= takes the first number, divides by the second number, and returns the remainder

10 % 2 = 5 remainder 0
5 % 2 = 2 Remainder 1
2 % 2 = 1 Remainder 0
1 % 2 = 0 Remainder 1

1010 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 
     = 8 + 0 + 2 + 0 
     = 10
     
To convert a number from Base 10 to Base 2 (decimal to binary):
    1) Take A % 2, keep in mind the quotient and remainder
    2) Take that quotient % 2, keep in the remainder
    3) Repeat 2) until you get to 1 % 2 = 0 R 1,
    4) From bottom to top, list the remainders from left to right
    
We know how to convert from Binary -> Decimal (Converting everything to powers of 2 and adding them
all up)

We know how to convert from Decimal -> Binary (By using the procedure above).

Bitwise operations: We can think of strings of binary numbers as being "registers of bits" 

1 Byte = 8 Bits

0000 0000 <= Two register of 4 Bits

They are just different ways of manipulating binary numbers that may be useful to us (primarily because
almost* every single operation that we can think of reduces to these bitwise operations)

We take two strings of binary numbers and apply the transformation to each pair of bits across binary
numbers

AND, OR <= conveniently model Boolean Logic (if-else conditions)

1 = True
0 = False 

We need truth tables: These are just dictionaries of all of the possible outputs in binary 
    - These are easy to compute because there are only 4 different ways to permute 2 binary numbers
        - 01
        - 10
        - 11
        - 00
        

AND returns 1, when both digits are on

0 AND 0 = 0
1 AND 0 = 0
0 AND 1 = 0
1 AND 1 = 1

OR returns 1 when EITHER digit is on

0 OR 0 = 0
1 OR 0 = 1
0 OR 1 = 1
1 OR 1 = 1

0110 0101 OR
0101 1010 
_________
0111 1111

Example of Bitwise AND using the same strings

0110 0101 AND
0101 1010
_________
0100 0000 <= this is the output of bitwise AND

Every single operation you can think can be represented as a sequence of ANDs and ORs (XOR) 
^ this is really what circuits are
"""