############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of sets
#          and their useful functions
# 
############################################################

# In this example, we are a company that needs to keep track of users and their different usernames. 
# For this we will use a set, because we don't want more than two users with the same name

# This is how you create an empty set, rather than using empty curly braces
# This is because an empty set of curly braces creates a dictionary, not a set
username_set = set()

# This is a simple function to nicely print out our sets
def print_set(set):
    for user in set:
        print(user, end=", ")
    print()

# This checks whether a user is already in the system before assigning a new username
def add_user():
    # Start with our datacheck boolean
    username_invalid = True
    # This loop will run until a new username is input
    while(username_invalid):
        username = input("What is your username: ")
        # If the user name is already in the set we cannot add another
        if username in username_set:
            print("Username already taken")
    
    # The loop stops with a unique username, and we add that to our list
    username_set.add(username)

# This function removes a user
def remove_user():
    # First we print the set for the current user to see
    print_set(username_set)
    # We get the username to remove from the user
    user_to_remove = input("Which user would you like to remove: ")
    # if the username we want to remove is in the set, remove it. Otherwise, print out an error message
    if user_to_remove in username_set:
        username_set.remove(user_to_remove)
    else:
        print("That user doesn't exist")

# This checks to see how many people are currently using the companies software
def company_statistics(set_stat):
    # We use the python len() function to check the size of the array
    print("There are currently", len(set_stat), "users.")
    print_set(set_stat)

# Now that we have all these useful functions, lets make our user list!
# First we add some users to our set. Let's do 5 of them
# For demonstration purposes, put one down as BillMcIntosh and one as MrCleaner
for i in range(0,5):
    add_user()

# If we call our company_statistics function, we can see that we now have those five users and their names
company_statistics(username_set)

# Now lets say that we acquire another smaller company, and we want to import the usernames from the last company
# But we can't let the usernames from the other company corrupt our data
# First, here is the other companies username set
othercompany_username_set = {"freddie6", "orangebob", "BillMcIntosh", "MrCleaner", "xx_supercrazyfreak_xx", "annie", "bob"}

# We want to see if any usernames conflict, so we use an intersection function for that
conflict_set = username_set & othercompany_username_set
# Notice above that we used an ampersand instead of the intersection function word. These do the same thing, it's just different syntax

# Next we check if there are any conflicts in our set, if there are, we print that out to the user
if len(conflict_set) == 0:
    print("There are no conflicts")
else:
    print("There are some conflicts. These are: ", end="")
    print_set(conflict_set)

# After this we can look at the usernames that are fine with a union operation
combined_set = othercompany_username_set | username_set
print_set(combined_set)