# CLASE ABSTRACTA: Base para todos los artistas
# IMPLEMENTA: ABC, Encapsulamiento (__atributo), Herencia

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional, List


class Artista(ABC):
    #Clase base abstracta. Obliga a subclases a implementar tipo() y anyos_carrera().

    # Variable de clase: compartida entre las instancias
    total_artistas: int = 0

    def __init__(self, nombre: str, pais: str, edad: Optional[int] = None, **kwargs: Any) -> None:

        #Inicializa artista.
        #- **kwargs permite herencia múltiple con Mixins.
        #- super().__init__(**kwargs) es esencial para que funcione ABC + Mixins.

        super().__init__(**kwargs)

        # Encapsulamiento: __atributo obliga a usar properties (control de acceso)
        self.__nombre: str = nombre
        self.__pais: str = pais
        self.__edad: Optional[int] = edad
        self.__canciones: List[Any] = []
        self.__albumes: List[Any] = []

        Artista.total_artistas += 1

    # ========================================================================
    # PROPERTIES: Acceso controlado (lectura)
    # ========================================================================

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def pais(self) -> str:
        return self.__pais

    @property
    def edad(self) -> Optional[int]:
        return self.__edad

    @property
    def canciones(self) -> List[Any]:
        return self.__canciones

    @property
    def albumes(self) -> List[Any]:
        return self.__albumes

    # ========================================================================
    # SETTERS: Validación antes de modificar (integridad de datos)
    # ========================================================================

    @nombre.setter  # type: ignore[no-redef, attr-defined]
    def nombre(self, valor: str) -> None:
        from excepciones import ValorInvalidoError
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValorInvalidoError("nombre", valor, "debe ser un texto no vacío")
        self.__nombre = valor

    @pais.setter  # type: ignore[no-redef, attr-defined]
    def pais(self, valor: str) -> None:
        from excepciones import ValorInvalidoError
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValorInvalidoError("país", valor, "debe ser un texto no vacío")
        self.__pais = valor

    @edad.setter  # type: ignore[no-redef, attr-defined]
    def edad(self, valor: Optional[int]) -> None:
        from excepciones import ValorInvalidoError
        if valor is None:
            self.__edad = None
        elif not isinstance(valor, int):
            raise ValorInvalidoError("edad", valor, "debe ser un número entero")
        elif valor < 0 or valor > 110:
            raise ValorInvalidoError("edad", valor, "debe estar entre 0 y 110 años")
        self.__edad = valor

    # ========================================================================
    # SOBRECARGA DE OPERADORES: Comparación y representación
    # ========================================================================

    def __str__(self) -> str:
        return f"{self.nombre}({self.pais})"

    def __add__(self, otro: Any) -> str:
        #artista1 + artista2 → string de colaboración
        if not isinstance(otro, Artista):
            return str(self)
        return f"{self.nombre} + {otro.nombre} -> Colaboración pendiente"

    def __eq__(self, otro: Any) -> bool:
        #Dos artistas son iguales si coinciden nombre y país
        if not isinstance(otro, Artista):
            return False
        return (self.nombre.lower() == otro.nombre.lower() and
                self.pais.lower() == otro.pais.lower())

    # ========================================================================
    # MÉTODOS DE INSTANCIA: Gestión de contenido
    # ========================================================================

    def agregar_canciones(self, cancion: Any) -> None:
        #Añade canción a la lista de canciones del artista.
        self.canciones.append(cancion)

    def agregar_album(self, album: Any) -> None:
        #Añade álbum a la lista de álbumes del artista.
        self.albumes.append(album)

    def total_canciones(self) -> int:

        #Calcula total: canciones de álbumes + singles individuales.
        #Usa comprensión de generadores para sumar.

        total = sum(len(album.canciones) for album in self.albumes)
        total += len(self.canciones)
        print(f"{self.nombre} tiene {total} canciones en total")
        return total

    def numero_albumes(self) -> int:
        #Muestra y retorna número de álbumes.
        print(f"{self.nombre} tiene {len(self.albumes)} álbumes en total")
        return len(self.albumes)

    def info(self) -> str:

        #Información básica.
        #Subclases sobrescriben para datos específicos.

        if self.edad:
            return f"{self.nombre} es de {self.pais} y tiene {self.edad} años"
        return f"{self.nombre} es de {self.pais}"

    # ========================================================================
    # MÉTODOS ABSTRACTOS: Si subclase no los implementa da error al instanciar
    # ========================================================================

    @abstractmethod
    def tipo(self) -> str:
        #Polimorfismo: cada subclase define su tipo (solista/banda)
        pass

    @abstractmethod
    def anyos_carrera(self) -> str:
        #Polimorfismo: cada subclase calcula años diferentes (debut/formación)
        pass

    @classmethod
    def estadisticas_artistas(cls) -> None:

        #Mét. de clase: usa cls (no self) para acceder a variable de clase.
        #Muestra total de artistas registrados en toda la plataforma.

        print(f"\n Total artistas registrados: {cls.total_artistas}")