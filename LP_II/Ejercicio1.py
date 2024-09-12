peso = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
IMC = peso / estatura**2
print(f"El Indice de Masa corporal es: {IMC:.2f}")