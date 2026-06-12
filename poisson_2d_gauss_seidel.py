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
# Definimos la función para calcular el error máximo

def error_maximo(u, u_exacta):
    return np.max(np.abs(u-u_exacta))

# Procedemos a ejecutar el método de Gauss-Seidel con una función
def graficar_mapa(u, titulo, nombre_archivo, cmap):
    plt.figure(figsize=(8,5))

    # Procedemos a usar U(x_i, y_j)

    plt.imshow(u.T, origin="lower", extent=[0,1,0,1], cmap="viridis")

    plt.colorbar(label="u(x,y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)
    plt.close()
