import time
# While loops we can execute a set of statements as long as a condition is true
# keep looping and iterating until a condition is met or it comes into a BREAK statement

# SYNTAX 1
# while <condition>:
    # block

# SYNTAX 2
# while <condition>:
    # block
    # if <condition>:
        # break

counter = 0
while True:
    print(counter)
    print('Jillian')
    counter += 1
    time.sleep(2)

# while True:
#     print('WAAAHHH')
#     print(counter)
#     if counter >= 10:
#     break
#     counter += 1

while True:
    print('What is up jigglypuff?')
    user_input = input()
    if user_input == 'exit':
        break
    elif user_input == 'cute':
        print('Ahhh Jigglypuff...<3')
    else:
        print('JIGGLYPUFFFFFF!!!')

player = ''
while player != 'exit':
    player = input('K DEN. BYE')

#if input is 'exit' I want to exit
#if input is 'cute' ---> Ahhh Jigglypuff...<3
#ELSE I want to shout back JIGGLYPUFFFFFF!!!
#
# cars = ['car', 'volvo', 'skoda', 'ferari', 'lambo']
# max_length = len(cars)
#
# counter = 0
# # while counter < max_length:
# #     print(cars[counter])
# #     counter += 1
#
# while counter < max_length:
#     print(counter + 1, '-', cars[counter].capitalize())
#     counter += 1




