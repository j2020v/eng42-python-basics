# Assignment 1

# Use variables, print and different data types
# Ask and store the following in variables:
    # Name, last_name, age, age_of_mother, 3 skills

# name = 'Julia'
# last_name = 'Wu'
# age = 23
# age_of_mother = 52
# three_skills = ['fencing', 'problem solving', 'python']

name = input ('What is your name?   ').capitalize()
last_name = input ('What is your last name?   ').capitalize()
age = int(input ('How old are you?   '))
age_of_mother = input ('How old is your mother?     ').lower()
list_skills = input('What are your 3 main skills?'     ).capitalize()
#three_skills = input('List 3 skills?     ').lower()

# Store skills in a list
my_list = list_skills.split
print(my_list)

# skills_list = []
# skills_list.append(skill1)
# skills_list.append(skill2)
# skills_list.append(skill3)
#
# print(skill1)
# print(skill2)
# print(skill3)

# Print out the information in a formated manner
print(f'Hey there {name} {last_name}, you are {age}. Your mother is {age_of_mother} and your skills are {list_skills}')

# Calculate age difference between response and mother
difference_of_ages = (int(age_of_mother)-int(age))
print(f"So cool! The difference between you and your mother's age is {difference_of_ages} years.")


# Print each skill in a formatted way
    # Definition of 'formatted': appropriate string formating like lower case/upper case, user-friendly, or other
print(f'Amazing! Your skills are {three_skills}.')

