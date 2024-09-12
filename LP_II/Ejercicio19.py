texto = input("Ingresa un texto: ")
lon = len(texto)
invertir = ""
for i in range(lon -1, -1, -1):
    invertir += texto[i]
print(invertir)