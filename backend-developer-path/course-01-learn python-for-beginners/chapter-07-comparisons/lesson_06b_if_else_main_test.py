import pytest
from lesson_06a_if_else_main import player_status

run_cases = [
    (0, "dead"),
    (4, "injured"),
    (6, "healthy"),
]

submit_cases = [
    pytest.param(5, "injured", marks=pytest.mark.submit),
    pytest.param(1, "injured", marks=pytest.mark.submit),
    pytest.param(10, "healthy", marks=pytest.mark.submit),
    pytest.param(-1, "dead", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("health", "expected_status"), run_cases + submit_cases)
def test_player_status(health, expected_status):
    print("\n---------------------------------")
    print(f"Health: {health}")
    result = player_status(health)
    print(f"Expected: {expected_status}")
    print(f"Result:   {result}")
    assert result == expected_status

# code above / assignment discription below

"""If-Else
An if statement can be followed by zero or more elif (which stands for "else if") statements, which can be followed by zero or one else statements.

For example:

if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")

First the if statement is evaluated. If it is True then the if statement's body is executed and all the other elifs and the else are ignored.

If the first if is false then the next elif is evaluated. Likewise, if it is True then its body is executed and the rest are ignored.

If none of the if or elif statements evaluate to True then the final else statement will be the only body executed.

If-else flowchart: with a score of 90 and high scores of 100, 80, and 60, the first check is false and the second is true. The second-place message prints, the remaining branches are skipped, and execution continues after the chain.

Assignment
Complete the player_status function. If the player's health is less than or equal to 0, return the string:

dead

Otherwise, if it's less than or equal to 5 return the string:

injured

Otherwise, return the string:

healthy"""