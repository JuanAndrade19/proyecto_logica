# -*- coding: utf-8 -*-
"""Ejercicio_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-THO-0phxxebeLYoAHUE8C49PXJYjTMu
"""

# Algoritmo para calcular el costo total del estacionamiento

TARIFA = 1.500

horas = int(input("Ingrese el tiempo de estacionamiento en horas: "))
minutos = int(input("Ingrese el tiempo de estacionamiento en minutos: "))

horasTotales = horas
if minutos > 0:
    horasTotales += 1

CostoTotal = horasTotales * TARIFA

print(f"El costo total por estacionamiento es: ${CostoTotal:.3f}")