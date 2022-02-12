import random
import numpy as np

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def get_action(p1, p2):
    '''
    Returns action depending on the move made by players.
    :param p1: Player class object
    :param p2: Player class object
    :return: Action (board coordinates) that player chose to carry out.
    '''
    while True:
        if p1.turn:
            action = int(input(f'{p1.name}, choose your next move. Choose wisely.\nMove: '))
        if p2.turn:
            action = int(input(f'{p2.name}, choose your next move. Choose wisely.\nMove: '))
        if board[action] == 0:
            return action
        else:
            continue


def print_board():
    '''
    Draws board brom board variable.
    0 - void
    1 - X
    2 - O
    :return: None
    '''
    chars = ['_', 'X', 'O']
    b = [chars[i] for i in board]
    print('\n\n')
    print('---------')
    print(f'| {b[0]} {b[1]} {b[2]} |\n| {b[3]} {b[4]} {b[5]} |\n| {b[6]} {b[7]} {b[8]} |')
    print('---------')


def check_winner():
    """
    Check if there is a winner (is 3 X or O in one line).
    :return: bool or 'Draw' if it is draw
    """
    # Horizontal 1
    if board[0] == board[1] and board[1] == board[2] and board[2] != 0:
        return True
    # Horizontal 2
    if board[3] == board[4] and board[4] == board[5] and board[5] != 0:
        return True
    # Horizontal 3
    if board[6] == board[7] and board[7] == board[8] and board[8] != 0:
        return True
    # Vertical 1
    if board[0] == board[3] and board[3] == board[6] and board[6] != 0:
        return True
    # Vertical 2
    if board[1] == board[4] and board[4] == board[7] and board[7] != 0:
        return True
    # Vertical 3
    if board[2] == board[5] and board[5] == board[8] and board[8] != 0:
        return True
    # Diagonal 1
    if board[0] == board[4] and board[4] == board[8] and board[8] != 0:
        return True
    # Diagonal 2
    if board[2] == board[4] and board[4] == board[6] and board[6] != 0:
        return True

    if not (0 in board):
        return 'Draw'
    return False


def EndGame(name=None, draw=False):
    """
    Shall be called when game is ended.
    Prints winning message + resets board.
    :param name: Player's name who won game
    :param draw: if there is a draw (no winner)
    :return: None
    """
    print_board()
    print('Board at the end\n')
    if not draw:
        print(f'Mighty {name} won')
    else:
        print('It was foreseen that it will be a draw...')
    global board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def state_to_num(state):
    """
    Encodes state of board to number.
    :param state: board array
    :return: number
    """
    return state[0] + 3 * state[1] + 9 * state[2] + 27 * state[3] + 81 * state[4] + 243 * state[5] + 729 * state[
        6] + 2187 * state[7] + 6561 * state[8]


def num_to_state(N):
    """
    Turns number to state of board (board array)
    :param N: number
    :return: board array
    """
    i = N // (3 ** 8)
    h = (N - i * (3 ** 8)) // (3 ** 7)
    g = (N - i * (3 ** 8) - h * (3 ** 7)) // (3 ** 6)
    f = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6)) // (3 ** 5)
    e = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6) - f * (3 ** 5)) // (3 ** 4)
    d = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6) - f * (3 ** 5) - e * (3 ** 4)) // (3 ** 3)
    c = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6) - f * (3 ** 5) - e * (3 ** 4) - d * (3 ** 3)) // (3 ** 2)
    b = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6) - f * (3 ** 5) - e * (3 ** 4) - d * (3 ** 3) - c * (3 ** 2)) // (3 ** 1)
    a = (N - i * (3 ** 8) - h * (3 ** 7) - g * (3 ** 6) - f * (3 ** 5) - e * (3 ** 4) - d * (3 ** 3) - c * (3 ** 2) - b * (3 ** 1)) // (3 ** 0)
    return ([a, b, c, d, e, f, g, h, i])

def get_action_ai(p1, p2):
    """
    Returns move that ai makes.
    :param p1:
    :param p2:
    :return:
    """
    global board
    if p1.turn:
        marker = 1
        epsilon = p1.epsilon
    else:
        marker = 2
        epsilon = p2.epsilon

    players = [p1, p2]
    possible_next_states = {}
    top_value = -1

    # Encode all possible states
    for i in range(len(board)):
        if board[i] == 0:
            state = np.copy(board)
            state[i] = marker
            state_encoded = state_to_num(state)
            possible_next_states[i] = state_encoded

    # Implementation of epsilon greedy
    if np.random.rand() < epsilon:
        if players[marker-1].epsilon > 0.05:
            players[marker-1].epsilon -= 0.001
            return random.sample(possible_next_states.keys(),1)[0]
    else:
        i = 0
        for state in possible_next_states.values():
            try:
                # Find the most beneficial state
                if players[marker-1].values(state) > top_value:
                    top_value = players[marker-1].values(state)
                    action = list(possible_next_states.keys())[i]
            except:
                pass
            i+=1

    if players[marker-1].epsilon > 0.05:
        players[marker-1].epsilon -= 0.001

    # If there was no action set, return a random action
    try:
        return action
    except:
        return random.sample(possible_next_states.keys(), 1)[0]


def play_game(p1, p2):
    """
    Main game loop.
    :param p1: Player class object
    :param p2: Player class object.
    :return: None
    """
    global board
    state_history = []
    # Main Loop
    while True:
        print_board()
        if p1.turn:
            if p1.ai:
                board[get_action_ai(p1, p2)] = 1
            else:
                board[get_action(p1, p2)] = 1
            state_history.append(state_to_num(board))

            if check_winner() == True:
                EndGame(name=p1.name)
                update_values(p1, state_history, True)
                update_values(p2, state_history)
                break

        if p2.turn:
            if p2.ai:
                board[get_action_ai(p1, p2)] = 2
            else:
                board[get_action(p1, p2)] = 2
            state_history.append(state_to_num(board))

            if check_winner() == True:
                EndGame(name=p2.name)
                update_values(p2, state_history, True)
                update_values(p1, state_history)
                break

        if check_winner() == 'Draw':
            EndGame(draw=True)
            update_values(p2, state_history)
            update_values(p1, state_history)
            break

        p1.turn = not p1.turn
        p2.turn = not p2.turn

def update_values(player, state_history, winner=False):
    """
    Updates values.
    """
    player.values[state_history[-1]] = -1
    if winner:
        player.values[state_history[-1]] = 1

    for state in state_history:
        if state not in player.values:
            player.values[state] = 0

    for i in range(len(state_history)-1, 0, -1):
        player.values[state_history[i-1]] += .1*(player.values[state_history[i]] - player.values[state_history[i-1]])