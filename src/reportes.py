import re

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

def precio_ventas_globales_pokemons(datos: list[dict]) -> float:
    """Funcion para obtener el precio de ventas globales de los pokemons.

    Pre: Recibe la lista de datos donde buscar.

    Post: Devuelve el precio de ventas globales de los pokemons.
    """
    assert isinstance(datos, list), "Los datos deben ser una lista."
    assert len(datos) > 0, "La lista de datos no puede estar vacia."

    total_ventas = sum(float(juego.get("Global_Sales", 0)) for juego in datos if "Pokemon" in juego.get("Name", "").lower())
    return total_ventas