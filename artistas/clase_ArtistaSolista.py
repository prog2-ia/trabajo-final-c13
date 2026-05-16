# HERENCIA: Extiende Artista | POLIMORFISMO: Implementa métodos abstractos
# IMPLEMENTA: Diferenciación solista vs banda (fecha_debut, edad)

from typing import Optional, Any
from artistas.clase_Artista import Artista
from datetime import datetime


class ArtistaSolista(Artista):

    #Artista individual.
    #Diferencia clave vs ArtistaBanda:
    #- fecha_debut (no formación)
    #- edad (persona física)
    #- numero_artistas = 1 (siempre)


    def __init__(self, nombre: str, pais: str, edad: Optional[int], fecha_debut: int, **kwargs: Any) -> None:

        #Inicializa solista.
        #- super() pasa datos a Artista.__init__().
        #- fecha_debut: año del primer lanzamiento/concierto.

        super().__init__(nombre=nombre, pais=pais, edad=edad, **kwargs)

        self.__fecha_debut: int = fecha_debut
        self.__es_banda: bool = False

    # ========================================================================
    # PROPERTIES: Acceso controlado (lectura)
    # ========================================================================

    @property
    def fecha_debut(self) -> int:
        return self.__fecha_debut

    @property
    def es_banda(self) -> bool:
        return self.__es_banda

    # ========================================================================
    # SETTERS: Validación antes de modificar
    # ========================================================================

    @fecha_debut.setter  # type: ignore[no-redef, attr-defined]
    def fecha_debut(self, valor: int) -> None:

        #Validación de año de debut:
        #- Debe ser entero
        #- Entre 1900 y año actual (no futuro)

        anyo_actual = datetime.now().year
        if isinstance(valor, int) and 1900 < valor <= anyo_actual:
            self.__fecha_debut = valor
        else:
            raise ValueError(f"La fecha de debut debe estar entre 1900 y {anyo_actual}")

    # ========================================================================
    # SOBRESCRITURA DE MÉTODOS: Polimorfismo
    # ========================================================================

    def info(self) -> str:

        #SOBRESCRITURA: Añade fecha_debut (específico de solistas).
        #Diferencia vs ArtistaBanda: muestra debut, no formación.

        return f"El artista es '{self.nombre}', debutó en {self.__fecha_debut} y es de '{self.pais}'"

    def tipo(self) -> str:
        #IMPLEMENTACIÓN abstracta: identifica como solista.
        return "El artista es solista"

    def anyos_carrera(self) -> str:

        #IMPLEMENTACIÓN abstracta: calcula desde fecha_debut (no formación).
        #Fórmula: año_actual - fecha_debut

        anyos = datetime.now().year - self.__fecha_debut
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self, pais_gira: str, fecha_gira: str) -> None:
        #Mét. específico de solistas: anuncia gira con fecha y lugar.
        print(f"¡{self.nombre} anuncia gira en {pais_gira} ({fecha_gira})!")