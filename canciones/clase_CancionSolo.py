# HERENCIA: Extiende Cancion | POLIMORFISMO: 1 artista vs múltiples en Colab
# IMPLEMENTA: Herencia simple, Properties, Sobrecarga __str__ y __repr__

from typing import Any, Optional
from canciones.clase_Cancion import Cancion


class CancionSolo(Cancion):

    #Canción de 1 artista. __numero_artistas siempre = 1.
    #Diferencia clave vs Colaboración: sin artistas secundarios.


    # Contador específico para estadísticas separadas
    total_canciones_solo: int = 0

    def __init__(self, titulo: str, artista_principal: Any, duracion_seg: int, genero: str,
                 album: Optional[str] = None, **kwargs: Any) -> None:

        #Inicializa canción solo.
        #- album=None indica single (no pertenece a ningún álbum).
        #- __numero_artistas siempre = 1 (inmutable).

        super().__init__(titulo=titulo, artista_principal=artista_principal,
                         duracion_seg=duracion_seg, genero=genero, **kwargs)

        self.__album: Optional[str] = album
        self.__numero_artistas: int = 1

        CancionSolo.total_canciones_solo += 1

    # ========================================================================
    # PROPERTIES: Acceso controlado (lectura)
    # ========================================================================

    @property
    def album(self) -> Optional[str]:
        return self.__album

    @property
    def numero_artistas(self) -> int:
        return self.__numero_artistas

    # ========================================================================
    # SETTERS: Validación antes de modificar
    # ========================================================================

    @album.setter  # type: ignore[no-redef, attr-defined]
    def album(self, valor: Optional[str]) -> None:
        #Álbum puede ser None (single) o texto no vacío.
        if valor is None or (isinstance(valor, str) and len(valor) > 0):
            self.__album = valor
        else:
            raise ValueError("El álbum debe ser None o texto")

    # ========================================================================
    # SOBRECARGA DE OPERADORES: Representación
    # ========================================================================

    def __str__(self) -> str:
        #Representación string: incluye álbum si existe.
        if self.album:
            return f"'{self.titulo}' de {self.artista_principal.nombre} ({self.album})"
        return f"{self.titulo} de {self.artista_principal.nombre} (Single)"

    def __repr__(self) -> str:

        #Representación para debugging.
        #Formato: ClassName(atributo='valor', ...)

        return f"CancionSolo(titulo='{self.titulo}', artista='{self.artista_principal.nombre}',duracion={self.duracion_seg}s)"

    # ========================================================================
    # SOBRESCRITURA DE MÉTODOS ABSTRACTOS: Polimorfismo
    # ========================================================================

    def info(self) -> str:

        #SOBRESCRITURA: Muestra 1 artista (polimorfismo vs Colaboración).
        #Diferencia: NO incluye "ft." ni lista de secundarios.

        if self.album:
            return f"'{self.titulo}' de {self.artista_principal.nombre} ({self.album})"
        return f"'{self.titulo}' de {self.artista_principal.nombre} (Single)"

    def get_numero_artista(self) -> int:

        #IMPLEMENTACIÓN: Siempre retorna 1.
        #Diferencia vs Colaboración: número fijo, no dinámico.

        return 1

    @classmethod
    def estadisticas_canciones_solo(cls) -> None:
        #Mét. de clase: muestra total de canciones solo creadas.
        print(f"\n Canciones Solo: {cls.total_canciones_solo}")