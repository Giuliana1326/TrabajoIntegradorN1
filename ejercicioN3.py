# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas
import random


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # 1)
    # Lista del 0 al 10
    lista_0_10 = [x for x in range(11)]
    print(lista_0_10)

    # 2)
    # Tabla del 5
    tabla_5 = [x * 5 for x in range(11)]
    print(tabla_5)

    # 3)
    # 10 números aleatorios entre 1 y 30
    dias_mes = [random.randint(1, 30) for _ in range(10)]
    print(dias_mes)

    print("terminamos")