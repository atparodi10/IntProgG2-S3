nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = (int(input("Introduce tu edad: ")))
peso_lb = (float(input("Introduce tu peso en libras: ")))

nombre_completo = nombre + " " + apellido
peso_kg = peso_lb / 2.204
edad_dias = edad * 365

print("Tu nombre completo es: ", nombre_completo)
print("Tu edad en dias es de: ", edad_dias)
print(f"Tu peso en kg es de: {peso_kg: .2f}")
