import os
import time
import datetime
class File:

    def __init__(self, path):
        self.path = path
        self.type = 'FILE'

        # Determine filename
        splitPath = self.path.split('/')
        self.filename = splitPath[len(splitPath)-1]

        # Determine size
        self.size = os.path.getsize(path)


        # Determine the dates that the files were created and modified
        rawCreationDate = time.localtime(os.path.getctime(path))
        rawModifiedDate = time.localtime(os.path.getmtime(path))
        self.unixTimeCreated = int(datetime.datetime(rawCreationDate.tm_year, rawCreationDate.tm_mon, rawCreationDate.tm_mday).timestamp())
        self.unixTimeModified = int(datetime.datetime(rawModifiedDate.tm_year, rawModifiedDate.tm_mon, rawModifiedDate.tm_mday).timestamp())
        self.rawCreationTime = os.path.getctime(path)
        self.rawModifiedTime = os.path.getmtime(path)
        self.date_created = [rawCreationDate.tm_mon, rawCreationDate.tm_mday, rawCreationDate.tm_year]
        self.date_modified = [rawModifiedDate.tm_mon, rawModifiedDate.tm_mday, rawModifiedDate.tm_year]

        # Setup other attributes
        self.ReturnData = None
        self.Filestream = None

    def __str__(self):
        return f'{self.path}'

    def ReadMode(self):
        if (self.Filestream != None):
            self.Filestream.close()
            self.Filestream = None
        self.Filestream = open(self.path, 'r')

    def WriteMode(self):
        if (self.Filestream != None):
            self.Filestream.close()
            self.Filestream = None
        self.Filestream = open(self.path, 'w')

    def CloseFilestream(self):
        if (self.Filestream != None):
            self.Filestream.close()
            self.Filestream = None
class Directory:
    def __init__(self, path):
        self.path = path
        self.type = 'DIR'

        # Determine filename
        splitPath = self.path.split('/')
        self.filename = '/' + splitPath[len(splitPath) - 1]

        # Determine other attributes
        self.size = os.path.getsize(path)
        rawCreationDate = time.localtime(os.path.getctime(path))
        rawModifiedDate = time.localtime(os.path.getmtime(path))
        self.unixTimeCreated = int(datetime.datetime(rawCreationDate.tm_year, rawCreationDate.tm_mon, rawCreationDate.tm_mday).timestamp())
        self.unixTimeModified = int(datetime.datetime(rawModifiedDate.tm_year, rawModifiedDate.tm_mon, rawModifiedDate.tm_mday).timestamp())
        self.rawCreationTime = os.path.getctime(path)
        self.rawModifiedTime = os.path.getmtime(path)
        self.date_created = [rawCreationDate.tm_mon, rawCreationDate.tm_mday, rawCreationDate.tm_year]
        self.date_modified = [rawModifiedDate.tm_mon, rawModifiedDate.tm_mday, rawModifiedDate.tm_year]
        self.ReturnData = None

    def __str__(self):
        return f'{self.path}'