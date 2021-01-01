import random
class Node:

    def __init__(self):

        self.left = None
        self.right = None
        self.data = None
    def addDataArray(self, dataArr):
        for data in dataArr:
            self.addData(data)

    def addData(self, data):
        if not self.data:
            self.data = data
        else:
            if data > self.data:
                if not self.right:
                    self.right = Node()
                self.right.addData(data)
            else:
                if not self.left:
                    self.left = Node()
                self.left.addData(data)

    def preorder(self):
        #used for copying a tree
        print(self.data)

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        #used for getting the contentes of a binary tree in ascending order
        if self.left:
            self.left.inorder()

        print(self.data)

        if self.right:
            self.right.inorder()

    def postorder(self):
        #used for going from infix to reverse polish notation
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.data)

    def search(self, item):
        if self.data == item:
            return self
        if item > self.data:
            return self.right.search(item)
        else: #if item < self.data
            return self.left.search(item)

data = [5,8,3,6,2,7,4,9,1]
mytree = Node()
mytree.addDataArray(data)
mytree.preorder()
print("~~~~~~~~~~~~~~~~~~")
mytree.inorder()
print("~~~~~~~~~~~~~~~~~~")
mytree.postorder()
print("~~~~~~~~~~~~~~~~~~")
print(mytree.search(7).data)