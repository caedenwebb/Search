import sys
import os

def GenerateFileSizeModel(dir) -> []:
    """This function generates a binary search tree search model for use in file-size searches and saves to a file"""
    pass


def GenerateModel():
    """This function implements functionality to determine which model to generate, and where to save the model"""

    # If no search model type is entered
    if (len(sys.argv) < 4):
        print('Error: No model type provided.')
        exit()

    # Determine whether the entered model type is a valid model type
    validModelTypes = ['filename', 'filesize', 'date-created', 'date-modified']
    if not (sys.argv[3] in validModelTypes):
        print(f'Error: \'{sys.argv[3]}\' is not a valid search model type.')
        exit()

    # If no directory was provided to model
    if (len(sys.argv) < 5):
        print('Error: No directory provided to model.')
        exit()

    # If the directory to model is not valid
    if (os.path.exists(f'{sys.argv[4]}') == False):
        print(f'Error: \'{sys.argv[4]}\' is not a valid directory.')
        exit()

    # If no path is provided to save the model
    if (len(sys.argv) < 6):
        print('Error: No path provided to save the model.')
        exit()

    # If the path already exists
    if (os.path.exists(f'{sys.argv[5]}')):
        print(f'Error: \'{sys.argv[5]}\' already exists.')
        exit()

    # If the path is invalid
    try:
        file = open(f'{sys.argv[5]}', 'w')
        file.close()
    except FileNotFoundError:
        print(f'Error: \'{sys.argv[5]}\' is not a valid path.')

    # Filename Models
    if (sys.argv[3] == 'filename'):
        GenerateFilenameModel()

    # Filesize Models
    if (sys.argv[4] == ''):
        GenerateFileSizeModel(sys.argv[4])



def GenerateFilenameModel():
    pass