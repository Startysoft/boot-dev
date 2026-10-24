print("Question 1: Functions must be ____ before they can be ____)")
print("Answer B: defined, called")  

print("Question 2: Which is best practice to make sure you don't define functions out of order?")
print("Answer A: Create an entrypoint funtion (usually called main) and call it at the end of the File")

# Quiz above / assignment below

"""
Order of Functions
All functions must be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function at the end of the file. That way all of the functions have been read by the Python interpreter before the first one is called.

Conventionally this "entry point" function is usually called main to keep things simple and consistent.

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has new_health health")

# call entrypoint at the end
main()"""