def max_players_on_server():
    small_server = 1.024e18
    medium_server = 1.024e19
    large_server = 1.024e20
    return small_server, medium_server, large_server

# code above / assignment discription below

"""Scientific Notation
As we covered earlier, a float is a positive or negative number with a fractional part.

You can add the letter e or E followed by a positive or negative integer to specify that you're using scientific notation.

print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

If you're not familiar with scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally.

In a nutshell, the exponent following the e specifies how many places to move the decimal: right when the exponent is positive, left when it's negative.

Underscores for Readability
Python also allows you to represent large numbers in the decimal format using underscores as the delimiter instead of commas to make it easier to read.

num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

Assignment
Due to the constraints of our app's server, there is a maximum number of players we can have on a single Fantasy Quest server.

Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static numbers:

The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
The max players on a "medium" server: 10,240,000,000,000,000,000
The max players on a "large" server: 102,400,000,000,000,000,000
Use scientific notation to represent these numbers. For example: 3.104e15.

Numbers in scientific notation are floats. For example, 1.024e18 is actually equivalent to 1,024,000,000,000,000,000.0 (note the .0 at the end). This is expected and perfectly fine for this assignment."""