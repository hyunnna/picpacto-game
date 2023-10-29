# %%
the_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
}


# %%
def print_board(board):
    top_list = []
    mid_list = []
    low_list = []
    for k, v in board.items():
        if 'top' in k:
            top_list.append(v)
        if 'mid' in k:
            mid_list.append(v)
        if 'low' in k:
            low_list.append(v)

    top_str = '|'.join(top_list)
    mid_str = '|'.join(mid_list)
    low_str = '|'.join(low_list)

    print("{}\n-+-+-\n{}\n-+-+-\n{}".format(top_str, mid_str, low_str))


#    print("{}|{}|{}".format(board['top-L'], board['top-M'], board['top-R']))
#    print("-+-+-")
#    print("{}|{}|{}".format(board['mid-L'], board['mid-M'], board['mid-R']))
#    print("-+-+-")
#    print("{}|{}|{}".format(board['low-L'], board['low-M'], board['low-R']))

# print_board(the_board)

# %%
import re
import random, time

turn = 'X'
board_location = list(the_board.keys())
digit_check = re.compile('^[1-9]{1}$')


# for i in range(9):
while True:
    if ' ' not in list(the_board.values()):
        break

    print_board(the_board)

    if turn == 'O':  # pc
        print('Turn for %s . computer!!' % turn)
        time.sleep(2)
        l = [bl for bl in board_location if bl != '']
        key_move = random.choice(l)
        move = board_location.index(key_move)
    else:  # human
        print('Turn for %s . Move on which space?' % turn)
        move = input()

        if not digit_check.match(move):
            print('input again!! (1-9)')
            continue

        move = int(move) - 1
        key_move = board_location[move]
        #if the_board[key_move] != ' ':
        if key_move == '':
            print('input again!!')
            continue

    the_board[key_move] = turn
    board_location[move] = ''
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)
