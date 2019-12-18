"""
    Solution of the famous chinese problem in two ways with checking the time performance of both.
    There are only chickens and sheeps in the farm, 35 heads and 94 legs totally.
    How many chickens and how many sheeps are in the farm?
"""

import numpy as np
import time


def function_performance(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end-start


def solve_numpy(heads, legs):
    matrix = np.array([[1, 1], [2, 4]])  # coefficients of left-hand sides of equations in algebraic system
    solutions = np.array([heads, legs])  # right-hand sides of equations in system
    result = np.linalg.solve(matrix, solutions)  # returns numpy array with float elements
    if str(result[0])[-1] == '0' and str(result[1])[-1] == '0':  # check whether the solution is integer
        return int(result[0]), int(result[1])
    return 'No solutions!'


def solve_simple(heads, legs):
    for chickens in range(heads+1):
        sheeps = heads - chickens
        if (2*chickens)+(4*sheeps) == legs:
            return chickens, sheeps
    return 'No solutions!'


if __name__ == '__main__':
    heads = 35
    legs = 94
    solution_simple = solve_simple(heads, legs)
    solution_numpy = solve_numpy(heads, legs)
    print(solution_simple, solution_numpy)
    print(function_performance(solve_simple, heads, legs))
    print(function_performance(solve_numpy, heads, legs))
