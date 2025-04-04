# Convertir de córdobas a euros

cordobas = float(input("Ingresa la cantidad de Córdobas: "))
while cordobas <= 0:
    print("Ingresa una cantidad valida.")
    cordobas = float(input("Ingresa la cantidad de Córdobas: "))

euros = cordobas / 43.08

print(f"Córdobas: {cordobas: .2f}")
print(f"Convertido a Euros: {euros: .2f}")