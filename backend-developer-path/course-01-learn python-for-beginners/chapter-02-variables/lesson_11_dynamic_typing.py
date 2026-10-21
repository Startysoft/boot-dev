print("question 1:  Is changing the type of a variable generally a good idea?")
print("Answer C:    No")

print("question 2:  What kind of typinh does python employ?")
print("Answer B:    Dynamic")

# code above / assignment below

"""Dynamic Typing
Python is dynamically typed, which means a variable can store any type, and that type can change.

For example, if I make a number variable, I can later change that variable to a string:

speed = 5
speed = "five"

But Like, Maybe Don't
In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one. For example:

speed = 5
speed_description = "five"

What Is Non-Dynamic Typing?
Languages that aren't dynamically typed are statically typed, such as Go and Typescript (one of which you'll learn in a later course depending on your chosen track). In a statically typed language, if you try to assign a value to a variable of the wrong type, you'll get a compile-time error and the program won't run.

If Python were statically typed, the first example from before wouldn't allow the second line, speed = "five". The computer would give an error along the lines of you can't assign a string value ("five") to a number variable (speed)."""