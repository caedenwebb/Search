class Node:
    def __init__(self, value, files):
        self.value = value  # The value at this node
        self.left = None  # A link (if any) to a node with a lesser value
        self.right = None  # A link (if any) to a node with a greater value
        self.files = []
    def add(self, value, files):
        if (value < self.value):
            if (self.left == None):
                self.left = Node(value, files)
            else:
                self.left.add(value, files)
        else:
            if (self.right == None):
                self.right = Node(value, files)
            else:
                self.right.add(value, files)

    def remove(self, value):
        # If value of node is the same as the value passed in
        if (self.value == value):
            # If node has no child nodes:
            if (self.left == None and self.right == None):
                return 'DELETE'
            # if node has left node but not right node
            elif (self.left != None and self.right == None):
                return 'SETTOLEFT'
            # If node has right node but not left node
            elif (self.right != None and self.left == None):
                return 'SETTORIGHT'
            # If node has both left and right nodes
            else:
                return 'MOVERIGHTTOEND'
        else:
            # Recurse left node
            if (self.left != None):
                ret = self.left.remove(value)
                if (ret == 'DELETE'):
                    self.left = None
                elif (ret == 'SETTOLEFT'):
                    self.left = self.left.left
                elif (ret == 'SETTORIGHT'):
                    self.left = self.left.right
                elif (ret == 'MOVERIGHTTOEND'):
                    rightNode = self.left.right
                    self.left = self.left.left
                    self.left.moveEnd(rightNode)
                else:
                    pass
            # Recurse right node
            if (self.right != None):
                ret = self.right.remove(value)
                if (ret == 'DELETE'):
                    self.right = None
                elif (ret == 'SETTOLEFT'):
                    self.right = self.right.left
                elif (ret == 'SETTORIGHT'):
                    self.right = self.right.right
                elif (ret == 'MOVERIGHTTOEND'):
                    rightNode = self.right.right
                    self.right = self.right.left
                    self.right.moveEnd(rightNode)
                else:
                    pass

    def moveEnd(self, rightNode):
        if (self.right == None):
            self.right = rightNode
        else:
            self.right.moveEnd(rightNode)

    def contains(self, value):
        if (self.value == value):
            return True
        elif (value < self.value):
            if (self.left == None):
                return False
            else:
                return self.left.contains(value)
        else:
            if (self.right == None):
                return False
            else:
                return self.right.contains(value)

    def as_list(self):
        returnList = [self.value]
        if (self.left != None):
            returnList = returnList + self.left.as_list()
        if (self.right != None):
            returnList = returnList + self.right.as_list()

        return returnList

    def size(self):
        if (self.left == None and self.right == None):
            return 0
        elif (self.left == None or self.right == None):
            if (self.left == None):
                return 1 + self.right.size()
            else:
                return 1 + self.left.size()
        else:
            return 2 + self.left.size() + self.right.size()

    def height(self):
        if (self.left == None and self.right == None):
            return 1
        elif (self.left != None and self.right != None):
            leftHeight = 1 + self.left.height()
            rightHeight = 1 + self.right.height()
            if (leftHeight >= rightHeight):
                return leftHeight
            else:
                return rightHeight
        elif (self.left != None):
            return 1 + self.left.height()
        else:
            return 1 + self.right.height()


class BST:
    """
    BST constructor. There is no need to change this function.
    """

    def __init__(self):
        self.head = None

    def add(self, value, files):
        if (self.head == None):
            self.head = Node(value, files)
        else:
            self.head.add(value, files)
        return self

    def remove(self, value):
        # If tree is empty
        if (self.head == None):
            return self
        else:
            ret = self.head.remove(value)
            if (ret == 'DELETE'):
                self.head = None
            elif (ret == 'SETTOLEFT'):
                self.head = self.head.left
            elif (ret == 'SETTORIGHT'):
                self.head = self.head.right
            elif (ret == 'MOVERIGHTTOEND'):
                rightNode = self.head.right
                self.head = self.head.left
                self.head.moveEnd(rightNode)
            else:
                pass

        return self

    def moveEnd(self, rightNode):
        self.head.moveEnd(rightNode)


    def contains(self, value):
        if (self.head == None):
            return False
        else:
            return self.head.contains(value)

    def size(self):
        if (self.head == None):
            return 0
        else:
            return 1 + self.head.size()

    def as_list(self):
        returnList = []
        if (self.head == None):
            return returnList
        else:
            returnList = self.head.as_list()
            return returnList

    def height(self):
        if self.head == None:
            return 0
        else:
            self.head.height()