############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of stacks
#          and their useful functions
# 
############################################################

# Setting: You're working on a new software, and you want to add an undo and a REDO function
# Everytime the undo and redo are done, the software should update to show the user the current data stage
# How would you go about creating this method? Remember that stacks are good for tracking your history

# Some starter code below

def undo():
    pass

def redo():
    pass

def get_input():
    pass

def main_loop():
    while(True):
        show_options()
        user_input = int(input("What would you like to do: "))
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

main_loop()