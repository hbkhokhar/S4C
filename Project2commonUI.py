
from pygame import *
mixer.init()
import connectfour
import Project2commonUI
import Project2console2
import Project2network
import time
import sys
import random
from colorama import *
init()


def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.0225)

def delay_print2(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.008)

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



def ShuffleMusic() -> None:
    L1 = ['Duel_of_the_Fates.ogg', 'Farewell&Trip.ogg', 'Ways_of_the_Force.ogg']
    random.shuffle(L1)
    for x in L1:
        mixer.music.load(x)
        mixer.music.play()
        

    
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
    
    while True:
        print(Fore.YELLOW)
        print('\nChoose your Game Mode or Enter \'Quit\' to exit the program...')
        print('[ Enter \'Network\' to play against the CPU & \'Versus\' for 2-on-2 battle!!! ]')
        print(Fore.CYAN + '')
        InputBox = input()
        GameMode = InputBox.upper()

        if GameMode == 'NETWORK':
            mixer.music.stop()
            time.sleep(1.5)
            ShuffleMusic()
            print(Fore.WHITE)
            Network = Project2network.connect_four_networkUI()
            
        elif GameMode == 'VERSUS':
            mixer.music.stop()
            time.sleep(1.5)
            ShuffleMusic()
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


