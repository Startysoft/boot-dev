import pytest
from lesson_11a_bitwise_AND_operator_main import get_create_bits, get_delete_bits, get_edit_bits, get_review_bits

run_cases = [
    (get_create_bits, 0b1000, 0b1010, True),
    (get_review_bits, 0b0100, 0b1001, False),
    (get_delete_bits, 0b0010, 0b0110, True),
    (get_edit_bits, 0b0001, 0b1110, False),
]

submit_cases = [
    pytest.param(get_create_bits, 0b1000, 0b0111, False, marks=pytest.mark.submit),
    pytest.param(get_review_bits, 0b0100, 0b0110, True, marks=pytest.mark.submit),
    pytest.param(get_delete_bits, 0b0010, 0b1101, False, marks=pytest.mark.submit),
    pytest.param(get_edit_bits, 0b0001, 0b0011, True, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("func", "perm_bit", "user_permissions", "expected_output"),
    run_cases + submit_cases,
)
def test_permission_bits(func, perm_bit, user_permissions, expected_output):
    print("\n---------------------------------")
    print(f"Testing {func.__name__}")
    print(f"Inputs: {user_permissions:04b}")
    print(f"Expecting: {expected_output}")
    result = func(user_permissions) == perm_bit
    print(f"Actual:    {result}")
    assert result == expected_output
