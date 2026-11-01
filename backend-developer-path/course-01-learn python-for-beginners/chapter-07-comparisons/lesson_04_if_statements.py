def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()

# code above / assignment discription below

"""If Statements
It's often useful to only execute code if a certain condition is met:

if CONDITION:
    # do some stuff here

# code after the if block may still run regardless

For example, in this code:

def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")

if boss_health is greater than 0, then this will be printed:

Ganondorf is alive!

Otherwise, this will be printed:

Ganondorf is unalive!

Without a return in the if block, Ganondorf is unalive would always be printed:

def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
    print("Ganondorf is unalive!")

This code could print both messages:

Ganondorf is alive!
Ganondorf is unalive!

When you only want code within an if block to run, use return to exit the function early.

Indentation is what tells Python whether the body of a function or the if statement has ended. Don't forget the colon after your if statement :; it is a required part of the syntax!

Assignment
Complete the print_status function.

If player_health is less than or equal to 0, print the text dead to the console.
Afterwards, whether or not the player is dead, print the text status check complete to the console."""