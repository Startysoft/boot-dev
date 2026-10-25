def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed

# Don't modify below this line

def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")

def main():
    test(100)
    test(500)
    test(1000)

main()

# code above / assignment discription below

"""Curse
An enemy's weapons can be cursed so that they don't deal as much damage.

Assignment
Complete the curse function. It accepts a weapon_damage parameter and returns two values:

The lesser_cursed damage: reduce the input weapon_damage to 50% of its original value (a 50% reduction).
The greater_cursed damage: reduce the input weapon_damage to 25% of its original value (a 75% reduction).
A greater curse is more powerful than a lesser curse, so it reduces the damage more.

Tip
You can multiply a number by a decimal to get a percentage of a number. For example:

30% of 50 is 50 * 0.3"""