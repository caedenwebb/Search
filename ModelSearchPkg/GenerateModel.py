import sys
import os
import datetime
import FileClass
from ModelSearchPkg import SearchModel

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


def GetFilesForSizeModel(directory, files={}):
    """Returns a dictionary of filesizes where each filesize is the key, and the value is a list of file objects"""
    dirlist = os.listdir(directory)
    for file in dirlist:
        try:
            if os.path.isdir(directory + '/' + file):
                dirObject = FileClass.Directory(directory + '/' + file)
                if not (dirObject.size in files.keys()):
                    files[dirObject.size] = [dirObject]
                else:
                    files[dirObject.size].append(dirObject)
                print(f'Including {directory}/{file}...')
                print(f'Search {directory}/{file}...')
                GetFilesForSizeModel(directory + '/' + file, files)
            else:
                fileObject = FileClass.File(directory + '/' + file)
                if not (fileObject.size in files.keys()):
                    files[fileObject.size] = [fileObject]
                else:
                    files[fileObject.size].append(fileObject)
                print(f'Including {directory}/{file}')
        except:
            print(f'Skipping {directory}/{file} due to exception...')

    return files

def GetFilesForFilenameModel(dir):
    """Returns a list of file objects"""
    dirlist = os.listdir(dir)
    files = []
    for file in dirlist:
        try:
            if os.path.isdir(dir + '/' + file):
                dirObject = FileClass.Directory(dir + '/' + file)
                files.append(dirObject)
                print(f'Including {dir}/{file}...')
                print(f'Search {dir}/{file}...')
                results = GetFilesForFilenameModel(dir + '/' + file)
                files = files + results
            else:
                fileObject = FileClass.File(dir + '/' + file)
                files.append(fileObject)
                print(f'Including {dir}/{file}')
        except:
            print(f'Skipping {dir}/{file} due to exception...')

    return files

def GenerateFileSizeModel(directory):
    """Generates a file size model"""
    files = GetFilesForSizeModel(directory)

    sModel = SearchModel.SearchModel()
    sModel.ModelType = sys.argv[3]
    sModel.ModelDirectory = directory
    rawDate = str(datetime.date.today()).split('-')
    sModel.ModelDateCreated = f'{rawDate[1]}-{rawDate[2]}-{rawDate[0]}'

    for size in files.keys():
        sModel.Model.add(size, files[size])

def GenerateFilenameModel():
    pass