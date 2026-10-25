print("Question 1: What happens if there is no 'return' line in a function?")
print("Answer C: It returns None")

print("Question 2: What's the difference between printing a value and returning it?")
print("Answer C: print shows a value in the console, return makes a value available to the caller of the function.")

# Quiz above / assignment discription below

"""None Return
When no return value is specified in a function, it will automatically return None. For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value. The following code snippets all return the same value, None:

def my_func():
    print("I do nothing")
    return None

def my_func():
    print("I do nothing")
    return

def my_func():
    print("I do nothing")

If we print the returned value, we see it is None.

result = my_func()
# I do nothing

print(result)
# None"""