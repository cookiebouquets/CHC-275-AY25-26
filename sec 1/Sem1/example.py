file = open("days.txt","r")
buffer = file.readlines() #<= this gives a list
file.close()
print(buffer)
print(buffer[0])
msft = buffer[0] #just assign the stock ticker to the line that corresponds to it in the buffer