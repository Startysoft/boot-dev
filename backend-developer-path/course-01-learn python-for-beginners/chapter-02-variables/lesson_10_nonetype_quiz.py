print("Question: Why might you use a None value?")
print("Answer D: As the default value that will be replaced later")

# quiz above / assignment below

"""NoneType Quiz
As we mentioned in the last exercise, the None keyword is used to define an "empty" variable.

So when would you use it? One use case is to represent that a value hasn't been determined yet, for example, an uncaptured input. Maybe your program is waiting for a user to enter their name. You might start with a variable:

username = None

Then later in the code, once the user has entered their name, you can assign it to the username variable:

username = input("What's your name? ")

Remember, it's crucial to recognize that None is not the same as the string "None". They look the same when printed to the console, but they are different data types. If you use "None" instead of None, you will end up with code that looks correct when it's printed but fails the tests. In that case, printing the type would distinguish between the two values.

str_none = "None"
actual_none = None

print(str_none)  # None
print(actual_none)  # None

print(type(str_none))  # <class 'str'>
print(type(actual_none))  # <class 'NoneType'>"""