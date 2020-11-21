

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        return self.root.
