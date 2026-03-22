# HERENCIA: Extiende Cancion | POLIMORFISMO: 1 artista vs múltiples en Colab

from canciones.clase_Cancion import Cancion


class CancionSolo(Cancion):
    #Canción de 1 artista. __numero_artistas siempre = 1.

    total_canciones_solo = 0  # Contador específico para estadísticas separadas

    def __init__(self, titulo, artista_principal, duracion_seg, genero, album=None, **kwargs):
        #album=None indica single (no pertenece a ningún álbum).
        super().__init__(titulo=titulo, artista_principal=artista_principal,
                         duracion_seg=duracion_seg, genero=genero, **kwargs)
        self.__album = album
        self.__numero_artistas = 1
        CancionSolo.total_canciones_solo += 1

    @property
    def album(self):
        return self.__album

    @property
    def numero_artistas(self):
        return self.__numero_artistas

    @album.setter
    def album(self, valor):
        if valor is None or (isinstance(valor, str) and len(valor) > 0):
            self.__album = valor
        else:
            raise ValueError("El álbum debe ser None o texto")

    def info(self):
        #SOBRESCRITURA: Muestra 1 artista (polimorfismo vs Colaboración).
        if self.album:
            return f"'{self.titulo}' de {self.artista_principal.nombre} ({self.album})"
        return f"'{self.titulo}' de {self.artista_principal.nombre} (Single)"

    def get_numero_artista(self):
        #IMPLEMENTACIÓN: Siempre retorna 1.
        return 1

    @classmethod
    def estadisticas_canciones_solo(cls):
        print(f"\n Canciones Solo: {cls.total_canciones_solo}")