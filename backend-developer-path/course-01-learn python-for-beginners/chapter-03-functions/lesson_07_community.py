def to_celsius(f):
    celsius = 5/9*(f-32)
    return celsius

## Don't touch below this line

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")

test(100)
test(88)
test(104)
test(112)

# code above / assignment below

"""Community
Getting help is a critical part of learning to code (and even in your day to day working as a developer). Boots and your spellbook are great first lines of defense. But, sometimes you just need a human. Luckily, we have an amazing Discord community full of developers and fellow students ready to help you out.

So...

Click the "Community" tab in the main nav at the top of the screen
Join the Boot.dev Discord server and sync your account
With your account linked up, you'll be able to chat with other learners and mentors, as well as use the #help... forums to ask questions. Also, if you help others in the Discord, you'll get Karma which will help you earn fellowship achievements.
When asking for help in the Discord, use the "share" button at the bottom of the lesson explanation to generate a link that includes your current code.

Assignment
Enough Discord talk, back to writing code.

In Fantasy Quest, characters lose health due to heat exhaustion. The game tracks the temperature in Freedom units (Fahrenheit), but we need to display the temperature in Celsius for players outside the US. Here's the formula to calculate the temperature in Celsius from Fahrenheit (f):

5/9 * (f - 32)

Complete the to_celsius function body. It should return the temperature in Celsius for a given Fahrenheit temperature (f parameter)."""