
# ICS 32 - Project 2
# Hassan Khokhar 33778724 & Ara Ghiulezian 10161406

import connectfour
import Project2commonUI
import time
from colorama import *
init()




def WelcomeBanner() -> str:
    ''' Prints a welcome banner to introduce the console version of Connect Four '''
    
    print(Fore.YELLOW)
    Project2commonUI.delay_print('\n**********************************************\n')    # the following function prints the welcome banner
    Project2commonUI.delay_print('** WELCOME TO CONNECT FOUR - VERSUS MODE!!! **\n')
    Project2commonUI.delay_print('**********************************************\n')
    time.sleep(1.5)



def InputRed() -> str:
    ''' Prompts User #1 to enter a username and assigns it to Red '''

    while True:                                                                           # prompts the user to enter a username for Red
        print(Fore.WHITE)
        PlayerRed = input('Enter username (RED): ')
        if len(PlayerRed) == 0:
            print('\nEveryone has a name and so do you! Enter a username. :)\n')          # error is printed if there is no username
        else:
            return PlayerRed                                                              # returns the username for Player Red



def InputYellow() -> str:
    ''' Prompts User #2 to enter a username and assigns it to Yellow '''

    while True:                                                                           # prompts the user to enter a username for Yellow
        PlayerYellow = input('Enter username (YELLOW): ')
        if len(PlayerYellow) == 0:                                                        # error is printed if there is no username
                print('\nEveryone has a name and so do you! Enter a username. :)\n')
        else:
                return PlayerYellow                                                       # returns the username for Player Yellow



def PlayerTurn(GameState, S1: str, S2: str) -> None:
    ''' Based on the current GameState it specifies the user's turn and
    prompts instructions '''

    if GameState.turn == 1:                                                               # If it is red's turn...
            print()                                                                      
            print("User RED -- {}'s turn".format(S1))                                     # The User is prompted that it's red turn along with instructions...
            print('POP/DROP Column? (i.e.: DROP 1)')
            
    if GameState.turn == 2:                                                               # If it is yellow's turn...
            print()
            print("User YELLOW -- {}'s turn".format(S2))
            print('POP/DROP Column? (i.e.: DROP 1)')                                      # The User is prompted that it's yellow turn along with instructions...


        
def InputMove(L: list, GameState) -> None:
    ''' Given a list of the input and the current GameState this function moves
    a piece and updates the GameState of Connect Four '''
    
    if len(L) == 2:                                                                       # the following drops a piece with the function call user_move()
        if L[0] == 'DROP' or L[0] == 'POP':                                               # it is only done if 'DROP' or 'POP' are in the input
            print()
            GameState = Project2commonUI.user_move(L, GameState)         
            Board = Project2commonUI.printBoard(GameState.board)                          # Once drops it prints the board with the new piece
            return GameState
            print()
        else:
            print('\nSorry invalid input. Try again. :p\n')                               # regardless of the outcomem GameState is always returned
            return GameState
    else:
        print('\nSorry invalid input. Try again. :p\n')                                   # error message is printed if the input is wrong
        return GameState



def WinningBanner(GameState, S1: str, S2: str) -> str:
    ''' Given the GameState and the names of the users, this function determines if there
    is a winner and prints a banner with the winner's name to end the program '''
    
    if connectfour.winner(GameState) == 1:                                                # If Red wins then the winning banner for red is printed!
        time.sleep(1)
        Project2commonUI.delay_print('\n**************************************\n')
        Project2commonUI.delay_print(' Player RED -- {} has won! :D \n'.format(S1))
        Project2commonUI.delay_print('**************************************\n')
        time.sleep(2)
        return 'You may exit the program!'                                                # Returns a string to indicate exiting the program

    elif connectfour.winner(GameState) == 2:
        time.sleep(1)
        Project2commonUI.delay_print('\n**************************************\n')        # If Yellow wins then the winning banner for yellow is printed!
        Project2commonUI.delay_print(' Player YELLOW -- {} has won! :D \n'.format(S2))
        Project2commonUI.delay_print('**************************************\n')          # Returns a string to indicate exiting the program
        time.sleep(2)
        return 'You may exit the program!'



def connect_four_consoleUI():
    ''' This is the main user interface where the program is executed and the Connect Four
    game runs with all its respective functions '''
    
    WelcomeBanner()  # prints welcome banner
    print()
    PlayerRed = InputRed()       # creates player 1 - red
    PlayerYellow = InputYellow() # creates player 2 - yellow
    print()
    
    GameState = connectfour.new_game()            # starts a new game and prints an empty board
    Project2commonUI.printBoard(GameState.board)
    
    while True:
        PlayerTurn(GameState, PlayerRed, PlayerYellow)      # function call to PlayerTurn() which determines whose turn it is
        message = input()
        message = message.upper()                           # prompts for input to drop/pop a piece
            
        try:
            if len(message) == 0:                               # if there is nothing, this error is printed.
                print('\nSorry invalid input. Try again. :p\n')
            else:
                Responses = message.split()                     # otherwise the move is placed on the board and printed through InputMove()
                GameState = InputMove(Responses, GameState)
                
        except connectfour.InvalidMoveError:
            print('Invalid move! Try again. :p\n[ You can only POP your own piece or DROP a piece in an empty column! ]')  # error for invalid move
            
        except ValueError:
            print('Invalid column number! Try again. :p\n[ Number must be 1, 2, 3, 4, 5, 6, or 7! ]\n')         # error for value error - wrong col num.

        finally:
            Finale = WinningBanner(GameState, PlayerRed, PlayerYellow)        # prints the banner and returns the exit string
            if Finale == 'You may exit the program!':                         # if exit string is correct then the program breaks and ends.
                break       

if __name__ == '__main__':
    connect_four_consoleUI()


