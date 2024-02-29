
from ___ui import obtener_parametros_usuario, mostrar_resultados
from __api import consultar_datos_api

def main():
    # Obtener parámetros del usuario
    departamento, limite_registros = obtener_parametros_usuario()

    # Consultar la API
    resultados = consultar_datos_api(departamento, limite_registros)

    # Mostrar resultados
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()
