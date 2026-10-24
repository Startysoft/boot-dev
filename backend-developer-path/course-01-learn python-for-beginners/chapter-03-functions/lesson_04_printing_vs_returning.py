def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return(title)

# Don't touch below this line

def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")

test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")

## code above / assignment below

"""Printing vs. Returning
Some new developers get hung up on the difference between print and return. They seem interchangeable, but they are not!

print is a function that:
Prints a value to the console
Does not return a value
def print_alchemy():
    print("equivalent exchange")


printed_alchemy = print_alchemy()
# equivalent exchange

print(printed_alchemy)
# None

return is a keyword that:
Ends the current function's execution
Provides a value (or values) back to the caller of the function
Does not print anything to the console (unless the return value is later printed)
def return_transmutation():
    return "nothing is lost"


returned_transmutation = return_transmutation()

print(returned_transmutation)
# nothing is lost

Printing to Debug Your Code
Printing values to the console is a great technique for debugging your code. By running the code, you can see what values are stored in variables, find your mistakes, and fix them. Add print statements and run your code as you go! Making sure that each line you write does what you expect is a great habit to get into.

In the real world, it's rare to leave print statements in your code when you're done debugging. Similarly, on Boot.dev you need to remember to remove any print statements from your code before submitting your work because it will fail the tests!

Assignment
There's a problem in the get_title function! It's supposed to construct the title value and return it to the caller. Instead, it's barbarically printing the value to the console!

Fix the get_title function.

Remove the print statement in get_title
return the title in get_title"""