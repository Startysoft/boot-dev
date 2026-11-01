import pytest
from lesson_02a_comparison_operator_evaluations_main import compare_heights

run_cases = [
    (5, 5, 7, 5, (True, True, False)),
    (6, 6, 5, 5, (False, True, False)),
]

submit_cases = [
    pytest.param(4, 4, 4, 4, (True, True, True), marks=pytest.mark.submit),
    pytest.param(2, 2, 2, 2, (True, True, True), marks=pytest.mark.submit),
    pytest.param(8, 8, 8, 7, (False, True, True), marks=pytest.mark.submit),
    pytest.param(5, 7, 9, 11, (False, False, False), marks=pytest.mark.submit),
    pytest.param(11, 9, 7, 5, (False, False, False), marks=pytest.mark.submit),
    pytest.param(5, 6, 6, 5, (True, False, True), marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("elon", "sara", "jill", "bob", "expected"), run_cases + submit_cases
)
def test_compare_heights(elon, sara, jill, bob, expected):
    print("\n---------------------------------")
    print(f"Inputs: {elon}, {sara}, {jill}, {bob}")
    result = compare_heights(elon, sara, jill, bob)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert result == expected
