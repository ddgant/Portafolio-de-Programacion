# Función para saludar según la hora ingresada en formato de 24 horas
def saludar_segun_hora(hora):
    # Convierte la hora ingresada a entero
    hora = int(hora)

    # Comprueba si la hora ingresada es menor a 18 (6 PM)
    if hora < 18:
        return "Buenos días"
    else:
        return "Es tiempo de dormir"

# Solicita al usuario que ingrese la hora
hora_ingresada = input("Ingrese la hora en formato de 24 horas (0-23): ")

# Llama a la función
print(saludar_segun_hora(hora_ingresada))
