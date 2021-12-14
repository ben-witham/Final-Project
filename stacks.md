# Stack

## Technical Description

The stack is a data-type that is characterized by a Last-In First-Out method. Any data that this structure receives will be removed from the data structure before any older data. If a new piece of data is added, that new data must now be removed first.

## Metaphor

Imagine that you have a tower of jenga blocks. You can only take the block off the top; if you tried to pull the block from the bottom, the tower would fall! If you want to remove the block at the very bottom, you need to remove every block on top sequentially before you can remove the bottom block. 

![](/assets/block_stack.PNG)

Let’s quickly recreate your tower, or stack, of jenga blocks. Now let’s say that you want to put a block in the very middle of the stack. If we try to push our block in, the tower will fall over. To get to the middle, we need to remove each block from the top until we get to where we want to place our block. We can then place our new block and add all the other blocks we removed to get down to it.

## Useful For?

Stacks are used every time you program, but you may or may not realize that yet. Every time you call a function, it’s added onto the stack. If you ever notice when you get an error, you’ll get a wall of text like this.

![](/assets/stack_fail.PNG)

If you read the text, you’ll notice that the text runs through all the functions that called your function before the error caused the crash. 

Stacks are useful when you need to remember the last thing you’ve done, which is like what happens above. The computer needs to remember which function its done, otherwise, after completing a function, it wouldn’t be able to return to your main function!

## How to Use and Code walk-through

To do a stack in python, we will be using a python list. If you haven’t used a list before, fret not! Lists are very easy. To create a list, all you need to do is use brackets around your data, and separate any of your starting data with commas like this:

![](/assets/python_list.PNG)

If you’re treating your list like a stack, then the key functions you will use to manipulate data on the stack is push() and pop(). You ‘push’ new data on to the stack, and ‘pop’ old data off the stack. In python to push, you will use the append keyword, and to pop, just use the pop function like this:

![](/assets/push_and_pop.PNG)

The awesome thing about append and pop is the efficiency is O(1), so there is no cost to using these functions!

Those are the main functions that you'll use for stacks, but there are some others that will be covered in this code [here.](stack_together.py)

Once you feel comfortable with the code try doing [this](stack_problem.py) problem on your own.

Finally, once you've finished, you can look at [this](stack_solution.py) possible solution and compare it to yours.

Use [this](README.md) to get back to the main page.