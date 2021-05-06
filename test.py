'''
*Universidad Sergio Arboleda
*Autor: Johan David Villalba Rodriguez
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:johan.villalba01@gmail.com
'''
from functionE import rbf_network
from Cy_functionE import Cy_rbf_network
import numpy as np
import time

### Inicializar
Py_D = 5
Py_N = 1500
Py_X = np.array([np.random.rand(Py_N) for d in range(Py_D)]).T
Py_beta = np.random.rand(Py_N)
Py_theta = 10


### Tiempos
inicio = time.time()
rbf_network(Py_X, Py_beta, Py_theta)
tiempoPy = time.time() - inicio

inicio = time.time()
Cy_rbf_network(Py_X, Py_beta, Py_theta)
tiempoCy = time.time() - inicio

speedUp = round(tiempoPy/tiempoCy,3)

print("Tiempo Python: {} \n".format(tiempoPy))
print("Tiempo Cython: {} \n".format(tiempoCy))
print("SpeedUp: {} \n".format(speedUp))