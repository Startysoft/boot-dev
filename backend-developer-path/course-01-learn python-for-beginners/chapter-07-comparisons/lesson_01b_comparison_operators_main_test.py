import pytest
from lesson_01a_comparison_operators_main import player_1_wins

run_cases = [
    (5, 6, False),
    (5, 5, False),
    (7, 6, True),
]

submit_cases = [
    pytest.param(10, 3, True, marks=pytest.mark.submit),
    pytest.param(2, 2, False, marks=pytest.mark.submit),
    pytest.param(0, 0, False, marks=pytest.mark.submit),
    pytest.param(10, 5, True, marks=pytest.mark.submit),
    pytest.param(5, 10, False, marks=pytest.mark.submit),
    pytest.param(3, 2, True, marks=pytest.mark.submit),
    pytest.param(4, 1, True, marks=pytest.mark.submit),
    pytest.param(6, 8, False, marks=pytest.mark.submit),
    pytest.param(9, 10, False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("player_1_score", "player_2_score", "expected"), run_cases + submit_cases
)
def test_player_1_wins(player_1_score, player_2_score, expected):
    print("\n---------------------------------")
    print(f"Inputs: {player_1_score}, {player_2_score}")
    result = player_1_wins(player_1_score, player_2_score)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
