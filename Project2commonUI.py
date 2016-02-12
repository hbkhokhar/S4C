
import pygame
import connectfour
import Project2commonUI
import Project2console2
import Project2network
import time
import sys
from colorama import *
init()


def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0)

def MainTitle() -> str: 
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
    Strign13 = ' *       *    *  *  * *  *  * *  *****  *          *         ******  *    *  *    *  ****  '
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

    
    MainTitle = Fore.YELLOW + String1 + '\n' + String2 + '\n' + String3 + '\n' + String4 + '\n' + String5 + '\n' + String6 + '\n' + String7 + '\n' + String8 + '\n' + String9 + '\n' + String10
    delay_print(MainTitle)

    MainTitle2 = Fore.WHITE + String11 + '\n' + String12 + '\n' + String13 + '\n' + String14 + '\n' + String15
    delay_print(MainTitle2)

    MainTitle3 = Fore.YELLOW + String16 + '\n' + String17 + '\n' + String18 + '\n' + String19 + '\n' + String20 + '\n' + String21 + '\n' + String22 + '\n' + String23 + '\n' + String24 + '\n' + String25
    delay_print(MainTitle3)
    
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
    
    music.mixer.load('C:\\Users\\Hassan\\UC Irvine\\ICS 32\\Project2\\StarWarsIntro.ogg')
    music.mixer.play()

    print(Fore.CYAN + '   A long time ago in a galaxy far, far away...')
    print()
    print()
    print()
    MainTitle()
    time.sleep(25)

    
    while True:

        music.mixer.stop()
        music.mixer.load('StarWarsGame.ogg')
        music.mixer.play()
        print('\nChoose your Game Mode or Enter \'Quit\' to exit the program...')
        print('[ Enter \'Network\' to play against the CPU & \'Versus\' for 2-on-2 battle!!! ]')
        
        InputBox = input()
        GameMode = InputBox.upper()

        if GameMode == 'NETWORK':
            music.mixer.stop()
            music.mixer.load('StarWarsNetwork.ogg')
            Network = Project2network.connect_four_networkUI()
            
        elif GameMode == 'VERSUS':
            music.mixer.stop()
            music.mixer.load('StarWarsVersus.ogg')
            Console = Project2console2.connect_four_consoleUI()

        elif GameMode == 'QUIT':
            break
        else:
            print('\nWhoops. Enter a valid response again! :p ')

if __name__ == '__main__':
    connect_four_integratedUI()

