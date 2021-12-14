############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/11/2021
# Purpose: This is to help build an understanding of trees
#          and their useful functions
# 
############################################################



# Using the code below, write a function to balance an unbalanced tree

# Tree Balance Hints:
# In order to balance a tree, you need all the data points in order
# After you get the points in order, you need to find the middle, and from there insert the points
# Once you find the middle, lower points should be inserted in descending order, and higher points should be inserted in ascending order
def balance_tree(tree):
    pass


# This is our tree class, it contains all information related to the tree we're creating
class Tree:

    class Node:
        def __init__(self, data):
           
            self.right = None
            self.left = None
            self.data = data
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = Tree.Node(data)
        else:
            self.recursive_insert(data, self.root)


    def recursive_insert(self, data, node):

        if data < node.data:
            if node.left is None:
                node.left = Tree.Node(data)
            else:
                self.recursive_insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Tree.Node(data)
            else:
                self.recursive_insert(data, node.right)
        elif data == node.data:
            return

    def __iter__(self):

        yield from self.recursive_in_order(self.root)
    
    def recursive_in_order(self, node):

        if node is not None:
            yield from self.recursive_in_order(node.left)
            yield node.data
            yield from self.recursive_in_order(node.right)

    def __contains__(self, data):

        current_node = self.root

        while True:
            if current_node is None:
                return False
            if current_node.data == data:
                return True
            elif current_node.data > data:
                current_node = current_node.right
            elif current_node.data < data:
                current_node = current_node.left

