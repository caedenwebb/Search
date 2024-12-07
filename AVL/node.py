"""
Node class for the AVL project.
Feel free to add additional functions here.
For example, it may be helpful to have a height() method, etc.
Some students prefer to implement the recursive add, remove, and contains functions
in Node while other keep the recursive functions in AVL.

Note that this starter code is identical to that of the Node class in the BST project.
"""

class Node:
    def __init__(self, value, nodeContents):
        self.value = value  # The value at this node
        self.left = None  # A link (if any) to a node with a lesser value
        self.right = None  # A link (if any) to a node with a greater value
        self.nodeContents = nodeContents

    def shiftLeft(self):
        """Shifts all nodes to the left (for instance, head node becomes left node of head, right node becomes head
        node, etc."""
        # Check for double rotation
        if self.getBalance() > 1 and self.right.getBalance() < 0:
            self.right.shiftRight()
        # Regular rotation
        if self.left == None:
            self.left = Node(self.value, self.nodeContents)
        else:
            leftNodePtr = self.left
            self.left = Node(self.value, self.nodeContents)
            self.left.left = leftNodePtr
            self.left.right = self.right.left
            self.right.left = None
        if self.pullLeft():
            self.right = None

    def pullLeft(self):
        if (self.right != None):
            self.value = self.right.value
            self.nodeContents = self.right.nodeContents
            '''Attempt to fix code with respect to line 59 of tests'''
            if self.left == None:
                if self.right.left != None:
                    self.left = self.right.left
                    self.right.left = None
            '''END: Attempt to fix code with respect to line 59 of tests'''
            if not self.right.pullLeft():
                return False
            else:
                self.right = None
                return False
        else:
            return True

    def shiftRight(self):
        """Shifts all nodes to the right (for example, head node becomes right node, etc)."""
        # Check for double rotation
        if self.getBalance() < -1 and self.left.getBalance() > 0:
            self.left.shiftLeft()
        # Regular rotation
        if self.right == None:
            self.right = Node(self.value, self.nodeContents)
        else:
            rightPtr = self.right
            self.right = Node(self.value, self.nodeContents)
            self.right.right = rightPtr
            self.right.left = self.left.right
            self.left.right = None
        if self.pullRight():
            self.left = None

    def pullRight(self):
        if (self.left != None):
            self.value = self.left.value
            self.nodeContents = self.left.nodeContents
            '''Attempt to fix code with respect to line 59 of tests'''
            if self.right == None:
                if self.left.right != None:
                    self.right = self.left.right
                    self.left.right = None
            '''END: Attempt to fix code with respect to line 59 of tests'''
            if not self.left.pullRight():
                return False
            else:
                self.left = None
                return False
        else:
            return True

    def add(self, value, nodeContents):
        if (value < self.value):
            if (self.left == None):
                self.left = Node(value, nodeContents)
            else:
                self.left.add(value, nodeContents)
        else:
            if (self.right == None):
                self.right = Node(value, nodeContents)
            else:
                self.right.add(value, nodeContents)

        balanceFactor = self.getBalance()
        # Right heavy, shift left
        if (balanceFactor > 1):
            self.shiftLeft()
        # Left heavy, shift right
        elif (balanceFactor < -1):
            self.shiftRight()
        # Balanced
        else:
            pass

    def getBalance(self):
        """Get the balance factor of a node"""
        heightRight = 1
        heightLeft = 1
        if (self.right != None):
            heightRight = 1 + self.right.height()
        if (self.left != None):
            heightLeft = 1 + self.left.height()
        return heightRight - heightLeft

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

    def search(self, min, max):
        contents = []


        return contents

    def getContents(self, node):
        pass
