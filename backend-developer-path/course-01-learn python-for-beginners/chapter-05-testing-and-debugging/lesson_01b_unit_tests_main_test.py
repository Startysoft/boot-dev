import pytest
from lesson_01a_unit_tests_main import total_xp

run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = [
    pytest.param(0, 0, 0, marks=pytest.mark.submit),
    pytest.param(0, 200, 200, marks=pytest.mark.submit),
    pytest.param(176, 350, 17950, marks=pytest.mark.submit),
    pytest.param(250, 100, 25100, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_total_xp(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expected: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual:   {result}")
    assert result == expected_output