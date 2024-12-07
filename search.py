# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchName
import SearchFileSize
import AttributeSearch


def main():

    # When input is either: "search" or "python search.py"
    if (len(sys.argv) < 2):
        print(f'\nUsage: {sys.argv[0]} [mode] [arguments]') # [directory/file] [attribute] [pattern]
        print('\n  Modes:')
        print('    \'-a\' Attribute search mode ---------- Searches the attributes of files and directories within a directory for a specific pattern')
        print('    \'-s\' Search session mode ------------ Opens a search session which can be used to search through a model of a directory based on file-size, date-created, and date-modified')
        print('')
        print('\tATTRIBUTE SEARCHES MODE:')
        AttributeSearch.AttributeSearchInstructions('\t')
        print()
        sys.exit()

    # Determine the search mode
    # Attribute Mode
    if (sys.argv[1] == '-a'):
        AttributeSearch.AttributeSearch()
    # Invalid Mode
    else:
        print(f"Error: Invalid mode: '{sys.argv[1]}'")


if __name__ == "__main__":
    main()