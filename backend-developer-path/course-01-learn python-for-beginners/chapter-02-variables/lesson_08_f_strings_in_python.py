name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

#code above / assignment below

"""F-Strings in Python
Have you ever played old-school Pokemon and chosen a funny name so that the in-game messages would come out funny?

america strength

In Python, we can create strings that contain dynamic values with the f-string syntax.

num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
# You have 10 bananas

Add an f to the start of quotes to create an f-string: f"this is easy!"
Use curly brackets {} around a variable to interpolate (put) its value into the string.
You can also use an f-string directly inside a print() call, without assigning it to a variable first. It's just a string – don't overthink it!

Assignment
Fix the bug on line 7. Use an f-string to inject the dynamic values into the string:

Replace NAME with the value of the name variable
Replace RACE with the value of the race variable
Replace AGE with the value of the age variable
Do not "hard-code" the values into the string. For example, this is not the solution we're looking for (even though it happens to work in this case):

print("Yarl is a dwarf who is 37 years old.")

We need the player to see their values.

Punctuation and capitalization matters! Make sure your output matches the expected output exactly."""