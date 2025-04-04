#  Cálculo del precio final de un producto con impuestos y descuentos

precio_original = float(input("Ingrese el precio del prodcuto: "))
while precio_original <= 0:
    print("Ingresa una cantidad valida.")
    precio_original = float(input("Ingrese el precio del prodcuto: "))

descuento = float(input("Ingresa el porcentaje del descuento(0-100): "))
while descuento < 0 or descuento > 100:
    print("Ingrese una cantidad valida.")
    descuento = float(input("Ingresa el porcentaje del decuento: "))

valor_descuento = descuento / 100

descuento_total = valor_descuento * precio_original
precio_descuento = precio_original - descuento_total

iva = float(input("Ingresa el valor del iva(0-100): "))
while iva < 0 or iva >100:
    print("Ingrese una cantidad valida.")
    iva = float(input("Ingresa el valor del iva(0-100): "))

iva_valor = iva / 100

precio_iva = precio_descuento * iva_valor
precio_final = precio_descuento + precio_iva

precio_real = precio_original * iva_valor
precio_real = precio_original + precio_real

print("-----FACTURA-----")
print(f"Precio: {precio_original: .2f}")
print(f"Descuento: {descuento}%")
print(f"Descuento Aplicado: {descuento_total: .2f}")
print(f"Precio con descuento: {precio_descuento: .2f}")
print(f"IVA: {iva}%")
print(f"IVA Aplicado: {precio_iva: .2f}")
print(f"Precio final(): {precio_final: .2f}")
print(f"Precio real sin descuento: {precio_real: .2f}")


