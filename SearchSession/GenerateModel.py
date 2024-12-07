from AVL import avl
import SearchFileSize
import os
import FileClass
from AVL import avl

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

def CreateModel(files):
    for index in files.keys():
        pass