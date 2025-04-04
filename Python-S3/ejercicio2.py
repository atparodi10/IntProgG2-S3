# Leer x cantidad de producto comprado a x precio, aplica el iva 15%
# Descuento de 10%
# Mostrar el total antes del iva
# Monto de descuento
# total a pagar

# Se debe leer el nombre del cliente y mostrar una factura

print("="*20)
print("Sistema de Facturación")
print("="*20)
while True:
    nombre = input("Ingresa el nombre del cliente: ").strip()
    if nombre:
        break
    print("El campo está vacío. Complete el espacio.")

while True:
    apellido = str(input("Ingrese el apellido del cliente: "))
    if apellido:
        break
    print("El campo está vacío. Completa el espacio.")

while True:
    nombre_producto = str(input("Ingrese el nombre del prodcuto a facturar: "))
    if nombre_producto:
        break
    print("El campo está vacío. Completa el espacio.")
    
precio_original = float(input("Ingresa el precio del producto: "))
while precio_original <= 0:
    print("Ingrese una cantidad valida.")
    precio_original = float(input("Ingresa el precio del producto: "))

cantidad_producto = float(input(f"Ingresa la cantidad de {nombre_producto} a facturar: "))
while cantidad_producto <= 0:
    print("Ingresa una cantidad valida.")
    cantidad_producto = float(input(f"Ingresa la cantidad de {nombre_producto} a facturar: "))

precio_sinDescuento = (precio_original * 0.15) + precio_original
iva = precio_original * 0.15
monto_descuento = precio_original * 0.10
precio_descuento = precio_original - monto_descuento
precio_total = precio_descuento + iva
nombre_completo = nombre + " " + apellido

import os
press_key = input("Presiona una tecla para continuar...")
os.system("cls || clear")

print("-"*5,"FACTURA", "-"*5)
print(f"Nombre del Cliente: {nombre_completo}")
print(f"Producto: {nombre_producto}")
print(f"Cantidad a Facturar: {cantidad_producto}")
print(f"Precio del producto: {precio_original: .2f}$")
print(f"IVA(15%): {iva: .2f}$")
print(f"Descuento 10%: {monto_descuento: .2f}$")
print(f"Total: {precio_descuento: .2f}$")
print(f"Total +IVA: {precio_total: .2f}$")
print("\n")
print("Productos \t Cantidad \t total")
print(f"{nombre_producto:>10} {cantidad_producto:>10} {precio_original:>10}$ {precio_total:>10}$")
print("-"*20)
