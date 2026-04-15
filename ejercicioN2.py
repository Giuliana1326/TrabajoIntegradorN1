# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    len_string = lambda x: len(x)

    print(len_string('jesus gonzalez'))

    # 2)
    # Lista de string
    palabras = ['love', 'casa', 'programacion']

    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto en cada iteración

    palabras_len = list(map(lambda x: len(x), palabras))

    print(palabras_len)

    print("terminamos")