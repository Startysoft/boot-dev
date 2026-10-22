def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")

# Code above / Assignment below

"""Functions
Functions let us reuse and organize code. Say we have some code that calculates the area of a circle:

radius = 5
area = 3.14 * radius * radius

That works! The problem is when we want to calculate the area of other circles, each with its own radius. We could just copy the code and change the variable names like this:

radius = 5
area1 = 3.14 * radius * radius

radius2 = 7
area2 = 3.14 * radius2 * radius2

But we want to reuse our code! Who wants to redo the same work?!? What if we wanted to calculate the area of thousands of circles??? That's where functions help.

Instead, let's define a new function called area_of_circle using the def keyword:

def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

It takes one input (aka "parameter" or "argument") called r
After the :, the indented lines form the function body, that is, the code that runs each time we use (aka "call") the function
It returns (outputs) a single value. In this case, the value stored in the result variable
To "call" this function (fancy programmer speak for "use this function") we can pass in any number as the argument (in this case, 5) for the parameter r, and capture the output into a new variable:

area = area_of_circle(5)
print(area)
# 78.5

5 goes in as the input r
The body of the function runs, storing 78.5 in the result variable in the function body
The function returns the result variable, meaning the area_of_circle(5) expression evaluates to 78.5
78.5 is stored in the area variable and then printed
Because we've already defined the function, now we can use it as many times as we want with different inputs!

area = area_of_circle(10)
print(area)
# 314.0

area = area_of_circle(7)
print(area)
# 153.86

Try calling the function yourself and watch the body run:

Call a Function
Define a function once, then call it as many times as you want.
def area_of_circle(r):
# r = 7
    pi = 3.14
# pi = 3.14
    result = pi * r * r
# result = 153.86
    return result
# returns 153.86
 
area = area_of_circle(7)
# area = 153.86
Current step
Back at the call site, store 153.86 in area.
area_of_circle(5)
area_of_circle(6)
area_of_circle(7)
r
Call
6 / 6
Auto

1x
Assignment
We need to calculate the size of a weapon's "attack area." With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

Fix the bug where spear_area is 0 by calling the area_of_circle function with the spear_length as input and store the result in the spear_area variable."""