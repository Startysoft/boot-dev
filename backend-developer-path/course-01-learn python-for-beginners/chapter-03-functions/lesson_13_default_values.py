def get_punched(health, armor=0):
    damage = 50 - armor
    return health - damage


def get_slashed(health, armor=0):
    damage = 100 - armor
    return health - damage

# Don't touch below this line

def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")

test(400, 5)
test(300, 3)
test(200, 1)

# code above / assignment discription below

"""Default Values
You can specify a default value for a function parameter, which is useful when a function has parameters that are "optional." They're created by using the assignment operator (=) inside the function signature:

def get_greeting(email, name="there"):
    print(f"Hello {name}, welcome! You've registered your email: {email}")

If we call it with both arguments, it uses the provided values:

get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com

But if we omit the optional name argument, it will use the default value instead:

get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com

Optional parameters (the ones with defaults) must come after all required parameters.

Assignment
Complete the get_punched and get_slashed functions. They both take two integers as arguments, health and armor.

Complete the get_punched function:
In the function signature, give the armor parameter a default value of 0.
In the function body, create a damage variable equal to 50 minus the armor. (Armor reduces damage.)
Return the result of the input health minus the calculated damage.
Complete the get_slashed function:
In the function signature, give the armor parameter a default value of 0.
In the function body, create a damage variable equal to 100 minus the armor.
Return the result of the input health minus the calculated damage."""