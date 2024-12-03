import os
import time
import sys

def SearchSessionMain():

    # Create search model of a directory to search


    # Mainloop
    while(True):
        # Get userinput
        userInput = input('Search>')
        if (userInput.split(' ')[0] == 'exit' or userInput.split(' ')[0] == 'quit' or userInput.split(' ')[0] == 'q' or userInput.split(' ')[0] == 'e'):
            break
        elif (userInput.split(' ')[0] == 'help' or userInput.split(' ')[0] == 'h'):
            HelpMenu()
        elif (userInput.split(' ')[0] == 'search'):
            pass
        elif (userInput.split(' ')[0] == 'regenerate'):
            pass
        elif (userInput.split(' ')[0] == 'clear'):
            if (os.name == 'nt'):
                os.system('cls')
            else:
                os.system('clear')
        else:
            print(f'Error: \'{userInput.split(' ')[0]}\' is not a recognized command.')

def HelpMenu():
    print('Search Session Commands:')
    print('   \'help\' (\'h\') ------------------------------------- Help menu')
    print('   \'exit\' (\'e\', \'quit\', \'q\') -------------------- Quit')
    print('   \'search\' ------------------------------------------- Execute a search query')
    print('   \'regenerate\' --------------------------------------- Regenerate the search model')
    print('   \'clear\' -------------------------------------------- Clear screen')