import pytest
from Lesson_05a_if_else_main import player_status

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
