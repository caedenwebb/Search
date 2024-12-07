import os
import sys
import time

from ModelSearchPkg import GenerateModel

def ModelSearch():
    if (len(sys.argv) < 3):
        ModelSearchInstructions()
        exit()

    if (sys.argv[2] != 'generate' and sys.argv[2] != 'search'):
        print(f'Error: \'{sys.argv[2]}\' is not a valid argument to the Model Search Mode. Please tell the search '
              f'program whether to generate or search a model.')
        exit()

    if (sys.argv[2] == 'generate'):
        GenerateModel.GenerateModel()
        exit()

    if (sys.argv[2] == 'search'):
        pass

def ModelSearchInstructions(tab=''):
    print(f'{tab}Usage: search -m [generate/search] [arguments]')
    print(f'\n{tab}   Generate Search Models')
    print(f'{tab}        Usage: search -m generate [model type] [directory to model] [model file location]')
    print(f'\n{tab}        Model Types:')
    print(f'{tab}           1. filename---optimizes search model for searching filenames')
    print(f'{tab}           2. filesize---optimizes search model for searching filesizes')
    print(f'{tab}           3. date-created---optimizes search model for searching based on creation date')
    print(f'{tab}           4. date-modified---optimizes search model for searching based on modification date')
    print(f'\n{tab}   Searching through a Search Model')
    print(f'{tab}        Usage: search -m search [model file location]\n')