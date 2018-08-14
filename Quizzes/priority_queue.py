from binary_tree_adt import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value, parent = None):
        if not parent: 
            parent = self
            
        if self.value == None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
            self._bubble_up(parent)  
            return True
        


        if self.left_node.size() == 0 and self.right_node.size() == 0: # if both nodes are empty, insert into left node
            self.left_node.insert(value, self) # self takes place of parent
            return False

        else: 
            
            if self.left_node.height() + 1 == log(self.left_node.size() + 1, 2) and (self.right_node.height() + 1) == log(self.right_node.size() + 1, 2) and self.left_node.size() == self.right_node.size():
                self.left_node.insert(value, self)
                return False

            # if left node is not full, insert into left node
            if self.left_node.height() + 1 != log(self.left_node.size() + 1, 2):
                self.left_node.insert(value, self)
                return False

        self.right_node.insert(value, self)


    def _bubble_up(self, parent = None):
        if not parent or self.value > parent.value:
            return True
        self.value, parent.value = parent.value, self.value
