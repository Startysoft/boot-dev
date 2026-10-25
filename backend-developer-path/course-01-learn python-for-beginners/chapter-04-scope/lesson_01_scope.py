def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

# don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")

# code above / assignment discription below

"""Scope
Scope refers to where a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.

Example
def subtract(x, y):
    return x - y


result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"

When the subtract function is called, we assign 5 to the variable x, but x only exists in the code within the subtract function. If we try to print x outside of that function, then we won't get a result. In fact, we'll get a big fat error.

Click to show video
Assignment
Find the bug in the code on line 10. We're using variable names from the wrong scope. Fix it!"""