# Este archivo hace que la carpeta 'artistas' sea un paquete Python.
# Sin él, los imports como 'from artistas.clase_Artista import Artista' no funcionarían.

from artistas.clase_Artista import Artista
from artistas.clase_ArtistaSolista import ArtistaSolista
from artistas.clase_ArtistaBanda import ArtistaBanda

# __all__ define qué clases se importan al usar 'from artistas import *'
__all__ = ['Artista', 'ArtistaSolista', 'ArtistaBanda']