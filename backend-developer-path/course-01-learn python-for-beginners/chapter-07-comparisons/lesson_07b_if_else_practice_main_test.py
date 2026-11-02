import pytest
from lesson_07a_if_else_practice_main import check_high_score

run_cases = [
    ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
    ("brock", "ash ketchum", "You are not the highest scoring player!"),
]

submit_cases = [
    pytest.param(
        "misty",
        "brock",
        "You are not the highest scoring player!",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "ash ketchum",
        "misty",
        "You are not the highest scoring player!",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "", "", "You are the highest scoring player!", marks=pytest.mark.submit
    ),
    pytest.param(
        "same", "same", "You are the highest scoring player!", marks=pytest.mark.submit
    ),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_check_high_score(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = check_high_score(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
