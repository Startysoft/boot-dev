import pytest
from lesson_06a_plus_equals_main import get_hurt

run_cases = [
    (1000, 100, 900),
    (900, 60, 840),
]

submit_cases = [
    pytest.param(840, 10, 830, marks=pytest.mark.submit),
    pytest.param(830, 3, 827, marks=pytest.mark.submit),
    pytest.param(0, 0, 0, marks=pytest.mark.submit),
    pytest.param(1, 1, 0, marks=pytest.mark.submit),
    pytest.param(100, 2, 98, marks=pytest.mark.submit),
    pytest.param(2500, 3, 2497, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("current_health", "damage", "expected_output"), run_cases + submit_cases
)
def test_get_hurt(current_health, damage, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {current_health}, {damage}")
    print(f"Expected:  {expected_output}")
    result = get_hurt(current_health, damage)
    print(f"Actual: {result}")
    assert result == expected_output
