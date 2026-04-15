# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # 1)
    # Convertir strings a enteros, reemplazando los no numéricos por 0

    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    lista_numeros = [int(x) if x.isdigit() else 0 for x in list_numeros_str]

    print(lista_numeros)

    # Prueba con números negativos

    list_numeros_str = ['-5', '-2', '3', '', '7', 'NaN']

    lista_numeros = [int(x) if x.lstrip('-').isdigit() else 0 for x in list_numeros_str]

    print(lista_numeros)

    print("terminamos")