from AVL import avl
import SearchFileSize
import os
import FileClass
import time

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

'''model = GenerateModelFileSize('G:/My Drive/College Files/2024-2025')
while (True):
    userInput = input('search>')
    if (userInput == 'q'):
        break
    else:
        userInput = userInput.split('-')
        start_time = time.time_ns()
        results = model.rangeSearch(int(userInput[0]), int(userInput[1]))
        end_time = time.time_ns()

        print(f'Results ({len(results)}, {end_time - start_time}ns):')

        for file in results:
            print(file.filename)'''