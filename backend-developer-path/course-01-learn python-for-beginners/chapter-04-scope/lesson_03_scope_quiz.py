print("question 1: Does the get_area_of_circle function have access to the pi variable?")
print("Answer A: Yes, because de pi variable is in the global scope.")  

print("Question 2: Without returning it, can the area variable inside the get_area_of_circle function be accessed outside of the function?")
print("Answer C: No, variables defined inside a function are not accessible outside of it.")    

# Quiz above / Assignment definition below

"""Scope Quiz
pi = 3.14


def get_area_of_circle(radius):
    area = pi * radius * radius
    return area"""