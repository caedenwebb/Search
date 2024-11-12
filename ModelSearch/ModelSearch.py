import os
import sys
import time

def ModelSearchInstructions(tab=''):
    print(f'{tab}Usage: search -m [generate/search] [arguments]')
    print(f'\n{tab*2}Generate Search Models')
    print(f'\n{tab*3}Usage: search -m generate [model type] [model file location]')
    print(f'\n{tab*2}Searching through a Search Model')
    print(f'\n{tab*3}Usage: search -m search [model file location] [arguments]')