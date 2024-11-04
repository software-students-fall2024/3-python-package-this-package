import pytest
from calculator import parse_eq, correct_calculator, wrong_calculator, calculator

@pytest.mark.parametrize("equation, expected", [
    ("3 + 5 / 2", ([3, 5, 2], ['+', '/'])),
    ("10 + 4 * 2", ([10, 4, 2], ['+', '*'])),
    ("4 + 8", ([4, 8], ['+'])),
    ("4 / 2 - 1", ([4, 2, 1], ['/', '-'])),
    ("2 +", "Invalid equation: Equation must have even spaces between numbers and operations."),
    ("3.5 + 1", "Invalid equation: Decimals are not allowed."),
    ("+ 5 - 2", "Invalid equation: Cannot start or end with an operator or space.")
])
def test_parse_eq(equation, expected):
    assert parse_eq(equation) == expected

@pytest.mark.parametrize("numbers, operators, expected", [
    ([3, 5, 6], ['+', '/'], 4), 
    ([10, 4, 2], ['-', '*'], 2), 
    ([4, 8], ['+'], 12),
    ([4, 2, 1], ['/', '-'], 1)
])
def test_correct_calculator(numbers, operators, expected):
    assert correct_calculator(numbers, operators) == expected

@pytest.mark.parametrize("numbers, operators", [
    ([3, 5, 6], ['+', '/']),
    ([10, 4, 2], ['-', '*']),
    ([4, 8], ['+']),
    ([4, 2, 1], ['/', '-'])
])
def test_wrong_calculator(numbers, operators):
    result = wrong_calculator(numbers, operators)
    assert isinstance(result, int)
    assert result != correct_calculator(numbers, operators)
