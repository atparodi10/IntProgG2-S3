#  Cálculo de área y perímetro de un rectángulo 
base = float(input("Ingrese la base de su rectángulo: "))
altura = float(input("Ingrese la altura de su rectángulo: "))

area = base * altura

perimetro = 2 * (base+ altura) 
print(f"Área: {area: .2f}")
print(f"perimetro: {perimetro: .2f}")

