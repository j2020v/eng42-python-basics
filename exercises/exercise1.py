# Define the following variables
# first_name, last_name, age, eye_color, hair_Color

first_name = 'Tracy'
last_name = 'Beaker'
age = 22
eye_color = 'Hazel'
hair_color = 'Black'

# Prompt user for input and re-assign these
name = input ('What is your name?   ').capitalize()
last_name = input ('What is your last name?   ').capitalize()
age = int(input ('How old are you?   '))
eye_color = input ('What color are your eyes?     ').lower()
hair_color = input('What color is your hair?     ').lower()

# Print them back to the user as conversation
print(f'Hey there {name} {last_name}, you are {age}. The color of your eyes are {eye_color} and the color of your hair is {hair_color}. Very nice!')
# Example: 'Hello Jack! Welcome, your age is 26, you eyes are green and your hair is black.'

# Section 2 - Calculate in what year was the person born? And respond back.
# Print something like: 'You said you we're 28 hence you were born in 1991!'
date_of_birth = (2019-int(age))
print(date_of_birth)

print(f'You said you were {age}, hence you were born in {date_of_birth}')