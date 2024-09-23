# Python Libraries
import os
import sys
import time

# Internal Project Files

def InputSearch():
    if (len(sys.argv) < 3):
        print(f'\nUsage: search -i [text] [pattern] [flags]')
        print('\n  NOTE: Input text must be put in quotes. Ex: "C:/Users/John Doe"')
        print('\n  Flags:')
        print('\n      Output Flags:')
        print('\n           \'/ret\' (return) ---------------- returns all instances in the text matching the pattern, each on a separate line')
        print('           \'/bool\' (boolean) -------------- returns true if some instance in text matches the pattern, otherwise returns false')
        print()  # Insert newline under final print
        sys.exit()