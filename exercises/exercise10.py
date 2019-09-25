# Story book!
# Create a dictionary with 3 stories inside! like a book :)

# each story should be it's own dictionary with:
    # beginning, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:
 # you already built a dictionary with a story
 # You already have something to prompt user for input & build dictionaries
 # Now what we want is to create a book that hold 3 stories

# extra:
 # stick it in a while loop so we continue to listen to stories :)
 # It would be nice to be able to read only one story

user_input = int(input('Choose a number 1, 2 or 3: '))
counter = 0
while user_input != int:
    if counter < user_input:
        counter += 1
        protagonist = input('Name of a boy:').capitalize()
        city = input('Enter a city:').capitalize()
        potion = input('Enter 3 ingredients:').lower()
        age = int(input('Enter a multiple of 7:'))
        if user_input == 1:
            print(f'A mad scientist named {protagonist} who lived in {city} wanted to look young forever. He made a potion out of {potion}. He drank the potion and instead, he began to age. Everytime {protagonist} would look at the mirror, his age would multiply {age} times. What a sad, sad life.')
            break
        elif user_input == 2:
            print(f'Once upon a time, a little boy named {protagonist}, found out he had teleportation powers. At the age of {age}, he teleported to {city} and decided to cook up a meal and ate {potion}')
            break
        elif user_input == 3:
            print(f'{protagonist}, a freakishly tall boy played basketball in {city}. Since he was born his mother has been preparing his meals for {age} years! This meal plan included: {potion}.')
            break
        else:
            print('Thanks for participating!')
else:
    print('Are you sure you put a number?')

dict_story = {
    'protagonist': 'Lee',
    'city': 'Tokyo',
    '3 ingredients': ['pig brain', 'salt', 'hemp'],
    'age': 4


}


