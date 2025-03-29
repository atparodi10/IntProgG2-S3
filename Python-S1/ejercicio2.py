# Realizar un programa que segun un área en m2 ingresada por el usuario muestre cuantos ladrillos se 
# utilizaran para cubrir el área total, teniendo en cuenta que se necesitan 20 ladrillos para cubrir 1m2

alto = (float(input("Ingrese el alto de su área: ")))
ancho = (float(input("Ingrese el ancho de su área: ")))

area = alto * ancho
total = area * 20 

print(f"Area a cubir: {area: .2f}m2")
print(f"Total de ladrillos para cubrir el área: {total: .2f}")


