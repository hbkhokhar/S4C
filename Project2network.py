
# ICS 32 - Project 2
# Hassan Khokhar 33778724 & Ara Ghiulezian 10161406

import connectfour
import Project2sockethandling
import Project2commonUI
import time


def WelcomeBanner() -> str:
    ''' Prints a welcome banner to introduce the console version of Connect Four '''
    
    print()
    Project2commonUI.delay_print('\n************************************************\n')
    Project2commonUI.delay_print('*****   WELCOME TO CONNECT FOUR - NETWORK  *****\n')      # Prints the welcome message!
    Project2commonUI.delay_print('************************************************\n\n')
    time.sleep(1.5)



def read_host() -> str:
    ''' Asks the user to specify what host they'd like to connect to,
    continuing to ask until a valid answer is given.  An answer is
    considered valid when it consists of something other than just
    spaces. '''

    while True:
        host = input('Host: ').strip()                                                      # Prompts the user for a hostname to connect

        if host == '':                                                                      # empty host prompts and error message and starts over
            print('Please specify a host (either a name or an IP address)\n')
        else:
            return host                                                                     # returns the host given



def read_port() -> int:
    ''' Asks the user to specify what port they'd like to connect to,
    continuing to ask until a valid answer is given.  A port must be an
    integer between 0 and 65535. '''

    while True:
        try:
            port = int(input('Port: ').strip())                                             # Prompts the user for a hostname to connect

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535\n')                     # If invalid port number is raised, error message comes up
            else:
                return port                                                                 # returns the host given

        except ValueError:
            print('Ports must be an integer between 0 and 65535\n')                         # prints a value error with an error message if this is raised



def hello(connection: Project2sockethandling.GameConnection, name: str):
    ''' Logs a user into the game service over a previously-made connection.
    If the attempt to send text to the ConnectFour server or receive a response
    fails (or if the server sends back a response that does not conform to
    the game protocol), an exception is raised. '''

    Project2sockethandling.send_message(connection, 'I32CFSP_HELLO ' + name)                # Sends the message to the server to establishes its protocol and begin the connection

    response = Project2sockethandling.receive_response(connection)
    return



def username() -> str:
    ''' Ask the user to submit a username to be used during the course of the game. '''
        
    while True:                                                                             # prompts the username
        username = input('Username: ')
        if ' ' in username:                                                               
            print('Usernames can\'t include SPACES or TABS\n')                              # error is raised if there is a space in the username given
        elif '\t' in username:
            print('Usernames can\'t include SPACES or TABS\n')                              # error is raised if there is a \t in the username given
        elif len(username) == 0:
            print('Everyone has a name and so do you! Type in a username. :)\n')            # error is raised if there is nothing in the username given
        else:
            return username                                                                 # returns the username



def read_message() -> str:
    ''' Asks the user what message they'd like to send to the server.
    Any message is legitimate, including the empty string, so no validation
    is done, but this function still serves the purpose of encapsulating
    our decision about how to prompt the user. '''

    return input('USER: ')                                                                  # prompts the user for a DROP or POP (reads the user input)



def print_response(response: str) -> None:
    '''
    Prints the response sent back from the game server, along with an
    appropriate prompt.
    '''

    print('SERVER: ' + response)                                                            # prints the response after the program executes InitiateGame



def InitiateGame(connection) -> str:
    ''' Initiates the game when the user prompts the keyword and the
    server prints a response and returns the username back to the UI '''

    name = username()                                                                                     # prompts the username
    hello(connection, name)                                                                               # Sends the message to the server to establish a username with the given connection
    print('\nHello {}! If you would like to start a game print: AI_GAME (case sensitive).'.format(name))  # Prompts the user to initiate game with given keyword sent to server
    AI_GAME = 'AI_GAME\r\n'                                                                               # Server is sent this...

    message = read_message()                                                                              # The following reads the message and the server catches it and prints that it is ready to start Connect Four!
    Project2sockethandling.send_message(connection, message)           
    response = Project2sockethandling.receive_response(connection)     
    print()
    print_response(response)                    
    print()
    return name



