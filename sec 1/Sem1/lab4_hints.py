""" 
Grocery Store Hints

Foods is structured exactly the same way Names.txt was during our notes for file I/O.

Second problem you're gonna have is that the foods have decimal values for their prices
"""

price1 = "4.50"
price2 = "5.75"
#How do we convert price into a number? 
price1 = float(price1) #If you don't know how to do this <- i don't know what to tell 
price2 = float(price2)
print(price1 + price2) #I got a value error

""" 
integers are whole numbers

floats take care of decimals

Sales tax: 6% we gotta multiply our total by *0.06 
"""

sub_total = 10.75 
tax = sub_total * 0.06
total = sub_total + tax
print(f"subtotal: {sub_total}")
print(f"total: {total}")

""" 
What variables should i declare as empty or zero at the top of the file:
    - total = 0 <- we're going to update this as we add things to our cart
    - foods = []
    - prices = []
    
while loop logic is required so you can keep running the program until they check out 
"""