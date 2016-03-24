
from pygame import *
mixer.init()
import connectfour
import Project2commonUI
import Project2console2
import Project2network
import time
import sys
import random
from threading import Thread
from colorama import *
init()


def delay_print(s):
    ''' Prints each character in a string at a delayed speed '''
    
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.0225)

def delay_print2(s):
    ''' Prints each character in a string at a delayed speed '''
    
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.008)

def MainTitle() -> str:
    ''' Prints the main title of the game! '''
    
    String1 = '            ****************************     *****            **************               '
    String2 = '           *                           *    *     *           *              *             '
    String3 = '           *     ***********     *******   *   *   *          *     *****     *            '
    String4 = '            *     *        *     *        *   * *   *         *     *    *    *            '
    String5 = '             *     *       *     *       *   *   *   *        *     *****     *            '
    String6 = '              *     *      *     *      *   *******   *       *              *             '
    String7 = '               *     *     *     *     *               *      *     *      *               '
    String8 = '   *************      *    *     *    *     *******     *     *     * *     ************   '
    String9 = '   *                  *    *     *   *     *       *     *    *     *  *               *   '
    String10 = '   ******************      *******  *******         *******   *******   ****************   '
    String11 = '  *****   ****   *    *  *    *  *****   *****  *******      ******   ****   *    *  ****  '
    String12 = ' *       *    *  * *  *  * *  *  *      *          *         *       *    *  *    *  *   * '
    String13 = ' *       *    *  *  * *  *  * *  *****  *          *         ******  *    *  *    *  ****  '
    String14 = ' *       *    *  *   **  *   **  *      *          *         *       *    *  *    *  *  *  '
    String15 = '  *****   ****   *    *  *    *  *****   *****     *         *        ****    ****   *   * '
    String16 = '   ******        ******          *****           **************        *****************   '
    String17 = '   *    *        *    *         *     *          *              *     *                *   '
    String18 = '   *    *        *    *        *   *   *         *     *****     *    *     ************   '
    String19 = '   *    *        *    *       *   * *   *        *     *    *    *     *     *             '
    String20 = '   *    *   **   *    *      *   *   *   *       *     *****     *      *     *            '
    String21 = '   *     * *  * *     *     *   *******   *      *              *        *     *           '
    String22 = '   *      *    *      *    *               *     *     *      *           *     *          '
    String23 = '   *                  *   *     *******     *    *     * *     ************      *         '
    String24 = '    *       **       *   *     *       *     *   *     *  *                      *         '
    String25 = '     *******  *******   *******         *******  *******   **********************          '

    
    MainTitle = String1 + '\n' + String2 + '\n' + String3 + '\n' + String4 + '\n' + String5 + '\n' + String6 + '\n' + String7 + '\n' + String8 + '\n' + String9 + '\n' + String10
    print(Fore.YELLOW)
    delay_print2(MainTitle)

    MainTitle2 = String11 + '\n' + String12 + '\n' + String13 + '\n' + String14 + '\n' + String15
    print(Fore.WHITE)
    delay_print2(MainTitle2)

    MainTitle3 = String16 + '\n' + String17 + '\n' + String18 + '\n' + String19 + '\n' + String20 + '\n' + String21 + '\n' + String22 + '\n' + String23 + '\n' + String24 + '\n' + String25
    print(Fore.YELLOW)
    delay_print2(MainTitle3)



def ShuffleMusic(L1: list) -> bool:
    ''' Function shuffles music within the given in-game music playlist '''
    
    random.shuffle(L1)
    print(L1)
    

    time.sleep(1.5)
    mixer.music.load(L1[0][0])
    mixer.music.play()
    time.sleep(L1[0][1])
    time.sleep(1.5)

    mixer.music.load(L1[1][0])
    mixer.music.play()
    time.sleep(L1[1][1])
    time.sleep(1.5)
    
    mixer.music.load(L1[2][0])
    mixer.music.play()
    time.sleep(L1[2][1])
    time.sleep(1.5)

    
def printBoard (board):
    ''' Function prints the connect four board '''
    print(Fore.YELLOW)
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
    ''' Given the response this 'drops' a piece on the connect four board '''
    column = int(response[1])
    column = column - 1
    return(connectfour.drop(GameState, column))

    print()


#POP
def user_pop(response, GameState):
    ''' Given the response this 'pops' a piece on the connect four board '''
    
    column = int(response[1])
    column = column - 1
    return(connectfour.pop(GameState, column))

    print()

####MOVE (WITH POP AND DROP)
def user_move(response, GameState):
    ''' Make a move on the board accordint to the input '''
    if response[0] == 'DROP':
        return user_drop(response, GameState)
        
    if response[0] == 'POP':
        return user_pop(response, GameState)

def connect_four_integratedUI():
    ''' Runs the user interface for the game by initiating each part
    of the program including text, music, etc. '''
    
    time.sleep(4)
    print()
    
    mixer.music.load('Intro.ogg')
    mixer.music.play()

    print(Fore.CYAN)        
    delay_print('    A long time ago in a galaxy far, far away...')
    time.sleep(8)
    print()
    print()
    print()
    MainTitle()
    print()
    print()
    print()
    time.sleep(20)
    mixer.music.stop()
    mixer.music.load('MainMenu.ogg')
    mixer.music.play(-1)

    L1 = [['Duel_of_the_Fates.ogg', 256], ['Farewell&Trip.ogg', 302], ['Ways_of_the_Force.ogg', 201]]
    
    while True:
        print(Fore.YELLOW)
        print('\nChoose your Game Mode or Enter \'Quit\' to exit the program...')
        print('[ Enter \'Network\' to play against the CPU & \'Versus\' for 2-on-2 battle!!! ]')
        print(Fore.CYAN + '')
        InputBox = input()
        GameMode = InputBox.upper()

        if GameMode == 'NETWORK':
            mixer.music.stop()
            mixer.music.load('Farewell&Trip.ogg')
            mixer.music.play(-1)
            time.sleep(1.5)
            Network = Project2network.connect_four_networkUI()
            
         
            
        elif GameMode == 'VERSUS':
            mixer.music.stop()
            mixer.music.load('Ways_of_the_Force.ogg')
            mixer.music.play(-1)
            time.sleep(1.5)
            print(Fore.WHITE)
            Console = Project2console2.connect_four_consoleUI()

        elif GameMode == 'QUIT':
            print(Fore.CYAN + '\nExiting program....')
            time.sleep(5.5)
            break
        else:
            print('\nWhoops. Enter a valid response again! :p ')

if __name__ == '__main__':
    connect_four_integratedUI()