def PlayerTurn(GameState, S1: str) -> bool:
    ''' Based on the current GameState it specifies the user's turn and
    prompts instructions '''

    if GameState.turn == 1:                                                 # Returns a string specifying instructions to Pop or Drop
            print()
            print("User RED -- {}'s turn".format(S1))
            print('POP/DROP Column? (i.e.: DROP 1)')
            return True                                                     # Returns a boolean at the end of the function
    else:
        return False

def ServerTurn(connection) -> list:
    ''' Specifies that its the Server's Turn and returns the response recieved by
    the Server after the Client makes a move '''
    
    print("\nUSER YELLOW -- CPU's turn...\n")                               # Prints that the server has its turn and is thinking and going to drop a piece
    time.sleep(2)
    answer = Project2sockethandling.receive_response(connection)                       
    print(answer)                                                           # responds by printing answer after socket recieves reponse
    response = answer.split()
    return response                                                         # response is returned



def ClientInputMove(L: list, GameState) -> None:
    ''' Given a list of the input and the current GameState this function moves
    a Client's piece and updates the GameState of Connect Four '''
    
    if L[0] == 'DROP' or L[0] == 'POP':                                     # The following is an 'if' statement that takes a Client input and calls user_move to do the
        print()                                                             # appropriate action to make a move and returns the updated GameState regardless of the input
        GameState = Project2commonUI.user_move(L, GameState)
        Board = Project2commonUI.printBoard(GameState.board)
        return GameState
        print()
    else:
        return GameState


                    
def ServerResponse(L: list, connection) -> list:
    ''' Given a list and a connection it returns the response after the server
    recieves it and after the ClientInputMove executes '''
    
    if L[0] == 'OKAY' or L[0] == 'READY':                                  # Given a list of input it prints the answer from the response recieved by server
        answer = Project2sockethandling.receive_response(connection)       # if equals 'OKAY' or 'READY'                        
        time.sleep(0)
        print(answer)
        time.sleep(0)
        response = answer.split()
        return response                                                    # returns the response



def ServerReady(L: list) -> None:
    ''' Given a list of reponses it prints that the server is 'READY' or the
    winner before printing it moves on the board  '''
    
    if L[0] == 'READY' or L[0] == 'WINNER_YELLOW':                        # prints that the server is ready to begin its move given a list of responses
        print(L[0])
        print()


    
def InvalidMovePrint(L: list, connection) -> list:
    ''' If an exception is raised due to invalid move, given a list of input
    and a connection it prints 'Invalid' and an error message '''
    
    if L[0] == 'INVALID':                                                                                    # Given a list of responses if the element is an invalid move....
        print(L[0])
        print('Rules:\nYou can only POP your own piece!\nYou can only DROP a piece in an empty column!')     # print 'invalid' and error message
        answer = Project2sockethandling.receive_response(connection)
        response = answer.split()                                                                            # once the response is recieved it returns the split list
        return response



def InvalidValuePrint(L: list, connection) -> list:
    ''' If an exception is raised due to invalid column value, given a list of input
    and a connection it prints 'Invalid' and an error message '''
    
    if L[0] == 'INVALID':                                                                                    # Given a list of responses if the element is an invalid move....
        print(L[0])                
        print('Invalid column number; Try again.\nNumber must be 1, 2, 3, 4, 5, 6, or 7!')                   # print 'invalid' and error message
        answer = Project2sockethandling.receive_response(connection)
        response = answer.split()                                                                            # once the response is recieved it returns the split list
        return response




    
