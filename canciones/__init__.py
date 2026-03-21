# Este archivo hace que la carpeta 'canciones' sea un paquete Python.
# Sin él, los imports como 'from canciones.clase_Cancion import Cancion' no funcionarían.

from canciones.clase_Cancion import Cancion
from canciones.clase_CancionSolo import CancionSolo
from canciones.clase_CancionColaboracion import CancionColaboracion

# __all__ define qué clases se importan al usar 'from canciones import *'
__all__ = ['Cancion', 'CancionSolo', 'CancionColaboracion']