# HERENCIA: Extiende Cancion | POLIMORFISMO: Múltiples artistas
# IMPLEMENTA: Herencia múltiple implícita, Properties con validación

from typing import Any, Optional, List
from canciones.clase_Cancion import Cancion


class CancionColaboracion(Cancion):

    #Colaboración: 1 artista principal + N secundarios (lista de objetos).
    #Diferencia clave vs CancionSolo: número_artistas > 1


    # Variable de clase: contador específico para estadísticas
    total_canciones_colaboracion: int = 0

    def __init__(self, titulo: str, artista_principal: Any, duracion_seg: int, genero: str,
                 artistas_secundarios: List[Any], album: Optional[str] = None, **kwargs: Any) -> None:

        #Inicializa colaboración.
        #- artistas_secundarios es LISTA de objetos Artista (no strings).
        #- album=None indica single (no pertenece a ningún álbum).

        super().__init__(titulo=titulo, artista_principal=artista_principal,
                         duracion_seg=duracion_seg, genero=genero, **kwargs)

        self.__artistas_secundarios: List[Any] = artistas_secundarios
        self.__album: Optional[str] = album
        self.__numero_artistas: int = 1 + len(artistas_secundarios)

        CancionColaboracion.total_canciones_colaboracion += 1

    # ========================================================================
    # PROPERTIES: Acceso controlado (lectura)
    # ========================================================================

    @property
    def artistas_secundarios(self) -> List[Any]:
        return self.__artistas_secundarios

    @property
    def album(self) -> Optional[str]:
        return self.__album

    @property
    def numero_artistas(self) -> int:
        return self.__numero_artistas

    # ========================================================================
    # SETTERS: Validación antes de modificar
    # ========================================================================

    @artistas_secundarios.setter  # type: ignore[no-redef, attr-defined]
    def artistas_secundarios(self, valor: List[Any]) -> None:
        #Actualiza lista y recalcula número_artistas automáticamente.
        if isinstance(valor, list):
            self.__artistas_secundarios = valor
            self.__numero_artistas = 1 + len(valor)
        else:
            raise ValueError("Los secundarios deben ser una lista")

    @album.setter  # type: ignore[no-redef, attr-defined]
    def album(self, valor: Optional[str]) -> None:
        #Álbum puede ser None (single) o texto no vacío.
        if valor is None or (isinstance(valor, str) and len(valor) > 0):
            self.__album = valor
        else:
            raise ValueError("El álbum debe ser None o texto")

    # ========================================================================
    # SOBRESCRITURA DE MÉTODOS ABSTRACTOS: Polimorfismo
    # ========================================================================

    def info(self) -> str:

        #SOBRESCRITURA: Muestra principal + secundarios.
        #Diferencia vs CancionSolo: incluye "ft. artista1, artista2"

        nombres = ", ".join([a.nombre for a in self.__artistas_secundarios])
        if self.__album:
            return f"'{self.titulo}': {self.artista_principal.nombre} ft. {nombres} ({self.__album})"
        return f"'{self.titulo}': {self.artista_principal.nombre} ft. {nombres} (Single)"

    def get_numero_artista(self) -> str:

        #IMPLEMENTACIÓN: 1 + longitud de secundarios.
        #Ejemplo: "3 artistas" (1 principal + 2 secundarios)

        return f"{self.__numero_artistas} artistas"

    @classmethod
    def estadisticas_colaboraciones(cls) -> None:
        #Mét. de clase: muestra total de colaboraciones creadas.
        print(f"\n Colaboraciones: {cls.total_canciones_colaboracion}")