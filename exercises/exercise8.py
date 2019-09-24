# The game POP and TOC!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are POPTOC

# as a user I should be asked for a number, so that I can play the game  with my input
# as a player, I should see the game counting up to many number and so that I can see if it is working
# as a player, I should be able to exit the game using a key word, so that I can stop playing

player_input = input('Do you want to play?').capitalize()
counter = 0
while player_input != 'exit':
    number_input = int(input('Enter a number:'))
    while counter < number_input:
        counter += 1
        if counter % 3 == 0 and counter % 5 == 0:
            print('POPTOC')
        elif counter % 3 == 0:
            print('POP')
        elif counter % 5 == 0:
            print('TOC')
        else:
            print(counter)
    input_2 = input('Do you want to continue playing?')
    print(input_2)
    if input_2 != 'no':
        print('Nice one!')
    else:
        print('You have chosen to exit game.')
        break
else:
    print('You have chosen to exit game.')

