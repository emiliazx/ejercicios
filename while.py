 #Pide al usuario dos números y una operación (+, -, *, /).
#Usa if/elif/else para realizar la operación correcta.
#Usa try-except para manejar errores si ingresa texto en lugar de números o intenta dividir por cero.
#Desafío extra: Envuelve todo en un while para que la calculadora siga funcionando hasta que el usuario escriba "salir".

print("bienvenido a tu calculadora\n")
    

num1= int(input("\ningrese el primer numero: "))
num2 = int(input("\ningrese el segundo numero: "))

while True :

    
    print("\nmenu de opciones")
    print("1.sumar")
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.salir")




    opcion = input("ingrese la opcion que quiere realizar:")

    

    if opcion == "1":
        resultado_suma = num1 + num2
        print(f"\n el resultado de la suma es: {resultado_suma}")
    
        num1= int(input("\ningrese el primer numero: "))
        num2 = int(input("\ningrese el segundo numero: "))


    elif  opcion =="2":
        resultado_resta = num1 - num2
        print(f"\n el resultado de la resta es: {resultado_resta}") 
        num1= int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))


    elif opcion =="3":
        resultado_multiplicacion  = num1 * num2
        print(f"\n el resultado de la multiplicacion es: {resultado_multiplicacion}")
        num1= int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))

    elif opcion == "4":
        resultado_division = num1 / num2
        print(f"\n el resultado de la division es:  {resultado_division}")
    elif opcion == "5":

        print("haz salido de la calculadora")
        break



     
     
