
the_board={'top_l':' ','top_m':' ','top_r':' ',
           'mid_l':' ','mid_m':' ','mid_r':' ',
            'low_l':' ','low_m':' ','low_r':' '}

def print_board(board):
    print(board['top_l'] + '|' + board['top_m'] + '|' + board['top_r'])
    print("-+-+-")
    print(board['mid_l'] + '|' + board['mid_m'] + '|' + board['mid_r'])
    print('-+-+-')
    print(board['low_l'] + '|' + board['low_m'] + '|' + board['low_r'])

turn='x'
for i in range(9):
    print_board(the_board)
    print('turn for ' + turn +'.move on which space?')
    move=input()
    the_board[move]=turn
    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'


print_board(the_board)

