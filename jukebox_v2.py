#After each time a coin is dropped into machine, a random song from the list should be played (just  print just print out the song title)
#Every song should be played only once per iteration
#After all songs from the list have been played the next iteration starts over with full original list of the songs
#The list of songs

songs_list = [
    'Onra - Tfbs Intro',
    'Malik Abdul Rahmaan - Mailbox Money [Nipsey Flip]',
    'Nekolai - No No',
    'Paal Singh - Huffr',
    'Middleeast - Devil In You',
    'Mr. Hong - Roses (Feat. Dvdkm And Christine Kim)',
    'Cam Matthews - Lykme',
    'Ercentius - Awake (%Ercentius)',
    'Low Key - The Gloves',
    'Co$Mo_✿ - I Want To Be Loved.',
]

import random

active = True
while active:
    if active == True:
        random.shuffle(songs_list)
        for song in songs_list:
            print("Опустите монетку для проигрывания трека:")
            mes = input()
            if mes == 'coin':
                print(song)
            else:
                active = False
                break