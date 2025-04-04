# Convertir fahrenheit a celcius y kelvin
tem_fah = float(input("Ingrese la temperaura en grados Fahrenheit: "))
temp_cel = tem_fah - 32
temp_cel = temp_cel * 5
temp_cel = temp_cel / 9
temp_kel = temp_cel + 273.15

print(f"{temp_cel: .2f}")
print(f"{temp_kel: .2f}")