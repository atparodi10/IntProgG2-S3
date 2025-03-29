# haga un programa que digite el precio, cantidad y total a facturar y luego aplique el 10% de descuento

producto = (str(input("Nombre del producto: ")))
while producto == "" or producto == " ":
    print("Nombre de producto vacío. Intente nuevamente.")
    producto = (str(input("Nombre del producto: ")))

precio = (float(input("Precio del producto: ")))
while precio <= 0:
    print("Precio de producto ínvalido. Intente nuevamente.")
    precio = (float(input("Precio del producto: ")))
    
cantidad = (int(input("Cantidad a facturar: ")))
while cantidad <= 0:
    print("Cantidad de producto ínvalido. Intente nuevamente.")
    cantidad = (int(input("Cantidad a facturar: ")))

total = cantidad * precio
descuento = total * 0.10
total_a_pagar = total -descuento 
print("-----FACTURA-----")
print(f"Producto:{producto}")
print(f"Cantidad:{cantidad}")
print(f"Precio:{precio: .2f}")
print(f"Total:{total: .2f}")
print(f"descuento 10%:{descuento: .2f}")
print(f"Total a pagar:{total_a_pagar: .2f}")
print("--------------------")
