import pytest
from lesson_01a_python_numbers_main import calculate_damage

run_cases = [
    (3, 5, 2, 1, 4, (15, 3.0)),
    (5, 5, 5, 5, 5, (25, 5.0)),
]

submit_cases = [
    pytest.param(1, 2, 3, 4, 5, (15, 3.0), marks=pytest.mark.submit),
    pytest.param(0, 0, 0, 0, 10, (10, 2.0), marks=pytest.mark.submit),
    pytest.param(0, 0, 0, 0, 0, (0, 0.0), marks=pytest.mark.submit),
    pytest.param(10, 20, 30, 40, 50, (150, 30.0), marks=pytest.mark.submit),
    pytest.param(2, 2, 2, 2, 2, (10, 2.0), marks=pytest.mark.submit),
    pytest.param(1, 1, 1, 1, 1, (5, 1.0), marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("sword", "arrow", "spear", "dagger", "fireball", "expected_output"),
    run_cases + submit_cases,
)
def test_calculate_damage(sword, arrow, spear, dagger, fireball, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {sword}, {arrow}, {spear}, {dagger}, {fireball}")
    result = calculate_damage(sword, arrow, spear, dagger, fireball)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
