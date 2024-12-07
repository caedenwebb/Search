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
        print(f'\nUsage: {sys.argv[0]} [search type] [arguments]') # [directory/file] [attribute] [pattern]
        print('\n  Search Types:')
        print('    \'-a\' Attribute Search ---------- Searches the attributes of files and directories within a directory for a specific pattern')
        print('')
        print('\tATTRIBUTE SEARCH INSTRUCTIONS:')
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