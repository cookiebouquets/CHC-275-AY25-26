word = input("enter a word").lower().strip().split()
word = "".join(word)
word = list(word)
reverse = (list(reversed(word)))
print(word == reverse)


print("A"* 8)