# Programa: Evaluación del nivel de compromiso de sesiones

# Matriz con los datos de las sesiones
# [ID del Cliente, Duración en segundos, Número de clics]

sesiones = [
    [101, 250, 15],
    [102, 45, 2],
    [103, 120, 5],
    [104, 200, 4],
    [105, 90, 10],
    [106, 30, 12]
]

# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):

    if duracion < 60 or clics < 3:
        return "Bajo"

    elif (duracion > 180 and clics > 2) or clics > 8:
        return "Alto"

    else:
        return "Medio"


# Función para generar el informe
def generar_informe(matriz):

    print("\n===== INFORME DE COMPROMISO DE CLIENTES =====")
    print("---------------------------------------------")
    print("ID del Cliente\tNivel de Compromiso")
    print("---------------------------------------------")

    for sesion in matriz:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(
            duracion, clics
        )

        print(f"{id_cliente}\t\t{clasificacion}")

    print("---------------------------------------------")


# Llamado de la función principal
generar_informe(sesiones)
