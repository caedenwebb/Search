# Python Libraries
import os
import sys
import time

# Internal Project Files

def InputSearch():
    if (len(sys.argv) < 3):
        InputSearchInstructions()
        sys.exit()

def InputSearchInstructions(tab=''):
    print(f'\n{tab}Usage: search -i [text] [pattern] [flags]')
    print(f'\n{tab}  NOTE: Input text must be put in quotes. Ex: "C:/Users/John Doe"')
    print(f'\n{tab}  Flags:')
    print(f'\n{tab}      Output Flags:')
    print(f'\n{tab}           \'/ret\' (return) ---------------- returns all instances in the text matching the pattern, each on a separate line')
    print(f'{tab}           \'/bool\' (boolean) -------------- returns true if some instance in text matches the pattern, otherwise returns false')
    print()  # Insert newline under final print