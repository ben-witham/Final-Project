############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of trees
#          and their useful functions
# 
############################################################

# This is our tree class, it contains all information related to the tree we're creating
class Tree:
    # Whenever working with binary search trees, the basic thing that you will need is a Node class
    # This node class is a class inside a tree class, meaning that the node class CANNOT be accessed unless by way of the Tree class
    class Node:
        # A node class will hold all the data for one node on the tree, and the tree will be made up of multiple nodes
        def __init__(self, data):
            # The right node is a pointer to the node connected to this one on the right side, the left is a pointer to the node to the left and data is the actual data of the node
            self.right = None
            self.left = None
            self.data = data
    
    def __init__(self):
        # When a tree is made, this is run, currently, the root node is zero because there are no nodes in the tree
        self.root = None

    # Often, recursive functions have wrapper functions to make it easier on the programmer to call them later
    # This insert is one
    def insert(self, data):
        # First we check if our tree is empty by checking if the root node is equal to None, if it is the tree is empty
        if self.root is None:
            # Create a node as the root node with the data
            self.root = Tree.Node(data)
        else:
            # Otherwise, we call the recursive sort function
            self.recursive_insert(data, self.root)


    def recursive_insert(self, data, node):
        # First we must check if our data is greater or less than the current parent node
        if data < node.data:
            # If this statement passes, the data must be on the left side so we can keep our efficiency up
            if node.left is None:
                # If the pointer of our current parent node to the left side is none, then there is an empty spot to put our node
                # We then create a new node on the left
                node.left = Tree.Node(data)
            else:
                # If there is not an open spot, we must keep going down the tree
                # this is where recursion comes in handy
                # Trying to find a loop for this would be incredibly difficult
                # But with recursion we can just edit the parameters and call the recursive_insert function again
                # Notice that we are now using the left node of the current node and that left node will become the current node when we run this function
                self.recursive_insert(data, node.left)
        # If the data is larger than the data in our current node, it belongs on the right side of the tree
        elif data > node.data:
            # Now, just like above, we must check whether or not the node to our right is empty
            # If it is, we can insert a new node there
            if node.right is None:
                # We can create a new node here
                node.right = Tree.Node(data)
            # Otherwise, we need to keep looking, and we need to change the recursive function to search the right side of the tree
            else:
                self.recursive_insert(data, node.right)
        # Sometimes, you will have duplicate values try to be inserted into your tree
        # How you handle duplicates is up to you
        # However, I am just going to ignore any duplicate values
        elif data == node.data:
            return

    # This function is called whenever the "in" operator is used in python, or whenever the tree is iterated over
    def __iter__(self):
        # This function will do an in-order travesal that starts at the root
        # Again, this is a wrapper function that we call that then calls the recursive function

        yield from self.recursive_in_order(self.root)
        # Notice the yield keyword that we use. This is very important 
        # The yield command is like a return, where it gives the caller back a result
        # The yield will run many times, as many times as is needed
        # A return function will run once before needing to be sent back to the caller
        # Once a return is sent back, any local variables are destroyed
    
    # Now we need to make the recursive function that __iter__ calls
    def recursive_in_order(self, node):
        # This will do an in-order traversal, meaning that the function will first go to the lowest numbers and from that ascend
        # If the node is none, then there would be no data for us to check, giving us an error.
        # This statement prevents that error from happening
        if node is not None:
            # The yields allow us to return to this function without destroying any of our local variables
            yield from self.recursive_in_order(node.left)
            yield node.data
            yield from self.recursive_in_order(node.right)

    # There is also a reverse-order traverse that will return the numbers in reserve order
    # Using what you know from the function above, can you make it?
    # The wrapper function for that uses __reversed__() instead of __iter__()

    # This function is like the __iter__ function where it will get called from the python script from a different operator
    # In this case __contains__() is called by the "in" operator
    def __contains__(self, data):
        # This function can be inmplemented recursively, but I will do this one with a normal loop
        # We start the node at the root node
        current_node = self.root

        # Then we create this loop go forever, but we'll return out of it eventually
        while True:
            # If the current_node is None, that means that we were never able to find our number, and it wasn't in our tree
            if current_node is None:
                return False
            # If the data is equal, that is our number
            if current_node.data == data:
                return True
            # if the current_node data is greater than the data input, then the number is going to be to the right of us
            elif current_node.data > data:
                # We then switch the current node to get the next node
                current_node = current_node.right
            # Similar process to above, except to the left side
            elif current_node.data < data:
                current_node = current_node.left

