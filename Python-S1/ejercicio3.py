# Calcular el interes del 3% a pagar al cabo de 5 años
capital = (float(input("Ingrese la cantidad del préstamo: ")))

interes = capital * 0.03 * 5 #forumla del interes simple interes = capital * interes * años
deuda = interes + capital

print(f"El total del interes acumulado al cabo de 5 años es de: {interes: .2f}")
print(f"Total de deuda: {deuda: .2f}")