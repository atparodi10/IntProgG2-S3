#  Cálculo del volumen de un cilindro y su área superficial 
import math
radio_cilindro = float(input("Ingrese el radio de su cilindro: "))
while radio_cilindro <= 0:
    print("Ingrese una dimensión valida.")
    radio_cilindro = float(input("Ingrese el radio de su cilindro: "))

altura_cilindro = float(input("Ingrese la altura de su cilindro: "))
while altura_cilindro <= 0:
    print("Ingrese una altura valida: ")
    altura_cilindro = float(input("Ingrese la altura de su cilindro: "))

area_base = math.pi * pow(radio_cilindro, 2)
volumen_cilindro = area_base * altura_cilindro
area_lateral = 2 * math.pi * radio_cilindro * altura_cilindro
area_superficial = area_lateral + (2*area_base)

print(f"Radio del cilindro: {radio_cilindro: .2f}")
print(f"Altura del cilindro: {altura_cilindro: .2f}")
print(f"Volumen del cilindro: {volumen_cilindro: .2f}")
print(f"Área Superficial: {area_superficial: .2f}")
    