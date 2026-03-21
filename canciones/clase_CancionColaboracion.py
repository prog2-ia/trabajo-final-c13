# HERENCIA: Extiende Cancion | POLIMORFISMO: Múltiples artistas

from canciones.clase_Cancion import Cancion


class CancionColaboracion(Cancion):
    #Colaboración: 1 artista principal + N secundarios (lista de objetos).

    total_canciones_colaboracion = 0

    def __init__(self, titulo, artista_principal, duracion_seg, genero,
                 artistas_secundarios, album=None, **kwargs):
        #artistas_secundarios es LISTA de objetos Artista (no strings).
        super().__init__(titulo=titulo, artista_principal=artista_principal,
                         duracion_seg=duracion_seg, genero=genero, **kwargs)
        self.__artistas_secundarios = artistas_secundarios
        self.__album = album
        self.__numero_artistas = 1 + len(artistas_secundarios)
        CancionColaboracion.total_canciones_colaboracion += 1

    @property
    def artistas_secundarios(self):
        return self.__artistas_secundarios

    @property
    def album(self):
        return self.__album

    @property
    def numero_artistas(self):
        return self.__numero_artistas

    @artistas_secundarios.setter
    def artistas_secundarios(self, valor):
        if isinstance(valor, list):
            self.__artistas_secundarios = valor
            self.__numero_artistas = 1 + len(valor)
        else:
            raise ValueError("Los secundarios deben ser una lista")

    @album.setter
    def album(self, valor):
        if valor is None or (isinstance(valor, str) and len(valor) > 0):
            self.__album = valor
        else:
            raise ValueError("El álbum debe ser None o texto")

    def info(self):
        #SOBRESCRITURA: Muestra principal + secundarios (polimorfismo vs Solo).
        nombres = ", ".join([a.nombre for a in self.__artistas_secundarios])
        if self.__album:
            return f"'{self.titulo}': {self.artista_principal.nombre} ft. {nombres} ({self.__album})"
        return f"'{self.titulo}': {self.artista_principal.nombre} ft. {nombres} (Single)"

    def get_numero_artista(self):
        #IMPLEMENTACIÓN: 1 + longitud de secundarios.
        return f"{self.__numero_artistas} artistas"

    @classmethod
    def estadisticas_colaboraciones(cls):
        print(f"\n✓ Colaboraciones: {cls.total_canciones_colaboracion}")