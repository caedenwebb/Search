import os
import sys
import time
import datetime

if __name__ != "__main__":
    from SearchSession import GenerateModel
if __name__ == "__main__":
    import GenerateModel
import FormatOutput
import utils


# I used this page for help converting times to unixtime: https://docs.python.org/3.12/library/datetime.html#datetime.timestamp
#How to find timestamp: int(datetime.datetime(year, month, day).timestamp())

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
            sys.exit()
        elif (user_input == 'help' or user_input == 'h'):
            print()
            HelpMenu()
        elif (user_input.startswith('generate')):
            arguments = parseArguments(user_input)
            if (arguments == ['']):
                print('Error: No directory to model provided.')
                continue
            if (len(arguments) == 1):
                print('Error: No model type provided.')
                continue

            directory = arguments[0]
            modelType = arguments[1]

            if (os.path.exists(directory) == False or os.path.isdir(directory) == False):
                print(f'Error: The path \'{directory}\' is either not a valid path or not a directory.')
                continue
            if not(arguments[1] in validModelTypes):
                print(f'Error: \'{arguments[2]}\' is not a valid model type.')
                continue

            # Generate Model
            if (modelType == 'file-size'):
                print('Generating Model...')
                model = GenerateModel.GenerateModelFileSize(directory)
            elif (modelType == 'date-created'):
                print('Generating Model...')
                model = GenerateModel.GenerateModelDateCreated(directory)
            elif (modelType == 'date-modified'):
                print('Generating Model...')
                model = GenerateModel.GenerateModelDateModified(directory)
            path = directory


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
                    dateRange = arguments[0]
                    dateSet = dateRange.split('-')
                    firstDate = dateSet[0].split('/')
                    secondDate = dateSet[1].split('/')

                    # I used this page for help converting times to unixtime: https://docs.python.org/3.12/library/datetime.html#datetime.timestamp
                    firstDateUnix = int(datetime.datetime(int(firstDate[2]), int(firstDate[0]), int(firstDate[1])).timestamp())
                    secondDateUnix = int(datetime.datetime(int(secondDate[2]), int(secondDate[0]), int(secondDate[1])).timestamp())

                    start_time = time.time_ns()
                    results = model.rangeSearch(firstDateUnix, secondDateUnix)
                    end_time = time.time_ns()
                    duration = end_time - start_time

                    FormatOutput.OutputAttributes(results, len(results), duration)


                elif (modelType == 'date-modified'):
                    if (arguments == []):
                        print('Error: No pattern provided.')
                        continue
                    dateRange = arguments[0]
                    dateSet = dateRange.split('-')
                    firstDate = dateSet[0].split('/')
                    secondDate = dateSet[1].split('/')

                    # I used this page for help converting times to unixtime: https://docs.python.org/3.12/library/datetime.html#datetime.timestamp
                    firstDateUnix = int(
                        datetime.datetime(int(firstDate[2]), int(firstDate[0]), int(firstDate[1])).timestamp())
                    secondDateUnix = int(
                        datetime.datetime(int(secondDate[2]), int(secondDate[0]), int(secondDate[1])).timestamp())

                    start_time = time.time_ns()
                    results = model.rangeSearch(firstDateUnix, secondDateUnix)
                    end_time = time.time_ns()
                    duration = end_time - start_time

                    FormatOutput.OutputAttributes(results, len(results), duration)
        else:
            print(f'Error: "{user_input}" is an unrecognized command.')
            print()

def HelpMenu():
    print('Commands:')
    print('quit (q) --- exit the search session and close the search application')
    print('help (h) --- prints this help menu')
    print('generate [directory to model] [model type] --- generate a search model and load the model for use in searches')
    print('search [pattern] --- run a search')

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