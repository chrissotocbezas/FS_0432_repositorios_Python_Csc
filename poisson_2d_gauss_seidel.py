import numpy as np
import matplotlib.pyplot as plt

# Se proceden a importar las librerías necesarias para el método de Guass-Seidel. 
# Se proceden a invocar funciones de la misma forma que se hizo para el método de poisson_2d_jacobi
# Gracias a lo anterior, podremos definir el algoritmo para ejecutar el método. 

# Procedemos a definir la función fuente

def f(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi *y)

def solucion_exacta(x, y):
    return -np.sin(np.pi * x) * np.sin(np.pi * y) / (2.0 * (np.pi)**2)

# En la función anterior, procedimos a definir la solución exacta de la función

# Procedemos a ejecutar el método de Gauss-Seidel