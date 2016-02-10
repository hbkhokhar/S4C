import connectfour
import Project2commonUI
import Project2console2
import Project2network
import time
import sys

print('Hello')
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0)

def printBoard (board):

    Result = ('  '.join(map(lambda x: str(x + 1), range(connectfour.BOARD_COLUMNS))))
    delay_print(Result)
    print()
    
    for y in range(connectfour.BOARD_ROWS):
        moves = ''
        for x in range(connectfour.BOARD_COLUMNS):
            if board[x][y] == 0:
                moves += '.'
            elif board[x][y] == 1:
                moves += 'R'
            elif board[x][y] == 2:
                moves += 'Y'
          
        Result2 = '  '.join(moves)
        delay_print(Result2)
        print()

#DROP
def user_drop(response, GameState):
    column = int(response[1])
    column = column - 1
    return(connectfour.drop(GameState, column))

    print()


#POP
def user_pop(response, GameState):
    column = int(response[1])
    column = column - 1
    return(connectfour.pop(GameState, column))

    print()
####MOVE (WITH POP AND DROP)
def user_move(response, GameState):
    if response[0] == 'DROP':
        return user_drop(response, GameState)
        
    if response[0] == 'POP':
        return user_pop(response, GameState)

def connect_four_integratedUI():
    time.sleep(0)
    print()
    
    delay_print('\n**********************************************\n')
    delay_print('********  WELCOME TO CONNECT FOUR!!!  ********\n')
    delay_print('**********************************************\n')
    time.sleep(0)

    while True:
        
        print('\nChoose your Game Mode or Enter \'Quit\' to exit the program...')
        print('[ Enter \'Network\' to play against the CPU & \'Versus\' for 2-on-2 battle!!! ]')
        
        InputBox = input()
        GameMode = InputBox.upper()

        if GameMode == 'NETWORK':
            Network = Project2network.connect_four_networkUI()
            
        elif GameMode == 'VERSUS':
            Console = Project2console2.connect_four_consoleUI()

        elif GameMode == 'QUIT':
            break
        else:
            print('\nWhoops. Enter a valid response again! :p ')

if __name__ == '__main__':
    connect_four_integratedUI()
