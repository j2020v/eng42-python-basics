# Control Flow - If statements
# Controls where the code is going to go
# Depending on the result of the evaluations that return True or False, it runs a block of code or not.

# SYNTAX
# if <condition>:
    # block
# elif <condition>:
    # block
    # do stuff
# else:
    # block

# weather = 'snowy, rainy and stormy'
#
# if ('rainy' in weather) and ('stormy' in weather):
#     print('stay home')
# elif weather == 'rainy':
#     print('take an umbrella')
# elif weather == 'snowie':
#     print('wear boots and scarf')
# else:
#     print('take shades')

# - You can vote and drive
# - You can vote
# - You can driver
# - You can't legally drink'
# - You're too young, go back to school'

age = 15
driver_license = True

if (age >=18) and (driver_license == True):
    print("You are allowed to vote, drive and drink!")
elif (age < 16) and (driver_license == True):
    print("You cannot vote and drive. You can't legally drink but your uncle might have your back.")
# else: (age >=18 ) and (driver_license == False)
# print("You are allowed to vote, and drink but you are not allowed to drive.")
