from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random
from sympy import symbols, diff, integrate, limit
from math_types import calculus, algebra, linear_algebra, statistics

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calculus")
async def get_random_calc_problem():
    problem_type = random.choice(["derivative", "integral", "limit"])
    if problem_type == "derivative":
        return calculus.generate_derivative_problem()
    elif problem_type == "integral":
        return calculus.generate_integral_problem()
    elif problem_type == "limit":
        return calculus.generate_limit_problem()

@app.get("/calculus/{problem_type}")
async def get_specific_calc_problem(problem_type: str):
    if problem_type == "derivative":
        return calculus.generate_derivative_problem()
    elif problem_type == "integral":
        return calculus.generate_integral_problem()
    elif problem_type == "limit":
        return calculus.generate_limit_problem()
    else:
        raise HTTPException(status_code=404, detail="Problem type not available")
    
@app.get("/algebra")
async def get_random_alg_problem():
    problem_type = random.choice([
        "linear", "quadratic", "system_of_equations", "inequality", "exponential", "logarithmic"])
    if problem_type == "linear":
        return algebra.generate_linear_equation_problem()
    elif problem_type == "quadratic":
        return algebra.generate_quadratic_equation_problem()
    elif problem_type == "system_of_equations":
        return algebra.generate_system_of_equations_problem()
    elif problem_type == "inequality":
        return algebra.generate_inequality_problem()
    elif problem_type == "exponential":
        return algebra.generate_exponential_equation_problem()
    elif problem_type == "logarithmic":
        return algebra.generate_logarithmic_equation_problem()

@app.get("/algebra/{problem_type}")
async def get_random_alg_problem(problem_type: str):
    if problem_type == "linear":
        return algebra.generate_linear_equation_problem()
    elif problem_type == "quadratic":
        return algebra.generate_quadratic_equation_problem()
    elif problem_type == "system_of_equations":
        return algebra.generate_system_of_equations_problem()
    elif problem_type == "inequality":
        return algebra.generate_inequality_problem()
    elif problem_type == "exponential":
        return algebra.generate_exponential_equation_problem()
    elif problem_type == "logarithmic":
        return algebra.generate_logarithmic_equation_problem()
    else:
        raise HTTPException(status_code=404, detail="Problem type not available")
    
@app.get("/linear_algebra")
async def get_random_linear_algebra_problem():
    problem_type = random.choice([
        "matrix_multiplication", "determinant", "eigen", "dot_product", "cross_product"
    ])
    if problem_type == "matrix_multiplication":
        return linear_algebra.generate_matrix_multiplication_problem()
    elif problem_type == "determinant":
        return linear_algebra.generate_determinant_problem()
    elif problem_type == "eigen":
        return linear_algebra.generate_eigen_problem()
    elif problem_type == "dot_product":
        return linear_algebra.generate_dot_product_problem()
    elif problem_type == "cross_product":
        return linear_algebra.generate_cross_product_problem()
    
@app.get("/linear_algebra/{problem_type}")
async def get_random_linear_algebra_problem(problem_type: str):
    if problem_type == "matrix_multiplication":
        return linear_algebra.generate_matrix_multiplication_problem()
    elif problem_type == "determinant":
        return linear_algebra.generate_determinant_problem()
    elif problem_type == "eigen":
        return linear_algebra.generate_eigen_problem()
    elif problem_type == "dot_product":
        return linear_algebra.generate_dot_product_problem()
    elif problem_type == "cross_product":
        return linear_algebra.generate_cross_product_problem()
    
@app.get("/statistics")
async def get_random_statistics_problem():
    problem_type = random.choice([
        "probability", "mean_median_mode", "std_variance", 
        "normal_distribution", "binomial_distribution", "hypothesis_testing"
    ])
    if problem_type == "probability":
        return statistics.generate_probability_problem()
    elif problem_type == "mean_median_mode":
        return statistics.generate_mean_median_mode_problem()
    elif problem_type == "std_variance":
        return statistics.generate_std_variance_problem()
    elif problem_type == "normal_distribution":
        return statistics.generate_normal_distribution_problem()
    elif problem_type == "binomial_distribution":
        return statistics.generate_binomial_distribution_problem()
    elif problem_type == "hypothesis_testing":
        return statistics.generate_hypothesis_testing_problem()
    
@app.get("/statistics/{problem_type}")
async def get_random_statistics_problem(problem_type: str):
    if problem_type == "probability":
        return statistics.generate_probability_problem()
    elif problem_type == "mean_median_mode":
        return statistics.generate_mean_median_mode_problem()
    elif problem_type == "std_variance":
        return statistics.generate_std_variance_problem()
    elif problem_type == "normal_distribution":
        return statistics.generate_normal_distribution_problem()
    elif problem_type == "binomial_distribution":
        return statistics.generate_binomial_distribution_problem()
    elif problem_type == "hypothesis_testing":
        return statistics.generate_hypothesis_testing_problem()
    