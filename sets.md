# Set

## Technical Description

A set is a data structure where the can only be one of each data point. You can’t have 2 3’s in your set, as it would no longer be a set. Sets are great because sets use a technique called hashing, which allows us to determine if we have a specific data piece in a set at NO COST TO EFFICIENCY or an efficiency of O(1). If we used a regular array, our efficiency would be O(n)! We can also add and remove data from the set just as easily, and also with no cost to your efficiency or again with an efficiency of O(1).

## Metaphor

Think of it like this. You’re at your Thanksgiving dinner and mashed potatoes are your favorite dish on the table. However, if you fill up your plate with mashed potatoes and only mashed potatoes, the rest of your family will get mad at you for “eating an entire pot of mashed potatoes”, as if it’s some kind of problem. 

In order to have a healthy, balanced meal, you need a bit of everything. Some turkey, some green beans, some rolls, and of course, some mashed potatoes. With a few key differences, this is exactly what a set is. A set cannot have a heaping mound of only 5’s or even a little extra 5 on the side. Doing so defeats the purpose of having a set.

## Useful For?

So why is this so important? What's the reason for all this fuss of having just one number? Using a set allows you to have data that is guaranteed to be different from each other. Imagine that you have a database full of user IDs. If two users had the same ID the result would be disastrous! One user would do actions that would affect the other user, making a very confusing time for both users and IT. With a set we can first check if the ID we use for a new user is free. If it matches no other number in the set, the ID is good to use!

One important note is that Python does not check if the number you're adding is already in your set. If you add another number that's the same, Python will not throw an error. This is done so that we can easily switch back and forth between sets, where there are no duplicates, and lists, where there are possibly many duplicates.

## How to Use and Code Walkthrough

Sets are great but you can't do anything with an empty set! To add data to a set, you will use the add function, and to take data away from a set, use the remove function. Whenever you use these functions remember to add the data that you want to add and remove, like the example below:

![](/assets/set_add_and_remove.PNG)

You can check the length of a set by using the python len() function, just like you can do with an array. 

Sets also tell you whether or not something a piece of data is within the set, and for pytho you'll use the in operator like this:
```python
my_set = {1,2,3}

if 2 in my_set:
    return True
else:
    my_set.add(2)
```

Finally, we can add sets together, using two different methods; one is an intersection, and one is a union. A union joins the sets together and removes any duplicate values, while an intersection shows only the duplicate values between the two sets. They are done like this:

```python
first_set = {1,2,4,6}
second_set = {4,6,7,8}

# This will give a result of {4, 6}
intersection_set = intersection(first_set, second_set)
# This will give a result of {1, 2, 4, 6, 7, 8}
union_set = union(first_set, second_set)
```
Those are the main functions that you'll use for sets, and see them in action [here.](set_together.py)

Once you feel comfortable with the code try doing [this](set_problem.py) problem on your own.

Finally, once you've finished, you can look at [this](set_solution.py) possible solution and compare it to yours.

Use [this](README.md) to get back to the main page.