edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("Puede entrar gratis")
elif 4 <= edad <= 18:
    print("Debe pagar $5")
else:
    print("Debe pagar 10$")