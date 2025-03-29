# Conversion de cordobas a dolares segun el tipo de cambio ingresado por el usuario

print("-----CONVERTIR CÓRDOBAS A DÓLARES-----")
cordobas = (float(input("Ingrese la cantidad de C$: ")))
while cordobas <= 0:
     print("Monto inválido. La cantidad no puede ser igual o menor a 0.")
     cordobas = (float(input("Ingrese la cantidad de C$: ")))
    
conversion = (float(input("Ingrese el tipo de cambio: ")))
while conversion <= 0:
     print("Monto inválido. La cantidad no puede ser igual o menor a 0.")
     conversion = (float(input("Ingrese el tipo de cambio: ")))
    
dolares =  cordobas / conversion


print("----------")
print(f"Cantidad a cambiar:{cordobas: .2f}C$")
print(f"Tipo de cambio a dólares:{conversion: .2f}C$")
print(f"Total convertido a córdobas:{dolares: .2f}US$")