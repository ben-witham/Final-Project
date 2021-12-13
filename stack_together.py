############################################################
# 
# Author: Benjamin Witham
# Date Created: 12/8/2021
# Purpose: This is to help build an understanding of stacks
#          and their useful functions
# 
############################################################

# For this example, we are going to be keeping track of a stack
# of pancakes, as we make pancakes we can add them to the stack,
# when people eat pancakes they take them off of the stack

# First, let's create our stack
stack_of_pancakes = []

# Next, we're going to add some pancakes to our stack
stack_of_pancakes.append("blueberry")
stack_of_pancakes.append("chocolate chip")
stack_of_pancakes.append("plain")
stack_of_pancakes.append("buttermilk")

# Now if we print out our stack of pancakes, we'll see all of the pancakes currently on the plate

print("The plate starts with:", stack_of_pancakes)
# This should print out this: ['blueberry', 'chocolate chip', 'plain', 'buttermilk']
# Notice that the pancakes are all printed in order that we put them in. With the stack implementation
# that blueberry pancake at the bottom will be the last pancake to be taken away.

# So writing out all those append (push) statements was boring. Let's make the computer do that for us!

def make_pancakes(pancakes_made, pancake_type):
    # For the number that you specify, this loop will run that many times
    for i in range(0, pancakes_made):
        # and each time the loop runs, it adds a pancake of that type to the stack
        stack_of_pancakes.append(pancake_type)
    # After we make these new pancakes, lets show what pancakes are in the stack
    print("The plate now has:", stack_of_pancakes)

# Now lets make 4 new bacon pancakes!
make_pancakes(4, "bacon")

# Making all these pancakes has made us hungry, and we both eat a pancake from off the top
stack_of_pancakes.pop()
stack_of_pancakes.pop()

# Now we should have two less bacon pancakes on the top
print("This plate now has:", stack_of_pancakes)

# Now lets make a function that will serve pancakes to people
# But before we write code, we need to make sure we have enough pancakes to feed everyone
# With this we'd use size() and empty() functions, but python doesn't have function calls for those.
# Instead, they're both based off of the len() function
# len() = size()
# len() == 0 = empty()

def serve_pancakes(hungry_people):
    # We get how many people want to eat some pancakes
    # First we check the length of the stack
    if hungry_people > len(stack_of_pancakes):
        print("There is not enough pancakes for everyone!")
        print("There will be", hungry_people - len(stack_of_pancakes), "hungry people.")
        # Keep taking off pancakes as people go through
    for i in range(0, hungry_people):
        # if the stack is empty we want to break our loop
        if len(stack_of_pancakes) == 0:
            print("No more pancakes on plate")
            break
        # If the stack is not empty, we will take a pancake off
        stack_of_pancakes.pop()
    # We then see what's in our stack
    print("This plate now has:", stack_of_pancakes)

# Now let's serve pancakes to three people
serve_pancakes(3)

# Feel free to keep using this code to learn more about stacks, and once you're ready try to solve the problem included in the tutorial