from funciones import *


menu = "1 - Cargar la matriz\n2 - Existen numeros consecutivos?\n3 - Cantidad de ocurrencias de numeros consecutivos\n4 - Secuencias mas corta\n5 - Secuencia mas larga\n6 - Salir\n\n"

interactuar = True

while interactuar:

    numero = input(menu)
    match (numero):
        case "1":
            matriz = insertar_csv_en_matriz('/Users/macbook/data_final_20240923/data_final_20240923.csv')
            print("La matriz se cargo con exito")
            print("\n\n")

        case "2":
            resultados = buscar_consecutivos(matriz)
            print(resultados['resultado'])
            print(f"La cantidad de ocurrencias es: {resultados['cantidad_ocurrencias']}")
            printear_matriz(matriz, 10)
            print("\n\n")

            print(f"Secuencias de tres: {resultados['secuencias_tres']}")
            print(f"Secuencias de cuatro: {resultados['secuencias_cuatro']}")
            print(f"Secuencias de cinco: {resultados['secuencias_cinco']}")

        case "3":
            print(f"La secuencia mas corta es de {secuencia_mas_corta(matriz)}")
        case "6":
            interactuar = False