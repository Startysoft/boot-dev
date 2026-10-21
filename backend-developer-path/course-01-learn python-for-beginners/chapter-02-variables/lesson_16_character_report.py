name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 10.5
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")

# code above / assingment below

"""Character Report
One of our interns built a program that prints information about Fantasy Quest characters. It's almost done, but there are still a few bugs.

Assignment
Fix the bugs to get the character report working!

Run the code to see it fail.
Fix the syntax so that each variable is the data type you'd expect:
name: String
level: Integer
character_class: String
magic_resistance: Float (change the variable assignment, not the print statement)
account_active: Boolean
Do not change the meaning of the values, only the syntax around them to change their data type.

Tips
You need to use the correct type-specific syntax for the variables. Here are some examples:

Type	Rule	Example
String	Double quotes	"Hello"
Integer	Whole number	42
Float	Use a Decimal	2.0
Boolean	True or False	True
"""