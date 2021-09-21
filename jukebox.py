#After each time a coin is dropped into machine, a random song from the list should be played (just  print just print out the song title)

#Every song should be played only once per iteration

#After all songs from the list have been played the next iteration starts over with full original list of the songs

#The list of songs

import random

active = True
while active:
    if active == True:
        first_step = "Будете ли вы продолжать проигрывание треков?"
        first_step += "\nЗабросьте монетку для продолжение проигрывания(coin/no): "
        def playing_songs(songs_list, new_songs_list):
            global active
            while active:
                if len(songs_list) == 0:
                    break
                message = input(first_step)
                if message == 'coin' and len(songs_list) > 0:
                        random_song = songs_list.pop(random.randrange(0, len(songs_list)))
                        print("Playing song: " + random_song)
                        new_songs_list.append(random_song)
                elif message == 'coin' and len(songs_list) == 0:
                        random_song = songs_list.pop()
                        print("Playing song: " + random_song)
                        new_songs_list.append(random_song)
                else:
                    active = False

        def new_playing_songs(new_songs_list, songs_list):
            global active
            while active:
                if len(new_songs_list) == 0:
                    break
                message = input(first_step)
                if message == 'coin' and len(new_songs_list) > 0:
                    random_song = new_songs_list.pop(random.randrange(0, len(new_songs_list)))
                    print("Playing song: " + random_song)
                    songs_list.append(random_song)
                    if len(new_songs_list) == 1:
                        random_song = songs_list.pop()
                        print("Playing song: " + random_song)
                        songs_list.append(random_song)
                elif message == 'no':
                    active = False
            if active == False:
                active = False

        songs_list = [
            '1Onra - Tfbs Intro',
            '2Malik Abdul Rahmaan - Mailbox Money [Nipsey Flip]',
            '3Nekolai - No No',
            '4Paal Singh - Huffr',
            '5Middleeast - Devil In You',
            '6Mr. Hong - Roses (Feat. Dvdkm And Christine Kim)',
            '7Cam Matthews - Lykme',
            '8Ercentius - Awake (%Ercentius)'
            '9Low Key - The Gloves',
            '10Co$Mo_✿ - I Want To Be Loved.',
        ]
        new_songs_list = []
        playing_songs(songs_list, new_songs_list)
        new_playing_songs(new_songs_list, songs_list)
    continue
