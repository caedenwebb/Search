"""
Node class for the AVL project.
Feel free to add additional functions here.
For example, it may be helpful to have a height() method, etc.
Some students prefer to implement the recursive add, remove, and contains functions
in Node while other keep the recursive functions in AVL.

Note that this starter code is identical to that of the Node class in the BST project.
"""

class Node:
    def __init__(self, value):
        self.value = value  # The value at this node
        self.left = None  # A link (if any) to a node with a lesser value
        self.right = None  # A link (if any) to a node with a greater value
        self.nodeContents = []

    def shiftLeft(self):
        """Shifts all nodes to the left (for instance, head node becomes left node of head, right node becomes head
        node, etc."""
        # Check for double rotation
        if self.getBalance() > 1 and self.right.getBalance() < 0:
            self.right.shiftRight()
        # Regular rotation
        if self.left == None:
            self.left = Node(self.value)
        else:
            leftNodePtr = self.left
            self.left = Node(self.value)
            self.left.left = leftNodePtr
            self.left.right = self.right.left
            self.right.left = None
        if self.pullLeft():
            self.right = None

    def pullLeft(self):
        if (self.right != None):
            self.value = self.right.value
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
            self.right = Node(self.value)
        else:
            rightPtr = self.right
            self.right = Node(self.value)
            self.right.right = rightPtr
            self.right.left = self.left.right
            self.left.right = None
        if self.pullRight():
            self.left = None

    def pullRight(self):
        if (self.left != None):
            self.value = self.left.value
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

    def add(self, value):
        if (value < self.value):
            if (self.left == None):
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if (self.right == None):
                self.right = Node(value)
            else:
                self.right.add(value)

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

            self.recbal()

    def moveEnd(self, rightNode):
        if (self.right == None):
            self.right = rightNode
        else:
            self.right.moveEnd(rightNode)

    def recbal(self):
        if (self.left != None):
            self.left.recbal()
        if (self.right != None):
            self.right.recbal()
        balanceFactor = self.getBalance()
        # Right heavy, shift left
        if (balanceFactor > 1):
            self.shiftLeft()
            if (self.right != None and self.right.left != None):
                if (self.right.left.value < self.value):
                    self.left.right = self.right.left
                    self.right.left = None
        # Left heavy, shift right
        elif (balanceFactor < -1):
            self.shiftRight()
            if (self.right != None and self.left.right != None):
                if (self.left.right.value > self.value):
                    self.right.left = self.left.right
                    self.left.right = None
        # Balanced
        else:
            pass