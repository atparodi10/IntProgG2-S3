# Cálculo del salario neto de un empleado 

salario_bruto = float(input("Ingrese el salrio bruto: "))

iva_renta = salario_bruto * 0.10
seguroSocial = salario_bruto * 0.05
fondos_pension = salario_bruto * 0.03

descuentos = iva_renta + seguroSocial + fondos_pension

salario_neto = salario_bruto - descuentos

print("-----SALARIO TOTAL-----")
print(f"Salario Bruto: {salario_bruto: .2f}")
print(f"Impuesto Sobre la Renta: {iva_renta: .2f}")
print(f"Seguro Social: {seguroSocial: .2f}")
print(f"Fondos Pensionales: {fondos_pension: .2f}")
print(f"Salario Neto: {salario_neto: .2f}")
