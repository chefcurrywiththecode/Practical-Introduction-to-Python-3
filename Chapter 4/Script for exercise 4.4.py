#A script that takes input from the user and displays that input back.

prompt = "Hey, how much money do you want to make"
user_input = input(prompt)
print("You said:", user_input)

#A script that takes input from the user and displays that input back in lower case.

prompt = "What type of voices do you use in the library?"
user_input = input(prompt).lower()
print("You said:", user_input)

#A script that takes input from the user and displays the number of characters inputted.

prompt = "Write a long sentence"
user_input = len(input(prompt))
print("You wrote this many characters:", user_input)