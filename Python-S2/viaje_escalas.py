#  Cálculo del tiempo total de un viaje con escalas

duracion = float(input("Ingrese la duración del primer tramo del vuelo: "))
while duracion <= 0: 
    print("Ingresa una cantidad valida: ")
    duracion = float(input("Ingrese la duración del primer tramo del vuelo: "))

primer_escala = float(input("Ingrese la duración de la primer escala: "))
while primer_escala <= 0: 
    print("Ingresa una cantidad valida: ")
    primer_escala = float(input("Ingrese la duración de la primer escala: "))

segundo_tramo = float(input("Ingrese la duración del segundo tramo del vuelo: "))
while segundo_tramo <= 0: 
    print("Ingresa una cantidad valida: ")
    primer_escala = float(input("Ingrese la duración de la primer escala: "))

segunda_escala = float(input("Ingrese la duración de la segunda escala: "))
while segunda_escala <= 0: 
    print("Ingresa una cantidad valida: ")
    segunda_escala = float(input("Ingrese la duración de la segunda escala: "))
    
tercer_tramo = float(input("Ingrese la duración del tercer tramo del vuelo: "))
while tercer_tramo <= 0: 
    print("Ingresa una cantidad valida: ")
    tercer_tramo = float(input("Ingrese la duración del tercer tramo del vuelo: "))

duracion_total = duracion + primer_escala
duracion_total += segundo_tramo
duracion_total += segunda_escala
duracion_total += tercer_tramo

print(f"Total de Duración del vuelo: {duracion_total: .2f}")
   
