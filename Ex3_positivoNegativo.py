numero = float(input("Ingrese un número: "))

#Validar si tiene un solo digito
if numero == 0:
    print("El número es neutro")
elif numero > -9 and numero < 9 :
    print("El número es de un solo digito")
    if numero > 0:
        print("es positivo")
    else:
        print("y es negativo")
