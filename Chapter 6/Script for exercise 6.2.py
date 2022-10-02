""" Write a function called cube() with one number parameter and returns
the value of that number raised to the third power. Test the
function by displaying the result of calling your cube() function on
a few different numbers. """

def cube(num):
    return num**3

print(cube(2))
print(cube(3))
print(cube(4))

""" Write a function called greet() that takes one string parameter
called name and displays the text "Hello <name>!", where <name> is
replaced with the value of the name parameter. """

def greet(name):
    print("Hello {0}".format(name))

greet('Natty')
