# Calcular el area de un circulo a=pi*r9^2
import math

radio = (float(input("Ingrese el radio de su circulo: ")))

area = math.pi * pow(radio, 2)

print(f"Área del círculo según el radio: {area: .2f}")

