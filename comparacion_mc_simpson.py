"""
Compara integración por Simpson vs Monte Carlo.

I = int_0^1 ... int_0^1 prod_i sin(pi x_i) dx_1 ... dx_d

"""

# Procedemos a importar librerías útiles para realizar nuestra integración de Monte Carlo. 

import numpy as np 
import scipy.integrate import simpson 
import time

d = 3 # dimensión del problema
valor_analitico = (2.0 / np.pi)**d

print(f"---Integración en d={d} ---")
print(f"Analítico: {valor_analitico:.8f}")
#------------------------------------------------------------------------
# MÉTODO DE MONTECARLO
#------------------------------------------------------------------------

N_total_mc = 10**6

t0_mc = time.time()

'''
TODO
Implemente acá el método de Monte Carlo para la integral I.
integral_mc =
'''

t1_mc = time.time()
error_mc = abs(integral_mc - valor_analitico)

print(
    f"Monte Carlo: {integral_mc:.8f}"
    f"(Error: {error_mc:.8f}, Tiempo: {t1_mc - t0_mc:.4f}s)"
)

# ---------------------------------------------------------------------------------------------------------
# MÉTODO DE SIMPSON
# ---------------------------------------------------------------------------------------------------------

N_simpson = 10
N_total_simpson = N_simpson**d

t0_simpson = time.time()

x_1d = np.linspace(0, 1, N_simpson)
malla = np.meshgrid(*]x_1d] * d, indexing="ij")

Z = np.prod([np.sin(np.pi * m) for m in malla], axis=0)

integral_simpson = Z
for _ in range(d):
    integral_simpson = simpson(integral_simpson, x=x_1d, axis=0)

t1_simpson = time.time()
error_simpson = abs(integral_simpson - valor_analitico)

print(
    f"Simpson: {integral_simpson:.8f}"
    f"(Error: {error_simpson:.8f}, Tiempo: {t1_simpson - t0_simpson:.4f}s)"
)