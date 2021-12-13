############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of stacks
#          and their useful functions
# 
############################################################

# Setting: You're working on a new software, and you want to add an undo and a REDO function
# How would you go about creating this method? Remember that stacks are good for tracking your history

# This is one possible solution, made specifically using stacks. If your solution does not match this, that's okay!
# What matters is that you learned and solved the problem your own way

# First I'm going to create a stack that will hold our input 
undo_stack = []

# Then I will create another stack of all the data that is needing to be redone

redo_stack = []

# Then we write a quick function to get input from the user
def get_input():
    new_word =  input("Write a new word to the sentence: ")
    undo_stack.append(new_word)
    
    # Once we add new input we delete all the other data in the redo stack
    for i in range(0, len(redo_stack)):
        redo_stack.pop()

# Populate our data
for i in range(0,5):
    get_input()

# A simple function to print our stack without all the quotation marks and commas
def print_stack(stack):
    for word in stack:
        print(word, end = " ")
    print()

print()

print_stack(undo_stack)

# This is our undo function
def undo():
    # First we check if the undo_stack is empty
    if len(undo_stack) == 0:
        print("Cannot undo, nothing left to undo!")
        return
    # if there is stuff in the stack we send the data from the end of the undo_stack to the end of the redo_stack
    temp_data = undo_stack[len(undo_stack) - 1]
    undo_stack.pop()
    redo_stack.append(temp_data)
    # Show the user the current state of the stack
    print_stack(undo_stack)

# the redo function is basically the undo function, but in reverse
def redo():
    if len(redo_stack) == 0:
        print("Cannot redo, all data up to date!")
        return
    temp_data = redo_stack[len(redo_stack) - 1]
    redo_stack.pop()
    undo_stack.append(temp_data)
    print_stack(undo_stack)

def main_loop():
    while(True):
        show_options()
        user_input = int(input("What would you like to do: "))
        print()
        if user_input == 1:
            get_input()
        elif user_input == 2:
            undo()
        elif user_input == 3:
            redo()
        elif user_input == 4:
            break
        else:
            print("Input not recognized!")

def show_options():
    print("\t[1] Add to sentence")
    print("\t[2] Undo")
    print("\t[3] Redo")
    print("\t[4] Quit")
    print()

main_loop()