def connect_four_networkUI() -> None:
    ''' Acts as a user interface which runs the entire Connect Four game
    and its respective functions '''
    
    WelcomeBanner()        # prints welcome banner!
    host = read_host()     # prompts for host
    port = read_port()     # promps for port

    print('\nConnecting to {} (port {})...'.format(host, port))    # prints that its attempting to connect to the server
    time.sleep(2)

    connection = Project2sockethandling.connect(host, port)        # function used to connect to server with given host & port
    print('Connected!')                                            # prints 'Connected' if successful
    time.sleep(1)
    
    name = InitiateGame(connection)                                # calls to InitiateGame() which prompts user to enter AI_GAME to initiate system
    GameState = connectfour.new_game()
    Project2commonUI.printBoard(GameState.board)                   # Once done, this initializes new game and prints the empty board

    while True:
        
       while True:
            if PlayerTurn(GameState, name) == True:                # Calls to function PlayerTurn() which checks if it is User's Turn
                message = read_message()                           # If so, the following prompts the user to drop or pop a piece
                message = message.upper()            
                response = message.split()

                if len(response)== 2:                                    # if the response given is a list of 2 elements, the following executes...
                    if response[0] == 'DROP' or response[0] == 'POP':         # if drop or pop is in the input then the client sends a message to the server of the placement
                        if response[1] in response:                    
                            if response[1] in ['1','2','3','4','5','6','7']:
                                Project2sockethandling.send_message(connection, message)
                            else:
                                print('\nInvalid column number; Try again.\nNumber must be 1, 2, 3, 4, 5, 6, or 7!\n')  # if its invalid its prints this message
                                break                                                                                   # breaks out of this while loop
                else:
                    print('\nSorry invalid input; try again\n')  # if its empty its prints this error message
                    break                                        # breaks out of this while loop
                                                                                        
            if GameState.turn == 2:                               # if it is the computer's turn the function call ServerTurn() is made to print that the server is going to make a move
                response = ServerTurn(connection)
                
            try:
                GameState = ClientInputMove(response, GameState)    # This function ClientInputMove() updates the GameState with the server's move
                response = ServerResponse(response, connection)     # This function ServerResponse() prints the server's response after the move is made
                
                if type(response) == list:                          # If type of response is list, this executes...
                    
                    if response[0] == 'DROP' or response[0] == 'POP':                 #  The following executes if 'DROP' or 'POP' is in input
                        GameState = Project2commonUI.user_move(response, GameState)   # Updates the server with the new move
                        answer = Project2sockethandling.receive_response(connection)
                        response = answer.split()
                        time.sleep(1)
                        ServerReady(response)                                         # Prints that the server is ready after move is placed
                        time.sleep(1)
                        Project2commonUI.printBoard(GameState.board)                  # prints the board with the server's move placed
                        print()
                        
                                                                                      ### for invalid move
            except connectfour.InvalidMoveError:
                answer = Project2sockethandling.receive_response(connection)          # Once the response is recieved, the function call InvalidMovePrint() is made...
                response = answer.split()
                Result = InvalidMovePrint(response, connection)                       # ... if the move made previously brings up this type of exception
                if type(Result) == list:
                    ServerReady(Result)                                               # it then prints that the server is ready for the next action
                    
            except ValueError:                          ### for column numbers
                answer = Project2sockethandling.receive_response(connection)          # Once the response is recieved, the function call InvalidValuePrint() is made...
                response = answer.split()
                

                Result = InvalidValuePrint(response, connection)                      # ... if the move made previously brings up this type of exception
                if type(Result) == list:
                    ServerReady(Result)                                               # it then prints that the server is ready for the next action

            finally:

                if connectfour.winner(GameState) == 1:
                    answer = Project2sockethandling.receive_response(connection)      # Once everything is done, a winner is determined...
                    response = answer.split()
                    if response[0] == 'WINNER_RED':                                   # if the winner is red (the user) it prints out the banner that they won!
                        time.sleep(1.5)
                        print('\n*****************************************\n')
                        print('** Player RED -- {} has won! :D **\n'.format(name))
                        print('*****************************************\n')
                        time.sleep(2)
                        return False                                                  # return false breaks out of the while loops and closes the connection and program

                if connectfour.winner(GameState) == 2:                                
                    print()
                    if response[0] == 'WINNER_YELLOW':
                        time.sleep(1.5)
                        print('\n*************************************\n')
                        print('** Player YELLOW -- AI has won! :( **\n')                    # if the winner is yellow (the server) it prints out the banner that they won!
                        print('*************************************\n')
                        time.sleep(2)
                        return False                                                  # return false breaks out of the while loops and closes the connection and program
    pass

        


        



# When we run this module, it calls our user interface and executes the program.

if __name__ == '__main__':
    connect_four_networkUI()
