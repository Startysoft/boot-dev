def hours_to_seconds(hours):
    seconds = hours * 60 * 60
    return seconds

# Don't touch below this line

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

test(10)
test(1)
test(25)
test(100)
test(33)

# code above / assignment discription below

"""Solutions
Okay, I just need to tell you about one last resource you have when you're stuck. Every lesson on Boot.dev has an instructor solution that you can view!

Like Boots, solutions come at a cost... a steeper one in fact. If you view a solution before you complete the lesson, you'll lose all the XP for that lesson. Well, unless you use a seer stone – in which case you won't lose any XP. Though you will be down a seer stone.

For this lesson only, you can claim enough gems to buy a seer stone.

Just like it's free to use Boots after a lesson is complete, viewing a solution after you've completed the lesson is free as well. In fact, we encourage you to frequently check your work against ours, often times there's something to learn from the differences.

View solutions sparingly. If you find yourself using the solution before completion more than about once per chapter you should consider slowing down, asking for help in the discord, and even resetting lessons and trying them again to build a stronger foundation.

Assignment
Enough about solution mechanics, let's write more code.

We need to display the current time to our players. The problem is that the time is stored as a number of hours, but we want to display it as a number of seconds. There are 60 seconds in a minute, but how many are in an hour?

Complete the hours_to_seconds function. It should convert hours to seconds and return the result."""