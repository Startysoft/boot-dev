import pytest
from lesson_14a_coverting_binary_main import binary_string_to_int

run_cases = [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
]

submit_cases = [
    pytest.param("0", "0", "0", (0, 0, 0), marks=pytest.mark.submit),
    pytest.param("1111", "1111", "1111", (15, 15, 15), marks=pytest.mark.submit),
    pytest.param("101010", "110011", "101010", (42, 51, 42), marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_binary_string_to_int(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = binary_string_to_int(input1, input2, input3)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
