# Conversión de unidades de tiempo

total_segundos = int(input("Ingrese la cantidad total de segundos: "))
while total_segundos <= 0: 
    print("Los segundos no pueden ser igual o menores a 0. Intente otra vez.")
    total_segundos = int(input("Ingrese la cantidad total de segundos: "))

horas = total_segundos // 3600

segundos_restantes = total_segundos - (horas * 3600)

minutos = segundos_restantes // 60

segundos = segundos_restantes - (minutos * 60)

print(f"Tiempo convertido:\n {horas}, horas \n {minutos}, minutos \n{segundos}, segundos")
