from player_class import Player
from game_func import play_game
from start import Greetings, PrintText
from pygame import mixer
import time

def main():
    name, char = Greetings()
    p1 = Player(name, char == 'O', False)
    p2 = Player('Junshi', char != 'O', True) # Junshi Daimyojin - japanese god of provocation.

    cont = True
    mixer.init()
    mixer.music.load("audio/fun_song.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)

    while cont:
        play_game(p1, p2)
        cont = input('Do you want to play the game again? (yes/No): ') == 'yes'
    mixer.music.stop()
    mixer.music.load("audio/dog_bass.mp3")
    mixer.music.play()
    time.sleep(4)
    PrintText(f'Bye little human {name}')

    return


if __name__ == '__main__':
    main()