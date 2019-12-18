import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value > self.value: # then it belongs on the right
            if self.right is None: # so if there is room on the right
                self.right = BinarySearchTree(value) # extend a branch there
            else: # but if there isn't room
                self.right.insert(value) # move right and try again
        elif value < self.value: # then it belongs on the left
            if self.left is None: # so if there is room on the left
                self.left = BinarySearchTree(value) # extend a branch there
            else: # but if there isn't room
                self.left.insert(value) # move left and try again
            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value: # if this is the target we're looking for
            return True # success!
        elif target > self.value: # then it belongs on the right
            if self.right is None: # so if there isn't anything on the right
                return False # it isn't there
            else: # but if there is stuff on the right
                return self.right.contains(target) # check the right
        elif target < self.value: # then it belongs on the left
            if self.left is None: # so if there isn't anything on the left
                return False # it isn't there
            else: # but if there is stuff on the left
                return self.left.contains(target) # check the left

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None: # if there's nothing to the right
            return self.value # this is the maximum value
        else: # but if there is something to the right
            return self.right.get_max() # it's on the right, so check there

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value) # call the function cb for the current value
        if self.right is not None: # and if there's anything to the right
            self.right.for_each(cb) # apply this for_each function to the right
        if self.left is not None: # and if there's anything to the left
            self.left.for_each(cb) # apply this for_each function to the left
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
