# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    potencia_2 = lambda x: x**2
    pot_3 = potencia_2(3)

    print('El número 3 elevado al cuadrado es:', pot_3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    numeros_potencia = list(map(lambda x: x**2, numeros))

    print(numeros_potencia)

    print("terminamos")