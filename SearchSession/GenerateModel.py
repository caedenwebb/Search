from AVL import avl
import SearchFileSize
import os
import FileClass
import time
import datetime

def GetFilesForDateCreatedModel(directory, files={}):
    dirlist = os.listdir(directory)

    for file in dirlist:
        if os.path.isdir(directory + '/' + file):
            dirObject = FileClass.Directory(directory + '/' + file)
            if not (dirObject.size in files.keys()):
                files[dirObject.unixTimeCreated] = [dirObject]
            else:
                files[dirObject.unixTimeCreated].append(dirObject)
            print(f'Including {directory}/{file}...')
            print(f'Search {directory}/{file}...')
            GetFilesForDateCreatedModel(directory + '/' + file, files)
        else:
            fileObject = FileClass.File(directory + '/' + file)
            if not (fileObject.size in files.keys()):
                files[fileObject.unixTimeCreated] = [fileObject]
            else:
                files[fileObject.unixTimeCreated].append(fileObject)
            print(f'Including {directory}/{file}')

        '''except:
            print(f'Skipping {directory}/{file} due to exception...')'''

    return files

def GetFilesForDateModifiedModel(directory, files={}):
    dirlist = os.listdir(directory)
    for file in dirlist:
        try:
            if os.path.isdir(directory + '/' + file):
                dirObject = FileClass.Directory(directory + '/' + file)
                if not (dirObject.size in files.keys()):
                    files[dirObject.unixTimeModified] = [dirObject]
                else:
                    files[dirObject.unixTimeModified].append(dirObject)
                print(f'Including {directory}/{file}...')
                print(f'Search {directory}/{file}...')
                GetFilesForDateModifiedModel(directory + '/' + file, files)
            else:
                fileObject = FileClass.File(directory + '/' + file)
                if not (fileObject.size in files.keys()):
                    files[fileObject.unixTimeModified] = [fileObject]
                else:
                    files[fileObject.unixTimeModified].append(fileObject)
                print(f'Including {directory}/{file}')
        except:
            print(f'Skipping {directory}/{file} due to exception...')

    return files



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

def GenerateModelFileSize(directory):
    """Generates and returns a AVL tree for searching a directory based on the file-size"""
    tree = avl.AVL()
    files = GetFilesForSizeModel(directory)
    for index in files.keys():
        tree.add(index, files[index])
    return tree

def GenerateModelDateCreated(directory):
    tree = avl.AVL()
    files = GetFilesForDateCreatedModel(directory)
    for index in files.keys():
        tree.add(index, files[index])
    return tree

def GenerateModelDateModified(directory):
    tree = avl.AVL()
    files = GetFilesForDateModifiedModel(directory)
    for index in files.keys():
        tree.add(index, files[index])
    return tree

def LoadModelFileSize(file):
    """Loads AVL tree model from file"""
    fileObject = open(file, 'r')
    rawModel = fileObject.readlines()
    fileObject.close()
    tree = avl.AVL()
    i = 0
    while (rawModel[i] != '.model\n'):
        i = i + 1
    i = i + 1

    while (rawModel[i] != '.endmodel\n'):
        extractedNode = rawModel[i].strip('\n')
        extractedNode = extractedNode.split('|')
        value = int(extractedNode[0])
        pathlist = generateList(extractedNode[1])
        nodeContents = []
        for path in pathlist:
            if (os.path.isdir(path)):
                try:
                    nodeContents.append(FileClass.Directory(path))
                except:
                    print(f'Skipping invalid path: {path}')
            else:
                try:
                    nodeContents.append(FileClass.File(path))
                except:
                    print(f'Skipping invalid path: {path}')
        tree.add(value, nodeContents)
        i = i + 1

    return tree

def SaveModelFileSize(model, file):
    fileObject = open(file, 'w')
    modelNodeList = model.as_list()
    modelFile = ['.metadata\n', 'ModelType=file-size\n', '.endmetadata\n', '.model\n']
    for node in modelNodeList:
        modelFile.append(node + '\n')
    modelFile.append('.endmodel\n')
    fileObject.writelines(modelFile)
    fileObject.close()

def generateList(stringList):
    stringList = stringList.strip('[')
    stringList = stringList.strip(']')
    stringList = stringList.replace('\'', '')
    stringList = stringList.split(', ')
    return stringList