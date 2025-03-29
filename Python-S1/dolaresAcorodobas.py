# Conversion de dolares a cordobas segun el tipo de cambio ingresado por el usuario

print("-----CONVERTIR DÓLARES A CÓRDOBAS-----")
dolares = (float(input("Ingrese la cantidad de US$: ")))

while dolares <= 0: 
    print("Monto inválido. La cantidad no puede ser igual o menor a 0.")
    dolares = (float(input("Ingrese la cantidad de US$: ")))

cambio = (float(input("Ingrese el tipo de cambio: ")))
while cambio <= 0: 
    print("Monto inválido. La cantidad no puede ser igual o menor a 0.")
    cambio = (float(input("Ingrese la cantidad de US$: ")))
    
cordobas = dolares * cambio

print("----------")
print(f"Cantidad a cambiar:{dolares: .2f}US$")
print(f"Tipo de cambio:{cambio: .2f}C$")
print(f"Total convertido a córdobas:{cordobas: .2f}C$")

