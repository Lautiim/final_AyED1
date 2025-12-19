import os
import sys

def limpiar_pantalla():
    """Funcion para limpiar la pantalla de la consola."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')