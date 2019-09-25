# Assignment 2

# Define an empty dictionary name_dictionary = {}
# Prompt user for input for a story. It should have:
    # hero, beginning, middle and end
    # Add each response to the dictionary under an appropriate key
    # 2 other things you define to be part of the story

protagonist = input('Name of a girl:').capitalize()
location = input('Your favorite place:').capitalize()
flower = input('Your favorite flowers:')
smell = input('A nasty smell:')
sound = input('Onomatopoeia:').lower()
creature = input('An animal you fear of:')

dict_story1 = {
    'start': 'There was once a little girl named {protagonist}. Everyday, without a fail she would visit her grandmother who lived in {location}',
    'middle': "Her grandmother's house would always smell of freshly picked {flower} until today... It smelt like {smell}. She followed the smell and it led her to the basement. {protagonist} heard a noise {sound}.",
    'end': 'She turned around and saw a {creature} eating what is left of her grandmother.'
}

dict_story2 = {
    'start': 'Once upon a time, a little boy named {protagonist}, found out he had teleportation powers.',
    'middle': 'At the age of {age}, he teleported to {city}.',
    'end': 'He was extremely hungry and decided to cook up a meal. So he ate {portion}.'

dict_story3 = {
    'start': '{protagonist}, a freakishly tall boy played basketball in {city}.',
    'middle': 'Since he was born his mother has been preparing his meals for {age} years!',
    'end': 'This meal plan included: {potion}.'
}
}
print(f"There was once a little girl named {dict_story1[protagonist]}. Everyday, without a fail she would visit her grandmother who lived in {dict_story1[location]}. Her grandmother's house would always smell of freshly picked {dict_story1[flower]} until today... It smelt like {dict_story1[smell]}. She followed the smell and it led her to the basement. {dict_story1[protagonist]} heard a noise {dict_story1[sound]}. She turned around and saw a {dict_story1[creature]} eating what's left of her grandmother.")

dict_story1 = {
     'protagonist': 'Lucy',
     'location': 'Cape Town',
     'flower': 'sunflowers',
     'smell': 'penguin',
     'sound': 'BAAAAAANNGGG!',
     'creature': 'crocodile'

# Print out a the dictionary information in an ordered way so we can read the story.
# SYNTAX dict_name = {'example_key': 'value', 'example_key': 'value'}

# protagonist = input('Name of a girl:').capitalize()
# location = input('Your favorite place:').capitalize()
# flower = input('Your favorite flowers:')
# smell = input('A nasty smell:')
# sound = input('Onomatopoeia:').lower()
# creature = input('An animal you fear of:')
#
# dict_story1 = {
#     'protagonist': 'Lucy',
#     'location': 'Cape Town',
#     'flower': 'sunflowers',
#     'smell': 'penguin',
#     'sound': 'BAAAAAANNGGG!',
#     'creature': 'crocodile'
# }
#
# print(f"There was once a little girl named {protagonist}. Everyday, without a fail she would visit her grandmother who lived in {location}. Her grandmother's house would always smell of freshly picked {flower} until today... It smelt like {smell}. She followed the smell and it led her to the basement. {protagonist} heard a noise {sound}. She turned around and saw a {creature} eating what's left of her grandmother.")

# teeth = input('brush or lick?')
# shower = input('jump or hop?')
# temp = input('hot or cold?')
# breakfast = input('porridge or pancakes?')
# drink = input('orange or apple?')
# face = input('eyebrows or lips?')
# bag = input('notebook or laptop?')
#
# print(f"I wake up {teeth} my teeth clean, {shower} in the shower and make sure the water is {temp}. For breakfast I have {breakfast} and drink a glass of {drink} juice. I paint my face, fill in my {face} and put on my lipstick. I pack my lunch and make sure my {bag} is in my bag. I am ready for school!")
#
# dict_story3 = {
#     'teeth': 'brush',
#     'shower': 'hop',
#     'temp': 'hot',
#     'breakfast': 'porridge',
#     'drink': 'orange',
#     'face': 'eyebrows',
#     'bag': 'laptop'
# }