def insertar_csv_en_matriz(path: str):
    # Lee un CSV e inserta esos datos en una matriz de 10x20
    #
    #    Argumento:
    #      path [str] -> Ruta del archivo CSV
    #    Retorna:
    #      matriz -> Matriz de 10x20 con los numeros cargados
    matriz = []

    with open(path, 'r') as archivo:
        lineas = archivo.readlines()

    
    for linea in lineas:
        fila = linea.strip().split(";")
        matriz.append(fila)
    
    return matriz


def printear_matriz(matriz, filas):
    for i in range(filas):
            print(matriz [i])
                

def buscar_consecutivos(matriz):
    # busca dentro de la matriz si hay numeros consecutivos y cuantos hay
    #
    #    Argumento:
    #      matriz [] -> Matriz leida del CSV
    #    Retorna:
    #      resultado [dict] -> diccionario con la leyenda y cantidad de ocurrencias
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = "NO EXISTEN NUMEROS CONSECUTIVOS"
    cantidad_ocurrencias = 0
    secuencias_tres = 0
    secuencias_cuatro = 0
    secuencias_cinco = 0


    #de izquierda a derecha y de arriba a bajo
    #la mas corta de 2 la mas larga de 5, 11 y 10 = 21 ocurrencias
    for i in range(0, filas ,1):
        for j in range(0, columnas ,1):
            numero_actual = int(matriz[i][j])
            
            if i > 0 and int(matriz[i - 1][j]) == numero_actual - 1:
                resultado = "EXISTEN NUMEROS CONSECUTIVOS"
                if  numero_actual - 2 == int(matriz[i][j - 2]):
                    secuencias_tres += 1
                else:
                    cantidad_ocurrencias += 1
                #matriz_ocurrencias[i] = numero_actual, int(matriz[i - 1][j])
                #cantidad_ocurrencias += 1

            if j > 0 and int(matriz[i][j - 1]) == numero_actual - 1:
                resultado = "EXISTEN NUMEROS CONSECUTTIVOS"
                if  numero_actual - 4 == int(matriz[i][j - 4]):
                    secuencias_cinco += 1
                    print()

                elif  numero_actual - 3 == int(matriz[i][j - 3]):
                    secuencias_cuatro += 1

                elif  numero_actual - 2 == int(matriz[i][j - 2]):
                    secuencias_tres += 1

                else:
                    cantidad_ocurrencias += 1

    #cantidad_ocurrencias += secuencias_tres

    resultados = {
        'resultado': resultado,
        'cantidad_ocurrencias': cantidad_ocurrencias,
        'secuencias_tres': secuencias_tres,
        'secuencias_cuatro': secuencias_cuatro,
        'secuencias_cinco': secuencias_cinco
    }

    return resultados


def secuencia_mas_corta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    secuencia_minima = []
    
    for i in range(filas):
        for j in range(columnas):
            numero_actual = int(matriz[i][j])
            secuencia_actual = [numero_actual]
            
            if i < filas - 1 and numero_actual + 1 == int(matriz[i + 1][j]):
                secuencia_actual.append(int(matriz[i + 1][j]))
            
            if j < columnas - 1 and numero_actual + 1 == int(matriz[i][j + 1]):
                secuencia_actual.append(int(matriz[i][j + 1]))

            if len(secuencia_actual) > 1 and (len(secuencia_actual) < len(secuencia_minima) or not secuencia_minima):
                secuencia_minima = secuencia_actual

    return  secuencia_minima




