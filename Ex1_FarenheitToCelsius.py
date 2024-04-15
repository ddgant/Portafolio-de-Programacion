# Función para convertir grados Fahrenheit a Celsius
def fahrenheit_a_celsius(f):
    c = (f - 32) * 5/9
    return c

# Solicita al usuario que ingrese los grados en Fahrenheit
g_fahrenheit = float(input("Ingrese los grados Fahrenheit: "))

# Llama a la función para convertir los grados y muestra el resultado
g_celsius = fahrenheit_a_celsius(g_fahrenheit)
print("Grados Celsius:", g_celsius, " C°")