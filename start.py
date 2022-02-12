import time
import sys
import random
from pygame import mixer

def PrintText(text):
    """
    Print text in animated style in terminal.
    :param text: str
    :return: None
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def Greetings():
    """
    Greets player.
    :return: name of the player, does he want to play with O or X
    """
    mixer.init()
    mixer.music.load("audio/intro.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    print('\n\n')

    PrintText('Hello, little human....\n')
    time.sleep(0.5)
    PrintText('I have not seen humans for a long time...\n')
    time.sleep(0.5)
    PrintText('What is your name?\n')
    time.sleep(0.5)
    name = input('- My name is ')
    time.sleep(1)
    PrintText(f'Greetings, {name}\n')
    PrintText('Shall we play the game of TicTacToe?\n')
    time.sleep(0.5)
    ans =  input('- (yes/No): ')
    if ans == 'yes':
        PrintText('Good...\n')
        time.sleep(0.5)
        PrintText('Do you want to play as X or O?\n')
        time.sleep(0.5)
        char = input('- (X/O/random): ')
        if char=='random':
            char = random.choice(['X', 'O'])
            PrintText(f'The God of Random gave you {char}')
    else:
        PrintText('That is not an option...\n')
        PrintText('SIKE')
        char = 'X'

    mixer.music.stop()
    return name, char
