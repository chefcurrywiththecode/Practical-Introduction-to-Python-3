Animals="Animals"
Badger="Badger"
Honey_Bee="Honey Bee"
Honeybadger= "Honeybadger"

#Printing to lowercase
print(Animals.lower())
print(Badger.lower())
print(Honey_Bee.lower())
print(Honeybadger.lower())

#Printing to uppercase
print(Animals.upper())
print(Badger.upper())
print(Honey_Bee.upper())
print(Honeybadger.upper())


string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

#Strip white spaces
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())


#A script that prints out the result of .startswith("be")
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

#Making all the startswith true
print(string1.startswith("Be"))
print(string2.startswith("be"))
print(string3.startswith("BE"))
print(string4.startswith("bE"))