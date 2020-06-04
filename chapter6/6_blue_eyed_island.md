# Blue-Eyed Island

## Question

A bunch of people are living on an island, when a visitor comes with a strange order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at 8:00 pm every evening. Each person can see everyone else's eye color, but they do not know their own (nor is anyone allowed to tell them). Additionally, they do not know how many people have blue eyes, although they do know that at least one person does. How many days will it take the blue-eyed people to leave?

## Answer

It will take the same number of days as the number of blue-eyed people (where leaving the first flight out counts as 1 day).

For the base case, let's say there is only 1 blue-eyed person. She sees 0 blue-eyed people, and since she knows there must be at least 1 blue-eyed person, then she deduces she must be blue-eyed. Thus, she will leave the 1st day (and not earlier). 

If there are 2 blue-eyed people, then each of these people sees 1 other blue-eyed person. They deduce there are either 1 or 2 blue-eyed people (depending on whether or not they are blue-eyed). Since they don't know how many blue-eyed people there are for sure, neither will leave the first day. Thus, the next day, they will see the blue-eyed person did not leave. Thus, they each deduce they must have blue eyes (making 2 blue-eyed people), because if there were only 1 blue-eyed person, she would have left the 1st day (per the base case). Thus, both blue-eyed people leave the 2nd day.

Formally, assume the inductive hypothesis that if there are n blue-eyed people on the island, then all blue-eyed people will leave on the nth day (and not earlier). Then if there are n+1 blue-eyed people, these people will all see n blue-eyed people. They will each deduce that there are either n or n+1 blue-eyed people. Since they don't know, they will not leave through the nth day. After the nth day, though, they will all see that none of the blue-eyed people left. Thus, they deduce they must have blue eyes (making n+1 blue-eyed people), because if there were only n blue-eyed people, they all would have left the nth day. Thus, all blue-eyed people leave on day n+1.

By induction, it will take the n days for the blue-eyed people to leave when there are n blue-eyed people.

Note that, from the perspective of non-blue-eyed people, they will see n blue-eyed people if there are n blue-eyed people on the island. They deduce there are either n or n+1 people with blue eyes. But on the nth day, all the blue-eyed people will leave (since they see n-1 blue-eyed people). Thus, the remaining people deduce that they do not have blue eyes.
