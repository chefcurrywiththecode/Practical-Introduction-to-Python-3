""" Write a script that asks the user to input a number and then displays
that number rounded to two decimal places.  """

num1=input("Input your number: ")

print(f"{num1} rounded to 2 decimal places is {round(float(num1),2)}")

""" Write a script that asks the user to input a number and then displays
the absolute value of that number. """

num2=input("Input your number: ")

print(f"The absolute value of {num2} is {abs(float(num2))}")

""" Write a script that asks the user to input two numbers by using the
input() function twice, then display whether or not the difference
between those two number is an integer. """

num3=input("Input your number: ")

num4=input("Input your number: ")

print(f"The difference between {num3} and {num4} is an integer? {(float(num3)/float(num4)).is_integer()}!")