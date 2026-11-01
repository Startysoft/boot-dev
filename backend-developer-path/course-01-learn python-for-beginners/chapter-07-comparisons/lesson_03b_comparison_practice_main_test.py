import pytest
from lesson_03a_comparison_practice_main import can_withstand_blow

run_cases = [(175, 250, False), (250, 175, True), (1, 1, True)]

submit_cases = [
    pytest.param(250, 250, True, marks=pytest.mark.submit),
    pytest.param(0, 0, True, marks=pytest.mark.submit),
    pytest.param(2, 3, False, marks=pytest.mark.submit),
    pytest.param(3, 2, True, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_can_withstand_blow(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = can_withstand_blow(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
