import sys
import os

def GenerateBSTModel(dir) -> []:
    """This function generates a binary search tree search model for use in file-size searches and saves to a file"""
    filelist = os.listdir(dir)
    for file in filelist:
        if os.path.isdir(dir + file):
            GenerateBSTModel(dir + file)
        else:
            pass





