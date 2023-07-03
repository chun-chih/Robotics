#!/usr/bin/env python

import numpy as np
from cvxopt import matrix, solvers
from numpy.linalg import lstsq
import math as m

x_points = []
y_points = []
t_points = []
new_t = []
n_x = []
n_y = []
coeffi = []
coeffi_y = []
data_points = []

for i in range(1, 182):
    new_t.append((i-1)*0.1)

with open('/home/chunchih/final_proj/src/code/src/waypoints.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(' ')
        x = float(data[1])
        y = float(data[2])
        t = float(data[0])

        x_points.append(x)
        y_points.append(y)
        t_points.append(t)

        if len(x_points) == 10 and len(y_points) == 10 and len(t_points) == 10:
            break

def fit_polynomial(x_points, t_points, degree):
    # Convert the lists to numpy arrays
    x_points = np.array(x_points)
    t_points = np.array(t_points)

    # Create the matrix A for polynomial regression
    A = np.column_stack([t_points ** i for i in range(degree + 1)])

    # Use least squares to solve for the coefficients
    coeffs, _, _, _ = lstsq(A, x_points, rcond=None)

    return coeffs

# Degree of the polynomial
degree = 7

# Fit the polynomial
coefficients = fit_polynomial(x_points, t_points, degree)

# Print the coefficients
for i, coeff in enumerate(coefficients):
    #print(f"c{i+1} = {coeff}")
    coeffi.append(coeff)

# Evaluate the polynomial at new points

new_t = np.array(new_t)
new_x = sum(coeff * (new_t ** i) for i, coeff in enumerate(coefficients))
#print("Fitted values at new points:")
for t, x in zip(new_t, new_x):
    #print(f"t = {t}, x = {x}")
    n_x.append(x)
#print(".................................................")


def fit_polynomial_y(y_points, t_points, degree):
    # Convert the lists to numpy arrays
    y_points = np.array(y_points)
    t_points = np.array(t_points)

    # Create the matrix A for polynomial regression
    A = np.column_stack([t_points ** i for i in range(degree + 1)])

    # Use least squares to solve for the coefficients
    coeffs, _, _, _ = lstsq(A, y_points, rcond=None)

    return coeffs

# Degree of the polynomial
degree = 7

# Fit the polynomial
coefficients = fit_polynomial(y_points, t_points, degree)

# Print the coefficients
for i, coeff in enumerate(coefficients):
    #print(f"c{i+1} = {coeff}")
    coeffi_y.append(coeff)

# Evaluate the polynomial at new points

new_t = np.array(new_t)
new_y = sum(coeff * (new_t ** i) for i, coeff in enumerate(coefficients))
#print("Fitted values at new points:")
for t, y in zip(new_t, new_y):
    #print(f"t = {t}, y = {y}")
    n_y.append(y)

for x, y, t in zip(n_x, n_y, new_t):
    data_points.append((x, y, t))

#print("data_points:",data_points)

# Save the combined dataset to a text file
with open('/home/chunchih/final_proj/src/code/src/trajectory.txt', 'w') as file:
    for data in data_points:
        file.write(f"{data[2]} {data[0]} {data[1]} {4} {0}\n")
print("save it into trajectory.txt")