""" 1. Write a for loop that prints out the integers 2 through 10, each on
a new line, by using the range() function. """

for n in range(2,11):
    print (n)

""" 2. Use a while loop that prints out the integers 2 through 10 (Hint:
You’ll need to create a new integer first.) """

num=2

while num <11:
    print(num)
    num +=1

""" Write a function called doubles() that takes one number as its input
and doubles that number. Then use the doubles() function in a
loop to double the number 2 three times, displaying each result on
a separate line. """

def doubles(num):
    return num*2

dub=2

for n in range(3):
    dub=doubles(dub)
    print(dub)