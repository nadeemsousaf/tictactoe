#start of function

def tictactoe():
    empty = ' '

    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']

    board = [row1,row2,row3]

    l = 'lost'
    w = 'won'
    t = 'tied'

    print('=======================')
    print('      TIC TAC TOE      ')
    print('    the game begins... ')
    print('=======================')
    print('*enter y to yield game*')
    print('=======================')
    print('------1----2----3------')
    print('=======================')
    print('1--',board[0],'--')
    print('2--',board[1],'--')
    print('3--',board[2],'--')
    print('=======================')

    player = 'x' #user goes first
    outcome = l
    while True:
        check = 0
        for row in board:
            if empty in row:
                check = check + 1
            else:
                continue
        if check > 0: #available moves
            if player=='x': #if player user
                print('Your move.')
                row = input('Enter row #: ')
                if row != '1' and row != '2' and row != '3':
                    if row == 'y':
                        outcome = l
                        break
                    elif row == 'Q':
                        print('End Game.')
                        exit()
                    print('Invalid entry, try again.')
                    continue
                else: #spending time here- column now
                    r = int(row)-1 #row index
                    col = input('Enter column #: ')
                    if col != '1' and col != '2' and col != '3' or board[int(row)-1][int(col)-1] != empty:
                        print('Invalid entry, try again.')
                        continue #goes back to row input
                    else:
                        c = int(col)-1 #col index #user made valid move
                        print('!Your Move!')
            else:
                done = False
                countr = -1
                for list in board:
                    if done == True:
                        break
                    countr = countr + 1
                    count = -1
                    for i in list:
                        count = count + 1
                        if i == empty:
                            list[count] = 'o'
                            print('!Opponent Move!')
                            c = count #program col index
                            r = countr #program row index
                            done = True #do not check any more rows
                            break
            board[r][c] = player #move registered on board
            #see board after move made
            print('=======================')
            print('------1----2----3------')
            print('=======================')
            print('1--',board[0],'--')
            print('2--',board[1],'--')
            print('3--',board[2],'--')
            print('=======================')
            #now we check for a win
            #were indexing now
            if board[r][0]==player and board[r][1]==player and board[r][2]==player:
                if player=='x':
                    outcome = w
                else:
                    outcome = l
                break
            elif board[0][c]==player and board[1][c]==player and board[2][c]==player:
                if player=='x':
                    outcome = w
                else:
                    outcome = l
                break
            elif board[0][0]==player and board[1][1]==player and board[2][2]==player:
                if player=='x':
                    outcome = w
                else:
                    outcome = l
                break
            elif board[0][2]==player and board[1][1]==player and board[2][0]==player:
                if player=='x':
                    outcome = w
                else:
                    outcome = l
                break
            else: #if no win, opponents turn
                if player == 'x':
                    player = 'o'
                else:
                    player = 'x'
                continue

        else: #no available moves
            outcome = t #we have a tie
            break

    print('=======================')
    print(f'You {outcome}...') #won, lost or tied
    if outcome == w:
        print('Congrats!')
    elif outcome == l:
        print('Tough luck!')
    else:
        print('Quite an even match!')
    print('=======================')
    return outcome
#end of function

tictactoe()