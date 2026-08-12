from sympy import symbols, Matrix, lambdify, log, exp, cos, cofactors
import numpy as np

x, y = symbols('x y')

f1 = x - exp(y)
f2 = log(1 + x) - cos(y)

J = Matrix([ [f1.diff(x), f1.diff(y)], 
             [f2.diff(x), f2.diff(y)]])

F = Matrix([f1, f2])

F_num = lambdify( (x,y), F, 'numpy')
J_num = lambdify( (x,y), J, 'numpy')

X0 = np.array([1, 0])

iteracion = 1
max_iteracion = 5
tolerancia = 0.01
error = 100.0

# < >
while error > tolerancia and iteracion <= max_iteracion:
    F_eval = F_num( X0[0], X0[1]).flatten()
    J_eval = J_num( X0[0], X0[1])

    """
    inv_J = np.linalg.inv(J_eval) 
    X1 = X0 - inv_J @ F_eval
    """

    det = np.linalg.det(J_eval)

    # ADJUNTA Y TRANSPUESTA !!

    #print(J_eval, "\n---")

    transp = np.array([[J_eval[1,1], -J_eval[0,1]], [-J_eval[1,0], J_eval[0,0]]])
    # print(transp, "\n---")

    inv = (1 / det) * transp

    X1 = X0 - inv @ F_eval

    cambio = np.linalg.norm(X1 - X0)
    actual = np.linalg.norm(X1)
    error = (cambio / actual) * 100

    print(f"{iteracion:<3} |  {X1[0]:<9.4f} | {X1[1]:<9.4f} | {error:>7.2f} %")
    print('-' * 20)

    X0 = X1

    iteracion += 1
