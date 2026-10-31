import pytest
from lesson_05a_changing_in_place_main import update_player_score

run_cases = [
    (0, 100, 100),
    (100, 200, 300),
]

submit_cases = [
    pytest.param(300, 300, 600, marks=pytest.mark.submit),
    pytest.param(600, 50, 650, marks=pytest.mark.submit),
    pytest.param(0, 0, 0, marks=pytest.mark.submit),
    pytest.param(1, 1, 2, marks=pytest.mark.submit),
    pytest.param(100, -50, 50, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_update_player_score(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = update_player_score(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
