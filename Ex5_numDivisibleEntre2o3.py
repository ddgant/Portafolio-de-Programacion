def divisible_por_2_y_3(numero):
    divisible_por_2 = numero % 2 == 0
    divisible_por_3 = numero % 3 == 0

    if divisible_por_2 and divisible_por_3:
        return "El número es divisible entre 2 y 3"
    elif divisible_por_2:
        return "El número es divisible entre 2 pero no entre 3"
    elif divisible_por_3:
        return "El número es divisible entre 3 pero no entre 2"
    else:
        return "El número no es divisible ni entre 2 ni entre 3"

numero = int(input("Ingrese un número entero: "))
print(divisible_por_2_y_3(numero))