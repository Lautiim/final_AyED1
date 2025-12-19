import utils

def importar_datos(ruta: str, lista: list=[]) -> list[dict]:
    """Funcion para importar datos desde un archivo CSV y almacenarlos en una lista.
    Solo utiliza las columnas Name, Platform, Year, Genre, Publisher, Global_Sales

    Pre: Recibe la ruta del archivo CSV y una lista vacía o existente (por defecto esta vacia).

    Post: Devuelve una lista de diccionarios (usa la primer fila como encabezado) con los datos importados del archivo CSV.
    """
    assert isinstance(ruta, str), "La ruta ingresada no es valida, debe ser ser un String."
    assert isinstance(lista, list), "La lista no es de tipo lista."

    _lista = lista # Se obtiene la lista desde los argumentos
    encabezados_validos = ["Name", "Platform", "Year", "Genre", "Publisher", "Global_Sales"] # Estos son los encabezados que vamos a utilizar

    try:
        with open(ruta, "r", encoding="utf-8") as archivo: # Abrimos el archivo en modo lectura
            # Vamos a utilizar las columnas Name, Platform, Year, Genre, Publisher, Global_Sales

            encabezados = [columna.strip() for columna in archivo.readline().split(",")] # Leemos la primera fila para obtener los encabezados
            indices_validos = [i for i in range(len(encabezados)) if encabezados[i] in encabezados_validos] # Obtenemos los indices de los encabezados validos
            encabezados = [columna for columna in encabezados if columna in encabezados_validos] # Filtramos los encabezados válidos

            fila = archivo.readline() # Leemos una linea
            while fila: # Mientras haya una fila iteramos
                valores_completos = [valor.strip() for valor in fila.split(",")] # Obtenemos los valores de un elemento, diviendolo con "," y los guardamos en una lista
                valores = [valores_completos[i] for i in indices_validos if i < len(valores_completos)] # Filtramos los valores válidos

                registro = {encabezados[i]: valores[i] for i in range(len(encabezados))} # Generamos un diccionario con la info del elemento y sus encabezados, limitando la creacion hasta len(encabezados)
                _lista.append(registro) # Apilamos el registro a la lista

                fila = archivo.readline() # Leemos otra linea para repetir en la siguiente iteracion.

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta obtenida: {ruta}")

    if len(_lista) == 0:
        print("No hay datos para mostrar.")
    else:
        print(f"Archivo cargado con exito, se cargaron {len(_lista)} juegos.")
        input("Presione ENTER para continuar...")
    return _lista

if __name__ == "__main__":
    utils.limpiar_pantalla()
    ruta = "./data/prueba.csv"
    datos = importar_datos(ruta)
    print(datos)