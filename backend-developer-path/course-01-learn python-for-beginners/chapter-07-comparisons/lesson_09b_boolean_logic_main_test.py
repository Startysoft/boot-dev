import pytest
from lesson_09a_boolean_logic_main import does_attack_hit

run_cases = [
    (17, 18, False),
    (20, 25, True),
    (2, 2, True),
]

submit_cases = [
    pytest.param(1, 0, False, marks=pytest.mark.submit),
    pytest.param(16, 13, True, marks=pytest.mark.submit),
    pytest.param(5, 5, True, marks=pytest.mark.submit),
    pytest.param(1, 1, False, marks=pytest.mark.submit),
    pytest.param(20, 20, True, marks=pytest.mark.submit),
    pytest.param(15, 10, True, marks=pytest.mark.submit),
    pytest.param(2, 3, False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_does_attack_hit(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = does_attack_hit(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
