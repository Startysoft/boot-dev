import pytest
from Lesson_12a_bitwise_I_operator_main import calculate_guild_perms

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011, 0b1011),
]

submit_cases = [
    pytest.param(0b0000, 0b0000, 0b0000, 0b1011, 0b1011, marks=pytest.mark.submit),
    pytest.param(0b1001, 0b0010, 0b1101, 0b1011, 0b1111, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "input4", "expected_output"),
    run_cases + submit_cases,
)
def test_calculate_guild_perms(input1, input2, input3, input4, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = calculate_guild_perms(input1, input2, input3, input4)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
