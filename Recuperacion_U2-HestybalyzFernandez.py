# Resolver por metodo de Newton-Raphson

from sympy import symbols, diff, lambdify, exp

VD = symbols('VD')

f_simb = (VD/100) + 0.1 * (exp(3*VD)) - 0.07
df_simb  = diff(f_simb, VD)

f = lambdify(VD, f_simb, 'numpy')
df = lambdify(VD, df_simb, 'numpy')

xo = 0
tolerancia = 0.001
error = 100
iteracion = 1

while error>=tolerancia:
    x_new = xo - (f(xo) / df(xo))
    x_new = float(x_new)

    error = abs( (x_new - xo) / x_new) * 100

    print(f'{iteracion}\t{x_new:.2f}\t{error:.2f}%')

    xo = x_new
    iteracion += 1