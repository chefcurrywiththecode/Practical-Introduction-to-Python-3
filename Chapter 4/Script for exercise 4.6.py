#Create a string containing an integer, then convert that string into an actual integer object using int().

string_int='20'

int_string=int(string_int)

print(int_string *1000)

#Create a string containing an integer, then convert that string into an actual floating object using int().
float_string=float(string_int)


print(float_string *1000)

#Create a string object and an integer object, then display them sideby-side with a single print statement by using the str() function.

name="Nathaniel"

age=34

print(name + str(age))

first_num=input("First number: ")
second_num=input("Second number: ")

print("The product of " + first_num + " and "  + second_num + " is" + str(int(first_num) * int(second_num)) )