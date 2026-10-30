import pytest
from lesson_06a_stack_track_main import create_stats_message

run_cases = [
    (1, 2, 3, "You have 1 strength, 2 wisdom, and 3 dexterity for a total of 6 stats."),
    (2, 4, 2, "You have 2 strength, 4 wisdom, and 2 dexterity for a total of 8 stats."),
]

submit_cases = [
    pytest.param(
        10,
        50,
        100,
        "You have 10 strength, 50 wisdom, and 100 dexterity for a total of 160 stats.",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        0,
        0,
        0,
        "You have 0 strength, 0 wisdom, and 0 dexterity for a total of 0 stats.",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        1,
        1,
        1,
        "You have 1 strength, 1 wisdom, and 1 dexterity for a total of 3 stats.",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_create_stats_message(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = create_stats_message(input1, input2, input3)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
