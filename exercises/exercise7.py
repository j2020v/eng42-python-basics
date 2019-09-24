# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg, General viewing, but some scenes may be unsuitable for young children
  ## 12, Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15, No one younger than 15 may see a 15 film in a cinema.
  ## 18, No one younger than 18 may see an 18 film in a cinema.

film_rating = input('What is the film rating?    ').lower().strip()

if film_rating == '18':
    print('No one younger than 18 may see this film.')
elif film_rating == '15':
    print('No one younger than 15 may see this film.')
elif film_rating == '12' or film_rating == '12a':
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for children. No one younger than 12 may see a 12A film unless accompanied by an adult.')
elif film_rating == 'universal':
    print('everyone can watch this film')
elif film_rating == 'pg':
    print('general viewing but some scenes may be unsuitable for young children.')
else:
    print('Unrecognisable rating')


