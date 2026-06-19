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