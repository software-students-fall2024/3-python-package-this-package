from src.utilities import calculator

equations = [
    "3 + 6 * 8",
    "12 - 4 / 2 + 5",
    "7 * 5 - 3 / 1",
    "3 +",
    "3+6*8",
    "3 - 5 *",
    "+ 5 - 2",
    "4.5 + 3",
    5 + 3,
    "9 / 0 + 4"git
]

print("TESTING calculator(equation: str)\n")

for eq in equations:
    print(f"Equation: {eq}")
    calculator(eq)