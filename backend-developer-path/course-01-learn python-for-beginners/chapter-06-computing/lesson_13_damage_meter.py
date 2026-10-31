def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()

# code above / assignment below

"""Damage Meter
You've been working with a group of interns to build a damage meter for Fantasy Quest... it's not going well.

Assignment
Fix the interns' error. The calculate_dps function should accept two arguments, but it's being called with 4 instead. Use the proper delimiter for thousands so that the numbers are still easy to parse visually.

The two numbers should be:

damage: 8 million, time: 45
damage: 10 million, time: 49
Tip
In normal text, 1,000,000,000 is one billion written with commas as the delimiters for better legibility. In Python, commas can't be used this way, but you can use underscores instead: 1_000_000_000."""