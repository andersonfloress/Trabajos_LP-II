frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contar = 0
for i in frase:
    if i == letra:
        contar += 1
print(f"La letra {letra} aparece {contar} veces ")