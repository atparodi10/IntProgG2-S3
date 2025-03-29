# Dividir dos numeros enteros ingresador por el usuario

dividendo = (int(input("Ingresa el dividendo: ")))
divisor = (int(input("Ingresa el divisor: ")))

while divisor == 0:
    print("No definido. No se puede dividir entre 0.")
    divisor = (int(input("Ingresa el divisor: ")))
    
cociente = dividendo / divisor

print(f"{dividendo} / {divisor} = {cociente: .2f}")
