'''
*Universidad Sergio Arboleda
*Autor: Johan David Villalba Rodriguez
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:johan.villalba01@gmail.com
'''
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize('Cy_functionE.pyx'))

setup(ext_modules=exts)