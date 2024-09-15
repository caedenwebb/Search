class File:

    def __init__(self, path):
        self.path = path
        self.filename = ''
        self.size = ''
        self.date_created = ''
        self.date_modified = ''
        self.ReturnData = None
        self.Filestream = None

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