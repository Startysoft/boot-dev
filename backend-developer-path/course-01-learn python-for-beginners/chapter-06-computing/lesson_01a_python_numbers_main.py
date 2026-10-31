def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

#code above/ assignment discription below

"""Python Numbers
In Python, numbers without a decimal point are called Integers – just like they are in mathematics.

Integers are simply whole numbers, positive or negative. For example, 3 and -3 are both examples of integers.

Arithmetic can be performed as you might expect:

Addition
2 + 1
# 3

Subtraction
2 - 1
# 1

Multiplication
2 * 2
# 4

Division
3 / 2
# 1.5 (a float)

This one is actually a bit different – division on two integers will actually produce a float. A float is, as you may have guessed, the number type that allows for decimal values.

Assignment
Complete the missing sections of the calculate_damage function.

Fix the total_damage variable so that it contains the sum of all the different weapons' and spells' damage values.
Fix the average_damage variable so that it contains the average of the combined weapon and spell damage."""