# Función para sumar todos los números reales hasta un número dado
def sumaR(numero):
    suma = 0
    # Utilizamos un bucle for para ir sumando de número hasta llegar al pedido
    for i in range(1, numero + 1):
        suma += i
    return suma

# Solicita al usuario que ingrese un número
numeroUsuario = int(input("Ingrese un número entero: "))

# Llama a la función para sumar los números y muestra el resultado
resultado = sumaR(numeroUsuario)
print("La suma de todos los números reales hasta", numeroUsuario, "es:", resultado)
