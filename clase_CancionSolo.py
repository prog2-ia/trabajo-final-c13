#clase_CancionSolo.py
from clase_Cancion import Cancion
class CancionSolo(Cancion):
    total_canciones_solo=0
    def __init__(self,titulo,artista_principal,duracion_seg,genero,album=None,**kwargs):
        super().__init__(titulo=titulo,artista_principal=artista_principal,duracion_seg=duracion_seg,genero=genero,**kwargs)
        self.__album=album
        self.__numero_artistas=1
        CancionSolo.total_canciones_solo+=1

    @property
    def album(self):
        return self.__album

    @property
    def numero_artistas(self):
        return self.__numero_artistas

    @album.setter
    def album(self,valor):
        if valor is None or (isinstance(valor,str) and len(valor)>0):
            self.__album=valor
        else:
            raise ValueError("El álbum debe ser None o un texto no vacío")

    def info(self):
        if self.album:
            return f"La canción es '{self.titulo}' de {self.artista_principal} y pertenece al álbum '{self.album}'"
        else:
            return f"La canción es '{self.titulo}' de {self.artista_principal} y es un single"

    def get_numero_artista(self):
        return 1

    @classmethod
    def estadisticas_canciones_solo(cls):
        """Muestra estadísticas de todas las canciones solo registradas."""
        print(f"\n✓ Canciones Solo registradas: {cls.total_canciones_solo}")