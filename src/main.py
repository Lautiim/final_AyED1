import utils
import datos
import reportes


def menu_principal() -> None:
    """Funcion para mostrar el menu principal y manejar las opciones."""
    _lista_datos = []

    while True:
        print("-" * 30 + " Opciones " + "-" * 30)
        print("A. Importar Datos")
        print("B. Buscar juegos por nombre de plataforma.")
        print("C. Exportar juegos por plataforma filtrados.")
        print("D. Precio de ventas globales de pokemos.")
        print("E. Ver todos los juegos.")
        print("Z. Salir")

        opcion = input("Seleccione una opcion: ").strip().upper()
        if opcion == "A":
            lista_datos = datos.importar_datos(ruta_csv)
            utils.limpiar_pantalla()
        elif opcion == "B":
            plataforma = input("Ingrese el nombre o parte del nombre de la plataforma: ") # a - Solicitar al usuario una parte del nombre a buscar
            if not lista_datos:
                utils.limpiar_pantalla()
                print("No hay datos para mostrar.")
                input("Presione Enter para continuar...")
            else:
                resultado = reportes.buscar_juegos_por_plataforma(plataforma, lista_datos) # Llamamos a la funcion para buscar juegos por plataforma
                
                if len(resultado) == 0:
                    print("No hay datos para mostrar.")
                else:
                    print("Busqueda completada. Revise los resultados.") # Informamos al usuario que la busqueda se completo
                    # Mostramos en formato de tabla los resultados
    

                    print("Name | Year | Genre | Publisher |")
                    print("-" * 50)
                    for juego in resultado:
                        print(f"{juego.get('Name', 'Desconocido')} | {juego.get('Year', 'Desconocido')} | {juego.get('Genre', 'Desconocido')} | {juego.get('Publisher', 'Desconocido')} |")                    
        #elif opcion == "C":
        #    plataforma = input("Ingrese el nombre de la plataforma: ")
        #    datos.exportar_juegos_por_plataforma(plataforma)
        #elif opcion == "D":
        #    reportes.precio_ventas_globales_pokemons()
        elif opcion == "E":
            utils.limpiar_pantalla()
            print("Juegos:")
            print("-" * 40)
            reportes.ver_juegos(lista_datos)
        elif opcion == "Z":
            break
        else:
            print("Opcion no valida, intente nuevamente.")

if __name__ == "__main__":
    ruta_csv = "./data/prueba.csv"

    utils.limpiar_pantalla()
    print("Bienvenido al sistema :D")
    menu_principal()