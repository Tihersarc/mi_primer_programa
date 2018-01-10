numero_ganador = 3

numero_usuario = int(input("Adivina un numero de 0-10: "))

if  numero_ganador == numero_usuario:
    print("Has adivinado!")
else:
    print("Has perdido")