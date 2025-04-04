# Cálculo del tiempo total de una película con comerciales

duracion_minutos = int(input("Ingresa la duración de la peliculas en minutos: "))
while duracion_minutos <= 0:
    print("Ingrese una cantidad valida.")
    duracion_minutos = int(input("Ingresa la duracion de la peliculas en minutos: "))

comerciales_previos = int(input("Ingresa la duración de los comerciles previos: "))
while comerciales_previos <= 0:
    print("Ingrese una cantidad valida.")
    comerciales_previos = int(input("Ingresa la duración de los comerciles previos: "))

pausa_comercial = int(input("Ingresa la cantidad de cada pausa comercial: "))
while pausa_comercial <= 0:
    print("Ingrese una cantidad valida.")
    pausa_comercial = int(input("Ingresa la cantidad de cada pausa comercial: "))

duracion_pausa_comercial = int(input("Ingresa la duración de cada pausa comercial: "))
while duracion_pausa_comercial <= 0:
    print("Ingrese una cantidad valida.")
    duracion_pausa_comercial = int(input("Ingresa la duración de cada pausa comercial: "))


total_Pausacomerciales = pausa_comercial * duracion_pausa_comercial
total_comerciales = total_Pausacomerciales + comerciales_previos 
duracion_total = duracion_minutos + total_comerciales

print(f"Duración de la película: {duracion_minutos}")
print(f"Cantidad total de comerciales: {total_comerciales}")
print(f"Duración total de la película: {duracion_total}")

