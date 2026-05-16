# CLASE ABSTRACTA: Base para CancionSolo y CancionColaboracion

from abc import ABC, abstractmethod
from typing import Any


class Cancion(ABC):
    #Clase base abstracta. Obliga a implementar info() y get_numero_artista().

    # Variables de clase: contadores GLOBALES (compartidos entre todas las canciones)
    total_canciones_plataforma: int = 0
    reproducciones: int = 0

    def __init__(self, titulo: str, artista_principal: Any, duracion_seg: int, genero: str, **kwargs: Any) -> None:
        #artista_principal es OBJETO Artista (no string) para navegación.
        super().__init__(**kwargs)
        self.__titulo: str = titulo
        self.__artista_principal: Any = artista_principal
        self.__duracion_seg: int = duracion_seg
        self.__genero: str = genero
        self.__reproducciones_cancion: int = 0
        Cancion.total_canciones_plataforma += 1

    # PROPERTIES: Acceso controlado
    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def artista_principal(self) -> Any:
        return self.__artista_principal

    @property
    def duracion_seg(self) -> int:
        return self.__duracion_seg

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def reproducciones_cancion(self) -> int:
        return self.__reproducciones_cancion

    # SETTERS: Validación de datos
    @titulo.setter  # type: ignore[no-redef, attr-defined]
    def titulo(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            from excepciones import ValorInvalidoError
            raise ValorInvalidoError("título",valor,"debe ser un texto no vacío")
        self.__titulo=valor

    @duracion_seg.setter  # type: ignore[no-redef, attr-defined]
    def duracion_seg(self,valor: int) -> None:
        from excepciones import ValorInvalidoError
        if not isinstance(valor, int):
            raise ValorInvalidoError("duración",valor,"debe ser un número entero")
        if valor <= 0:
            raise ValorInvalidoError("duración", valor, "debe ser mayor que 0")
        if valor > 25200:  #Máximo 7 horas
            raise ValorInvalidoError("duración",valor,"no puede superar las 7 horas (25200s)")
        self.__duracion_seg=valor


    @genero.setter  # type: ignore[no-redef, attr-defined]
    def genero(self,valor: str) -> None:
        from excepciones import ValorInvalidoError
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValorInvalidoError("género", valor, "debe ser un texto no vacío")
        self.__genero=valor

    def __str__(self) -> str:
        return self.__titulo

    def __eq__(self,otra: Any) -> bool:
        if not isinstance(otra,Cancion):
            return False
        return self.titulo.lower()==otra.titulo.lower()

    def __lt__(self,otra: Any) -> bool:
        if not isinstance(otra,Cancion):
            return NotImplemented
        return self.duracion_seg<otra.duracion_seg

    def __gt__(self,otra: Any) -> bool:
        if not isinstance(otra, Cancion):
            return NotImplemented #Le dice a Python: "no puedo comparar estos tipos"
        return self.duracion_seg > otra.duracion_seg

    def repros(self) -> None:
        #Incrementa DOS contadores: individual (esta canción) + global (plataforma).
        self.__reproducciones_cancion += 1
        Cancion.reproducciones += 1
        print(f"Reproduciendo: {self.__titulo} - {self.__artista_principal.nombre}")

    def numero_reproducciones(self) -> None:
        #Muestra estadísticas a dos niveles: canción y plataforma.
        print(f"'{self.__titulo}': {self.__reproducciones_cancion} reproducciones")
        print(f"Total plataforma: {Cancion.reproducciones}")

    @abstractmethod
    def info(self) -> str:
        pass

    @abstractmethod
    def get_numero_artista(self) -> Any:
        pass