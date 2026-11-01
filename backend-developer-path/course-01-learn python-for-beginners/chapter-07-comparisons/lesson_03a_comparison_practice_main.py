def can_withstand_blow(hero_armor, enemy_damage):
    can_withstand_blow = hero_armor >= enemy_damage
    return can_withstand_blow

#  code above / assignment discription below

"""Comparison Practice
car_size = 4
truck_size = 5
is_smaller = car_size < truck_size
# is_smaller is True

Assignment
Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise."""