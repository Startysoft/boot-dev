import pytest
from lesson_05a_debugging_practice_main import unlock_achievement

run_cases = [
    (100, 20, "Speedster", (120, "Achievement Unlocked: Speedster")),
    (200, 50, "Killer", (250, "Achievement Unlocked: Killer")),
]

submit_cases = [
    pytest.param(
        100,
        50,
        "Unstoppable",
        (150, "Achievement Unlocked: Unstoppable"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        400,
        75,
        "Gnarly",
        (475, "Achievement Unlocked: Gnarly"),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_unlock_achievement(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = unlock_achievement(input1, input2, input3)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
