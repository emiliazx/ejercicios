from random import randint

# Solicitar los límites del rango
while True:
    limite_inferior = int(input("Ingrese limite inferior: "))
    limite_superior = int(input("Ingrese limite superior: "))
    
    if limite_inferior < limite_superior:
        break
    else:
        print("El límite inferior debe ser menor que el superior. Intente nuevamente.")

# Generar número aleatorio
numero_secreto = randint(limite_inferior, limite_superior)
print(f"Número secreto generado: {numero_secreto}")
intentos = []
adivino = False

# Primer intento
intento = int(input("\nIntente adivinar: "))
intentos.append(intento)

if intento == numero_secreto:
    print("Felicitaciones, adivinó en el primer intento.")
    adivino = True
else:
    if intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

# Segundo intento (si no acertó en el primero)
if not adivino:
    intento = int(input("\nIntente de nuevo: "))
    intentos.append(intento)
    
    if intento == numero_secreto:
        print("Felicitaciones, adivinó en su segundo intento.")
        adivino = True
    else:
        if intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        
        # Dar pista comparando con el primer intento
        print("Te daré una pista:")
        distancia_primer = abs(intentos[0] - numero_secreto)
        distancia_segundo = abs(intentos[1] - numero_secreto)
        
        if distancia_segundo < distancia_primer:
            print(f"El numero que buscas está más cerca de {intentos[1]} que de {intentos[0]}")
        else:
            print(f"El numero que buscas está más cerca de {intentos[0]} que de {intentos[1]}")

# Tercer intento (si no acertó en los anteriores)
if not adivino:
    intento = int(input("\nIntente la ultima vez: "))
    
    if intento == numero_secreto:
        print("Felicitaciones, adivinó en su tercer intento.")
    else:
        print("Perdiste.")
        print(f"El número era: {numero_secreto}")