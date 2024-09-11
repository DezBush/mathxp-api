from sympy import symbols, diff, integrate, limit
import random

x = symbols('x')

def generate_derivative_problem():
    degree = random.choice([2, 3])
    coefficients = [random.randint(1, 10) for _ in range(degree + 1)]
    polynomial = sum(c * x**i for i, c in enumerate(coefficients))
    derivative = diff(polynomial, x)
    problem = f"Find the derivative of {polynomial}"
    solution = str(derivative)
    return {"problem": problem, 
            "solution": solution
    }

def generate_integral_problem():
    degree = random.choice([2, 3])
    coefficients = [random.randint(1, 10) for _ in range(degree + 1)]
    polynomial = sum(c * x**i for i, c in enumerate(coefficients))
    integral = integrate(polynomial, x)
    problem = f"Find the indefinite integral of {polynomial}"
    solution = str(integral) + " + C"
    return {"problem": problem, 
            "solution": solution
    }

def generate_limit_problem():
    numerator = sum(random.randint(1, 10) * x**i for i in range(2))
    denominator = random.randint(1, 5) * (x + random.randint(1, 5))
    rational_function = numerator / denominator
    approach_value = random.choice([0, 1, 2])
    limit_result = limit(rational_function, x, approach_value)
    problem = f"Find the limit of {rational_function} as x approaches {approach_value}"
    solution = str(limit_result)
    return {"problem": problem, 
            "solution": solution
    }