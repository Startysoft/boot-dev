import pytest
from lesson_03a_debugging_main import take_magic_damage

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
]

submit_cases = [
    pytest.param(0, 0, 0, 0, 0, marks=pytest.mark.submit),
    pytest.param(1, 1, 1, 1, 1, marks=pytest.mark.submit),
    pytest.param(100, 2, 3, 1, 99, marks=pytest.mark.submit),
    pytest.param(2500, 3, 2, 2, 2499, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "input4", "expected_output"),
    run_cases + submit_cases,
)
def test_take_magic_damage(input1, input2, input3, input4, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = take_magic_damage(input1, input2, input3, input4)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output