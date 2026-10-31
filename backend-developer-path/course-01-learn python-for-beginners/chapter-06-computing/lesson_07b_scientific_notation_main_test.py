import pytest
from lesson_07a_scientific_notation_main import max_players_on_server

run_cases = [
    (1.024e18, 1.024e19, 1.024e20),
]

submit_cases = []


@pytest.mark.parametrize(
    ("expected1", "expected2", "expected3"), run_cases + submit_cases
)
def test_max_players_on_server(expected1, expected2, expected3):
    print("\n---------------------------------")
    result = max_players_on_server()
    print(f"Expected: {(expected1, expected2, expected3)}")
    print(f"Actual:   {result}")
    assert result == (expected1, expected2, expected3)
