# CLASE ABSTRACTA: Base para CancionSolo y CancionColaboracion

from abc import ABC, abstractmethod


class Cancion(ABC):
    #Clase base abstracta. Obliga a implementar info() y get_numero_artista().

    # Variables de clase: contadores GLOBALES (compartidos entre todas las canciones)
    total_canciones_plataforma = 0
    reproducciones = 0

    def __init__(self, titulo, artista_principal, duracion_seg, genero, **kwargs):
        #artista_principal es OBJETO Artista (no string) para navegación.
        super().__init__(**kwargs)
        self.__titulo = titulo
        self.__artista_principal = artista_principal
        self.__duracion_seg = duracion_seg
        self.__genero = genero
        self.__reproducciones_cancion = 0
        Cancion.total_canciones_plataforma += 1

    # PROPERTIES: Acceso controlado
    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista_principal(self):
        return self.__artista_principal

    @property
    def duracion_seg(self):
        return self.__duracion_seg

    @property
    def genero(self):
        return self.__genero

    @property
    def reproducciones_cancion(self):
        return self.__reproducciones_cancion

    # SETTERS: Validación de datos
    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self.__titulo = valor
        else:
            raise ValueError("El título debe ser texto no vacío")

    @duracion_seg.setter
    def duracion_seg(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__duracion_seg = valor
        else:
            raise ValueError("La duración debe ser positiva")

    @genero.setter
    def genero(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self.__genero = valor
        else:
            raise ValueError("El género debe ser texto no vacío")

    def __str__(self):
        return self.__titulo

    def repros(self):
        #Incrementa DOS contadores: individual (esta canción) + global (plataforma).
        self.__reproducciones_cancion += 1
        Cancion.reproducciones += 1
        print(f"Reproduciendo: {self.__titulo} - {self.__artista_principal.nombre}")

    def numero_reproducciones(self):
        #Muestra estadísticas a dos niveles: canción y plataforma.
        print(f"'{self.__titulo}': {self.__reproducciones_cancion} reproducciones")
        print(f"Total plataforma: {Cancion.reproducciones}")

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def get_numero_artista(self):
        pass