print("calculdora")

print("1. sumar") 
print("2. restar")
print("3. multiplicar")
print("4. dividir")
print ("salir")

def calcular (num1,num2,opcion ):

    if opcion ==1:

        return num1+num2
    
    elif opcion == 2:


        return num1-num2
    
    elif opcion ==3:

        return num1*num2
    
    elif opcion ==4:

        while  num2 == 0:



            print ("no se puede divir por cero")

            num2 = int (input("vuelva a ingresar el divisor "))

            return num1/num2



    

opcion = int (input("ingrese una opcion: "))


while opcion > 0 and opcion < 5:

    if opcion ==1:

        print ("sumando")

        num1 = int(input("ingrese el primer valor "))
        num2 = int(input("ingrese el segundo valor "))

        resultado = calcular(num1,num2,opcion )

        print (f"el resultado es: {resultado}")

        
    elif opcion == 2:  
        num1 = int(input("ingrese el primer valor "))
        num2 = int(input("ingrese el segundo valor "))

        resultado = calcular(num1,num2,opcion )

        print (f"el resultado es: {resultado}")

    elif opcion == 3:
        num1 = int(input("ingrese el primer valor "))
        num2 = int(input("ingrese el segundo valor "))

        resultado = calcular(num1,num2,opcion )


        print (f"el resultado es: {resultado}")

    elif opcion == 4: 
        num1 = int(input("ingrese el primer valor "))
        num2 = int(input("ingrese el segundo valor "))

        resultado = calcular(num1,num2,opcion )

    opcion = int (input("ingrese una opcion: "))   


      