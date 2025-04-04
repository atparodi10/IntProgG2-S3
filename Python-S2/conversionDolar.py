# Conversión de una cantidad en dólares a distintas monedas 

dolares = float(input("Ingresa la cantidad en dólares: "))
while dolares < 0: 
    print("Ingresa una cantidad valida: ")
    dolares = float(input("Ingresa la cantidad en dólares: "))

cambio_euro = float(input("Inregresa la tasa de cambio de Dólares a Euros: "))
while cambio_euro <= 0:
    print("Ingresa una cantidad valida.")
    cambio_euro = float(input("Inregresa la tasa de cambio de Dólares a Euros: "))

cambio_libras = float(input("Inregresa la tasa de cambio de Dólares a Libras Esterlinas: "))
while cambio_libras <= 0:
    print("Ingresa una cantidad valida.")
    cambio_euro = float(input("Inregresa la tasa de cambio de Dólares a Libras Esterlinas: "))

cambio_yenes = float(input("Inregresa la tasa de cambio de Dólares a Yenes: "))
while cambio_yenes <= 0:
    print("Ingresa una cantidad valida.")
    cambio_euro = float(input("Inregresa la tasa de cambio de Dólares a Yenes: "))

euros = dolares * cambio_euro
libras = dolares * cambio_libras
yenes = dolares * cambio_yenes

print(f"Cantidad en Dólares: {dolares: .2f}")
print(f"Valor en Euros: {euros: .2f}")
print(f"Valor en Libras Esterlinas: {libras: .2f}")
print(f"Valor en Yenes: {yenes: .2f}")


    
    