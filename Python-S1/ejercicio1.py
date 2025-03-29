#Pedir al usuario nombre, apellido, edad y peso en lb para mostrar nombre concatenado, peso en kg y edad en dias

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = (int(input("Ingrese su edad: ")))
peso_lb = (float(input("Ingrese su peso en lb: ")))

nombre_completo = nombre + " " + apellido
edad_dias = edad * 365
peso_kg = peso_lb / 2.204

print("Su nombre completo es: ",nombre_completo)
print("Su edad en días: ", edad_dias)
print(f"Su peso en Kg es de: {peso_kg: .2f}")