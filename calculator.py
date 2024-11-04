import random
from shutdown import shutdown_system

def parse_eq(equation):
    if '.' in equation:
        return "Invalid equation: Decimals are not allowed."
    if equation.strip()[0] in '+-*/' or equation.strip()[-1] in '+-*/ ':
        return "Invalid equation: Cannot start or end with an operator or space."
    
    parse_e = equation.split()

    if len(parse_e) % 2 == 0:
        return "Invalid equation: Equation must have even spaces between numbers and operations."
    
    numbers = []
    operators = []
    for i, t in enumerate(parse_e):
        if i % 2 == 0:
            if t.isdigit():
                numbers.append(int(t))
            else:
                return "Invalid equation: Expected a number."
        else:
            if t in '+-*/':
                operators.append(t)
            else:
                return "Invalid equation: Expected an operator."
    
    return numbers, operators

def correct_calculator(numbers, operators):
    i = 0
    while i < len(operators):
        if operators[i] in ('*', '/'):
            if operators[i] == '*':
                result = numbers[i] * numbers[i + 1]
            elif operators[i] == '/':
                if numbers[i + 1] != 0:
                    result = numbers[i] / numbers[i + 1] 
                else:
                    return "Can't do division by zero"
            numbers[i:i + 2] = [result]
            operators.pop(i)
        else:
            i += 1
    
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '-':
            result -= numbers[i + 1]

    return result

def wrong_calculator(numbers, operators):
    if operators:
        all_operators = ['+', '-', '*', '/']
        for i in range(len(operators)):
            current_op = operators[i]
            new_list = [o for o in all_operators if o != current_op]
            operators[i] = random.choice(new_list)
    result = correct_calculator(numbers, operators)
    if result == correct_calculator(numbers[:], operators[:]):
        result += random.choice([-1, 1]) 
    return result

def calculator(equation):
    if random.random() <= 0.05:
        shutdown_system()
        
    if not isinstance(equation, str):
        print("Warning: Please pass the equation as a string, like '4 - 8 + 9 / 2'.")
        return
    
    result = parse_eq(equation)
    if isinstance(result, str):
        print(result)
        return
    numbers, operators = result
    probabilities = random.randint(0,1)
    if probabilities > 0.7:
        result = wrong_calculator(numbers[:], operators[:])
    else:
        result = correct_calculator(numbers[:], operators[:])
    print(f"The result is: {result}")



