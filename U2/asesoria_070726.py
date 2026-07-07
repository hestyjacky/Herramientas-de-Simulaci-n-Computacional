from sympy import symbols, lambdify, exp
import matplotlib.pyplot as plt

Vd = symbols('Vd')
x_guess = 0

# ecuacion a resolver con newton-raphson
f = (1/50) * Vd + 10**-15 * (exp(38*Vd) - 1) - 0.06
calcular_f = lambdify(Vd, f, 'numpy')

# derivada de la ecuacion
df = f.diff(Vd)
calcular_df = lambdify(Vd, df, 'numpy')
error = 100
iteracion = 1

while error > 0.01:
    x_new = x_guess - (calcular_f(x_guess)/calcular_df(x_guess))
    error = abs(x_new - x_guess)
    print(f'{iteracion}  |  x_guess: {x_guess:.6f}  |  x_new: {x_new:.6f}  |  error: {error:.6f}')
    x_guess = x_new
    iteracion += 1



