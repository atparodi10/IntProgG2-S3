# Cálculo del índice de masa corporal (IMC)

peso_kg = float(input("Ingrese su peso en KG: "))
while peso_kg <= 0:
    print("Ingresa una cantidad valida.")
    peso_kg = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))
while altura <= 0:
    print("Ingresa una cantidad valida.")
    altura = float(input("Ingrese su altura en metros: "))

altura2 = altura * altura
imc = peso_kg / altura2 
imc *= 100
imc /= 100

print("-----RESUMEN-----")
print(f"Peso: {peso_kg: .2f}KG")
print(f"Altura: {altura: .2f}M")
print(f"IMC: {imc: .2f}")
print("-----CLASIFICACIÓN IMC-----")
print("Bajo peso: IMC menor a 18.5 \nPeso normal: IMC entre 18.5 y 24.9 \nSobrepeso: IMC entre 25.0 y 29.9 \nObesidad: IMC de 30.0 o más \nObesidad grave o de alto riesgo: IMC mayor a 40") 
