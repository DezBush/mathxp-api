import numpy as np

def generate_matrix_multiplication_problem():
    matrix1 = np.random.randint(1, 10, (2, 2))
    matrix2 = np.random.randint(1, 10, (2, 2))
    solution = np.dot(matrix1, matrix2)
    return {"problem": f"Multiply the matrices: {matrix1} and {matrix2}", 
            "solution": solution.tolist()
    }

def generate_determinant_problem():
    matrix = np.random.randint(1, 10, (2, 2))
    solution = np.linalg.det(matrix)
    return {"problem": f"Find the determinant of matrix {matrix}", 
            "solution": round(solution, 2)
    }

def generate_eigen_problem():
    matrix = np.random.randint(1, 10, (2, 2))
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return {
        "problem": f"Find the eigenvalues and eigenvectors of matrix {matrix}",
        "solution": {"eigenvalues": eigenvalues.tolist(), "eigenvectors": eigenvectors.tolist()}
    }

def generate_dot_product_problem():
    vector1 = np.random.randint(1, 10, 3)
    vector2 = np.random.randint(1, 10, 3)
    solution = np.dot(vector1, vector2)
    return {"problem": f"Find the dot product of vectors {vector1} and {vector2}", 
            "solution": solution
    }

def generate_cross_product_problem():
    vector1 = np.random.randint(1, 10, 3)
    vector2 = np.random.randint(1, 10, 3)
    solution = np.cross(vector1, vector2)
    return {"problem": f"Find the cross product of vectors {vector1} and {vector2}", 
            "solution": solution.tolist()
    }