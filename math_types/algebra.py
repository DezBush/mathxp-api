import random
import math
from sympy import symbols, Eq, solve

def generate_linear_equation_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    equation = f"{a}x + {b} = {c}"
    solution = (c - b) / a
    return {"problem": equation, 
            "solution": solution
    }

def generate_quadratic_equation_problem():
    a = random.randint(1, 5)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    equation = f"{a}x^2 + {b}x + {c} = 0"
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        solution = "No real solution"
    else:
        solution_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        solution = (solution_1, solution_2)
    return {"problem": equation, 
            "solution": solution
    }

def generate_system_of_equations_problem():
    x, y = symbols('x y')
    a1, b1, c1 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    a2, b2, c2 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    eq1 = Eq(a1*x + b1*y, c1)
    eq2 = Eq(a2*x + b2*y, c2)
    solution = solve((eq1, eq2), (x, y))
    return {"problem": f"{a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}", 
            "solution": solution
    }

def generate_inequality_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    inequality = f"{a}x - {b} > {c}"
    solution = f"x > {(c + b) / a}"
    return {"problem": inequality, 
            "solution": solution
    }

def generate_exponential_equation_problem():
    base = random.randint(2, 5)
    exponent = random.randint(2, 5)
    result = base ** exponent
    equation = f"{base}^x = {result}"
    solution = exponent
    return {"problem": equation, 
            "solution": solution
    }

def generate_logarithmic_equation_problem():
    a = random.randint(2, 5)
    b = random.randint(1, 10)
    equation = f"log(x) + log(x - 1) = {a}"
    solution = b + 1  # Approximate for simple problems
    return {"problem": equation, 
            "solution": solution
    }