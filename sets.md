# Set

## Technical Description

A set is a data structure where the can only be one of each data point. You can’t have 2 3’s in your set, as it would no longer be a set. Sets are great because sets use a technique called hashing, which allows us to determine if we have a specific data piece in a set at NO COST TO EFFICIENCY. If we used a regular array, our efficiency would be O(n)! We can also add and remove data from the set just as easily, and also with no cost to your efficiency.

## Metaphor

Think of it like this. You’re at your Thanksgiving dinner and mashed potatoes are your favorite dish on the table. However, if you fill up your plate with mashed potatoes and only mashed potatoes, the rest of your family will get mad at you for “eating an entire pot of mashed potatoes”, as if it’s some kind of problem. 

In order to have a healthy, balanced meal, you need a bit of everything. Some turkey, some green beans, some rolls, and of course, some mashed potatoes. With a few key differences, this is exactly what a set is. A set cannot have a heaping mound of only 5’s or even a little extra 5 on the side. Doing so defeats the purpose of having a set.

## Useful For?

So why is this so important? What's the reason for all this fuss of having just one number? Using a set allows you to have data that is guaranteed to be different from each other. Imagine that you have a database full of user IDs. If two users had the same ID the result would be disastrous! One user would do actions that would affect the other user, making a very confusing time for both users and IT. With a set we can first check if the ID we use for a new user is free. If it matches no other number in the set, the ID is good to use!

## How to Use and Code walkthrough

