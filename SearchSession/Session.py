import os
import sys
import time

import GenerateModel
import FormatOutput


def SessionMain():
    print('Welcome to Search v. 1.0.')
    print('Copyright (C) 2024 Caeden Webb')
    print()
    HelpMenu()
    path = 'NO MODEL LOADED'
    model = None
    modelType = None
    validModelTypes = ['file-size', 'date-created', 'date-modified']
    while (True):
        print()
        user_input = input(f'{path}:search> ')
        if (user_input == 'quit' or user_input == 'q'):
            exit()
        elif (user_input == 'help' or user_input == 'h'):
            print()
            HelpMenu()
        elif (user_input.startswith('generate')):
            arguments = parseArguments(user_input)
            if (arguments == ['']):
                print('Error: No arguments provided.')
                continue
            if (len(arguments) == 1):
                print('Error: No path to save the model file provided.')
                continue
            if (len(arguments) == 2):
                print('Error: No model type provided.')
                continue
            directory = arguments[0]
            modelPath = arguments[1]
            modelType = arguments[2]
            if (os.path.exists(directory) == False or os.path.isdir(directory) == False):
                print(f'Error: The path \'{directory}\' is either not a valid path or not a directory.')
                continue
            if (os.path.exists(modelPath) == True):
                print(f'Error: \'{modelPath}\' already exists.')
                continue
            try:
                file = open(f'{modelPath}', 'w')
                file.close()
            except:
                print('Error: \'{modelPath}\' is not a valid path.')
                continue
            os.remove(modelPath)
            if not(arguments[2] in validModelTypes):
                print(f'Error: \'{arguments[2]}\' is not a valid model type.')


            # Generate Model
            if (modelType == 'file-size'):
                print('Generating Model...')
                model = GenerateModel.GenerateModelFileSize(directory)
            path = modelPath

            # Save Model to File
            if (modelType == 'file-size'):
                #GenerateModel.SaveModelFileSize(model, modelPath)
                pass
        elif (user_input.startswith('load')):
            arguments = parseArguments(user_input)

        elif (user_input.startswith('search')):
            arguments = parseArguments(user_input)
            if (model == None):
                print('Error: No model loaded. Please load a model before use.')
                continue
            else:
                if (modelType == 'file-size'):
                    if (arguments == []):
                        print('Error: No pattern provided.')
                        continue
                    pattern = arguments[0]
                    sizeRange = pattern.split('-')
                    # Attempt to determine the maximum and minimum ranges by obtaining it from the list and converting them to integers
                    minVal = 0
                    maxVal = 0
                    try:
                        rightValue = sizeRange[1]

                        maximumValueString = ''
                        curIndex = 0
                        for char in rightValue:
                            if (char.isnumeric()):
                                maximumValueString = maximumValueString + char
                                curIndex = curIndex + 1
                            else:
                                break

                        units = rightValue[curIndex:]
                        minVal = 0
                        maxVal = 0
                        if (units == '' or units == 'b'):
                            minVal = int(sizeRange[0])
                            maxVal = int(maximumValueString)

                        elif (units == 'kb'):
                            minVal = int(sizeRange[0]) * 1000
                            maxVal = int(maximumValueString) * 1000

                        elif (units == 'mb'):
                            minVal = int(sizeRange[0]) * 1000 * 1000
                            maxVal = int(maximumValueString) * 1000 * 1000

                        elif (units == 'gb'):
                            minVal = int(sizeRange[0]) * 1000 * 1000 * 1000
                            maxVal = int(maximumValueString) * 1000 * 1000 * 1000

                        elif (units == 'tb'):
                            minVal = int(sizeRange[0]) * 1000 * 1000 * 1000 * 1000
                            maxVal = int(maximumValueString) * 1000 * 1000 * 1000 * 1000

                        else:
                            print(f'Error: \'{units}\' is not a recognized unit.')
                            continue

                    # If the user fails to input a range correctly (e.g. failure to use a hyphen to divide minimum and maximum)
                    except IndexError:
                        print("Error: Input size ranges as follows: [minimum]-[maximum][sizeUnit]\n")
                        continue

                    # If the user inputs a range correctly, but specified anything that cannot be converted to an int (e.g. 30-15d)
                    except ValueError:
                        print("Error: Search only accepts integer size ranges\n")
                        continue  # For exiting to ensure that the following if statements do not run

                    # Check if the size range minimum is smaller than or equal to the maximum:
                    if (minVal > maxVal):
                        print(
                            f"\nError: Search minimum '{minVal}' is greater than search maximum '{maxVal}'. Did you mean '{maxVal}-{minVal}?'\n")
                        continue

                    start_time = time.time_ns()
                    results = model.rangeSearch(minVal, maxVal)
                    end_time = time.time_ns()
                    duration = end_time - start_time

                    FormatOutput.OutputAttributes(results, len(results), duration)

                elif (modelType == 'date-created'):
                    if (arguments == []):
                        print('Error: No pattern provided.')
                        continue
                elif (modelType == 'date-modified'):
                    if (arguments == []):
                        print('Error: No pattern provided.')
                        continue
        else:
            print(f'Error: "{user_input}" is an unrecognized command.')
            print()

def HelpMenu():
    print('Commands:')
    print('quit (q) --- exit the search session and close the search application')
    print('help (h) --- prints this help menu')
    print('generate [directory to model] [path to model file] [model type] --- generate a search model and load the model for use in searches')
    print('load [model] --- load a model from the filesystem to use for searches')
    print('search [pattern] [flags] --- run a search')

def parseArguments(command) -> list:
    """Returns a list of arguments for a command"""
    arguments = ['']
    inQuote = False
    currentArgument = 0
    index = 0
    if (command.startswith('generate')):
        index = 9
    elif (command.startswith('load')):
        index = 5
    elif (command.startswith('search')):
        index = 7
    else:
        return []

    while (index < len(command)):
        while index < len(command):
            if (command[index] == ' ' and inQuote == False):
                currentArgument = currentArgument + 1
                arguments.append('')
                index = index + 1
                break
            elif (command[index] == '\'' or command[index] == "\""):
                if (inQuote == False):
                    inQuote = True
                    index = index + 1
                else:
                    inQuote = False
                    index = index + 1
            else:
                arguments[currentArgument] = arguments[currentArgument] + command[index]
                index = index + 1

    return arguments

SessionMain()