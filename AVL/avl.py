
from AVL.node import Node

"""
The AVL class. It will have one member variable, root, 
which is the first node (if there are any).
Don't forget to implement these functions with recursion.

Note that the following functions can be the same as in your BST project:
- contains
- size
- as_list
- height

You will want to add a function that calculates the balance factor of a node.
You will also want to add a function that rotates nodes left or right.
Then you will want to add the functionality that decides how to rotate nodes (or double rotate them)
 based on their balance factor.
"""

# I used https://www.youtube.com/watch?v=2ldaQMa_o74 to help understand the AVL tree data structure


class AVL:
    def __init__(self):
        self.head = None

    def add(self, value):
        if (self.head == None):
            self.head = Node(value)
        else:
            self.head.add(value)
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
                self.head.recbal()
            elif (ret == 'SETTORIGHT'):
                self.head = self.head.right
                self.head.recbal()
            elif (ret == 'MOVERIGHTTOEND'):
                rightNode = self.head.right
                self.head = self.head.left
                self.head.moveEnd(rightNode)
                self.head.recbal()
            else:
                pass

        return self

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
            return self.head.height()

    def printExt(self):
        printExt.printExt(self)