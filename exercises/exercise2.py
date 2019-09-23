# Use operators
# equate something

# As a user, I want to be able to guess a number and know if I got it correct or not, so that I can know if I won or not.

# 1. We should define/assign number to a variable called magic_number
# 2. I need to ask user for input
# 3. I need to check ig this input matches a magic number
# 4. I need to let the user know if their guess was true or false 


magic_number = 30
user_input = int(input('Please enter your number:   '))

#print(magic_number == user_input)
print("Your guess was", magic_number == user_input)

