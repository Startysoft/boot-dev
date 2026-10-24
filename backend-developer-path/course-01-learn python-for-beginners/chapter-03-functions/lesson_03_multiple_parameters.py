def triple_attack(damage_one, damage_two, damage_three):
    Damage_result = damage_one + damage_two + damage_three
    return Damage_result

# Don't touch below this line

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# code above / assignment below

"""Multiple Parameters
Functions can have multiple parameters ("parameter" being a fancy word for "input"). For example, this subtract function accepts 2 parameters: a and b.

def subtract(a, b):
    result = a - b
    return result

It's the argument's position that determines which parameter receives it. The first argument goes to the first parameter, the second to the second, and so on. In this example, the subtract function is called with a = 5 and b = 3:

result = subtract(5, 3)
print(result)
# 2

Here's another example with three parameters:

def create_introduction(name, age, height):
    intro = f"Hello, {name}! You are {age} years old and {height} meters tall."
    return intro

It can be called like this:

msg = create_introduction("Elendil", 322, 2.4)
print(msg)
# Hello, Elendil! You are 322 years old and 2.4 meters tall.

Assignment
We need to calculate the total damage from a combo of three attacks.

Complete the triple_attack function by returning the sum of its parameters, damage_one, damage_two, and damage_three. Remember to indent the code inside the function body.

The pass statement is just a placeholder that does nothing. Replace it with your code.

Tip
The attack damage values (attack_one to attack_six) are already passed to the two triple_attack function calls for you. You only need to reference them by their new damage parameter names (damage_one, damage_two, and damage_three)."""