import os
import sys
import SearchName
import SearchFileSize
import time
import Modes

def main():

    # When input is either: "search" or "python search.py"
    if (len(sys.argv) < 2):
        print('\nUsage: search [search mode] [arguments]') # [directory/file] [attribute] [pattern]
        '''print('\nData Attributes to Search:')
        print('filename ------------------ returns files and directories containing the given pattern in their filenames')
        print('file-size ------------------ returns files and directories matching the size range provided in the pattern for their filesize')
        print('date-created --------------- returns files and directories matching the date range provided in the pattern for their creation dates')
        print('date-modified -------------- returns files and directories matching the date range provided in the pattern for their modification dates\n')'''

        print('\nSearch Modes:')
        print('-a Attribute mode ---------- Searches the attributes of files and directories within a directory for a specific pattern')
        print('-f File content mode ------- Searches the content of a file for a given pattern')
        print('-d Directory contents mode - Searches the contents of a directory (that is, the contents of its files and directories) for a given pattern')
        print('-i Input mode -------------- Searches input text for a given pattern')

    # Determine the search mode

    # Attribute Mode
    if (sys.argv[1] == '-a'):
        Modes.AttributeMode()
    # File Content Mode
    elif (sys.argv[1] == '-f'):
        Modes.FileContentMode()
    # Directory Content Mode
    elif (sys.argv[1] == '-d'):
        Modes.DirectoryContentMode()
    # Input Mode
    elif (sys.argv[1] == '-i'):
        Modes.InputMode()
    # Invalid Mode
    else:
        print(f"Error: Invalid mode: '{sys.argv[1]}'")


if __name__ == "__main__":
    main()