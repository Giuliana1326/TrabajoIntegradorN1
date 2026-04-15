# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # 1)
    # Filtrar IDs entre 1 y 10 inclusive
    personal_1_10 = [x for x in accesos if 1 <= x <= 10]

    print('Personal del 1 al 10:', personal_1_10)
    print('Cantidad de personal en ese rango:', len(personal_1_10))

    # 2)
    # Filtrar IDs válidos
    id_validos = [3, 4, 7, 8, 15]

    personal_valido = [x for x in accesos if x in id_validos]

    print('Personal con acceso válido:', personal_valido)

    print("terminamos")