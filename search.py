# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchName
import SearchFileSize
import AttributeSearch
import FileContentSearch
import InputSearch

# External Libraries


def main():

    # When input is either: "search" or "python search.py"
    if (len(sys.argv) < 2):
        print('\nUsage: search [search type] [arguments]') # [directory/file] [attribute] [pattern]
        print('\n  Search Types:')
        print('    \'-a\' Attribute Search ---------- Searches the attributes of files and directories within a directory for a specific pattern')
        print('    \'-f\' File Content Search ------- Searches the content of a file for a given pattern, or the files in a directory for a given pattern')
        print('    \'-i\' Input Search -------------- Searches input text for a given pattern')
        print('')
        print('\tATTRIBUTE SEARCH INSTRUCTIONS:')
        AttributeSearch.AttributeSearchInstructions('\t')
        print()
        print('\tFILE CONTENT SEARCH INSTRUCTIONS:')
        FileContentSearch.FileContentSearchInstructions('\t')
        print()
        print('\tINPUT SEARCH INSTRUCTIONS:')
        InputSearch.InputSearchInstructions('\t')
        print()
        sys.exit()

    # Determine the search mode
    # Attribute Mode
    if (sys.argv[1] == '-a'):
        AttributeSearch.AttributeSearch()
    # File Content Mode
    elif (sys.argv[1] == '-f'):
        FileContentSearch.FileContentSearch()
    # Input Mode
    elif (sys.argv[1] == '-i'):
        InputSearch.InputSearch()
    # Invalid Mode
    else:
        print(f"Error: Invalid mode: '{sys.argv[1]}'")


if __name__ == "__main__":
    main()