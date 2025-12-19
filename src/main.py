import utils
import datos
import reportes

ruta_csv = "./data/prueba.csv"

def menu_principal() -> None:
    """Funcion para mostrar el menu principal y manejar las opciones."""

    while True:
        print("-" * 30 + " Opciones " + "-" * 30)
        print("A. Importar Datos")
        print("B. Buscar juegos por nombre de plataforma.")
        print("C. Exportar juegos por plataforma filtrados.")
        print("D. Precio de ventas globales de pokemos.")
        print("Z. Salir")

        opcion = input("Seleccione una opcion: ").strip().upper()
        if opcion == "A":
            lista_datos = datos.importar_datos(ruta_csv)
            utils.limpiar_pantalla()
        elif opcion == "B":
            plataforma = input("Ingrese el nombre o parte del nombre de la plataforma: ") # a - Solicitar al usuario una parte del nombre a buscar
            if len(lista_datos) == 0:
                print("No hay datos para mostrar.")
            else:
                resultado = reportes.buscar_juegos_por_plataforma(plataforma, lista_datos) # Llamamos a la funcion para buscar juegos por plataforma
                
                if len(resultado) == 0:
                    print("No hay datos para mostrar.")
                else:
                    print("Busqueda completada. Revise los resultados.") # Informamos al usuario que la busqueda se completo
                    print(resultado)
        #elif opcion == "C":
        #    plataforma = input("Ingrese el nombre de la plataforma: ")
        #    datos.exportar_juegos_por_plataforma(plataforma)
        #elif opcion == "D":
        #    reportes.precio_ventas_globales_pokemons()
        elif opcion == "Z":
            break
        else:
            print("Opcion no valida, intente nuevamente.")

if __name__ == "__main__":
    utils.limpiar_pantalla()
    lista_datos = []
    print("Bienvenido al sistema :D")
    menu_principal()