numero = int(input("Ingrese un numero: "))
atras = ""
for i in range(numero, -1, -1):
    if i != numero:
        atras += ", "
    atras += str(i)
print(atras)