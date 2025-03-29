# Calcular el promedio de 5 asignaturas
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre:
        break
    print("El campo está vacío. Complete el espacio.")


while True:
    apellido = input("Ingresa tu apellido: ").strip()
    if apellido:
        break
    print("El campo está vacío. Complete el espacio.")
    
materias = []
calificaciones = []
suma = 0

for i in range(5):
    while True: 
        materia = input("Ingresa el nombre de la materia: ").strip()
        if materia:
            materias.append(materia)
            break
        print("El nombre de la materia no puede estar vacío. Intente otra vez.")

    while True:
        try:
            calificacion = (float(input(f"Ingresa la calificacion de {materia}: ")))
            if  0 <= calificacion <= 100:
                calificaciones.append(calificacion)
                suma += calificacion
                break
            else:
                print("La calificación no puede ser menor a 0 o mayor a 100. Intente de nuevo.")
            
        except ValueError:
            print("Por favor. Ingrese un número válido.")
    
print("\nResumen de Calificaciones:")
for i in range(5):
    print(f"{materias[i]}: {calificaciones[i]}")
    
promedio = suma / 5

print(f"\nPromedio de calificaiones: {promedio: .2f}")
        
        
    
        