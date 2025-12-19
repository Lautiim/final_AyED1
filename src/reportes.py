import re

def ver_juegos(datos: list[dict]) -> None:
    """Funcion para mostrar todos los juegos en la lista de datos.

    Pre: Recibe la lista de datos donde buscar.

    Post: No devuelve nada, solo muestra los juegos en pantalla.
    """
    assert isinstance(datos, list), "Los datos deben ser una lista."
    assert len(datos) > 0, "La lista de datos no puede estar vacia."

    for juego in datos:
        print(f"Nombre: {juego.get('Name', 'Desconocido')}")
        print(f"Plataforma: {juego.get('Platform', 'Desconocido')}")
        print(f"Ventas Globales: {juego.get('Global_Sales', 0)}")
        print("-" * 40)

def buscar_juegos_por_plataforma(plataforma: str, datos: list[dict]) -> list[dict]:
    """Funcion para buscar juegos segun el nombre o parte del nombre de la plataforma. No discrimina mayusculas de minusculas.
    
    Pre: Recibe el nombre o parte del nombre de la plataforma a buscar y la lista de datos donde buscar.

    Post: Devuelve una lista de diccionarios con los juegos encontrados.
    """
    assert isinstance(plataforma, str), "El nombre de la plataforma debe ser un String."
    assert len(plataforma) > 0, "El nombre de la plataforma no puede estar vacio."
    assert isinstance(datos, list), "Los datos deben ser una lista."
    assert len(datos) > 0, "La lista de datos no puede estar vacia."

    # Por comprension, si la plataforma ingresada esta en el nombre de la plataforma del juego, lo agregamos a los resultados
    resultados = [juego for juego in datos if plataforma.lower() in juego.get("Platform", "").lower()] # b - realizmos la busqueda sin discriminar mayusculas de minusculas

    return resultados # Devolvemos la lista de resultados encontrados

def precio_ventas_globales_pokemons(datos: list[dict]) -> list[dict]:
    """Funcion para obtener el precio de ventas globales de los pokemons. Solo se puede usar buscar con expresiones regulares

    Pre: Recibe la lista de datos donde buscar.

    Post: Devuelve un diccionario con dos columnas (Nombre y Global_Sales).
    """
    lista_resultados = []
    re.compile(r"p[oó]k[eé]m[oó]n", re.IGNORECASE)

    return lista_resultados