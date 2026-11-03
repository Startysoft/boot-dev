import pytest
from lesson_08a_if_else_practice_main import check_high_score

run_cases = [
    ("ash ketchum", "ash ketchum", "brock", "high"),
    ("brock", "ash ketchum", "brock", "low"),
]

submit_cases = [
    pytest.param("misty", "brock", "ash ketchum", "neither", marks=pytest.mark.submit),
    pytest.param("red", "red", "blue", "high", marks=pytest.mark.submit),
    pytest.param("blue", "red", "blue", "low", marks=pytest.mark.submit),
    pytest.param("green", "red", "blue", "neither", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    (
        "player_name",
        "high_scoring_player_name",
        "low_scoring_player_name",
        "expected_output",
    ),
    run_cases + submit_cases,
)
def test_check_high_score(
    player_name, high_scoring_player_name, low_scoring_player_name, expected_output
):
    print("\n---------------------------------")
    print(
        f"Player Name: {player_name}, High Scoring Player: {high_scoring_player_name}, Low Scoring Player: {low_scoring_player_name}"
    )
    result = check_high_score(
        player_name, high_scoring_player_name, low_scoring_player_name
    )
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
