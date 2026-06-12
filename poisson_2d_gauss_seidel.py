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

def graficar_error_convergencia(errores, nombre_archivo):
    plt.figure(figsize=(6, 4))
    plt.plot(errores, color="green") # Procedemos a cambiar el color de la gráfica
    plt.yscale("log") # Escala logarítmica para observar el decrecimiento exponencial del error
    plt.xlabel("Iteracion")
    plt.ylabel("Error de convergencia")
    plt.title("Error de convergencia (Gauss-Seidel)")
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)
    plt.close()

def main():
    N = 50 # Colocamos el número de iteraciones
    h = 1.0/N # Colocamos el paso
    tol = 1e-8
    max_iter = 200000

    # Colocamos el dominio para x y y

    x = np.linspace(0.0, 1.0. N+1) #N + 1 se realiza por el tema del paso
    y = np.linspace(0.0, 1.0, N+1)

    X, Y = np.meshgrid(x, y, indexing="ij")

    f = f(x,y)
    u_exacta = solucion_exacta(X,Y) # El arreglo para X y Y se utiliza para la solución u_exacta

    # NOTA: En Gauss-Seidel no requerimos u_new para el almacenamiento del bloque completo, ya que las actualizaciones ocurren sobre la misma matriz 'u'

    u = np.zeros((N+1, N+1))

    errores_convergencia = [] # Agregamos una lista en blanco para generar un lugar donde se pueda almacenar los arreglos de conveiencia

    iteracion = 0
    error_conv = 1.0

    while error_conv > tol and iteracion < max_iter:
        # Procedemos a guardar una copia exacta para evaluar la convergencia al final del paso completo

        u_old = u.copy()

        # Procedemos a realizar una actualización fila por fila consecutiva para logar un Gauss-Seidel real y donde apliquemos una formulación específica para vectores
        # Esto lo podemos conseguir mediante un bucle for para recorrer cada parte del arreglo matricial
        # AL recorrer i, la fila 'i-1' ya contiene los valores nuevos de esta iteración. 

        for i in range(1, N):
            u[i, 1:N] = 0.25 * (u[I+1, 1:N] + u[i-1, 1:N] + U[i, 2:N+1] + u[i, 0:N-1] - (h**2) *f[i, 1:N])
        
        error_conv = np.max(np.abs(u[1:N, 1:N] - u_old[1:N, 1:N]))
        errores_convergencia.append(error_conv)

        # Procedemos a incrementar el contador de iteraciones para que esto no recurra en un bucle infinito sin que estas se guarden

        iteracion += 1
