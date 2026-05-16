# HERENCIA: Extiende Artista | POLIMORFISMO: Implementa métodos abstractos
# IMPLEMENTA: Diferenciación banda vs solista (numero_miembros, fecha_formacion)

from typing import Any
from artistas.clase_Artista import Artista
from datetime import datetime


class ArtistaBanda(Artista):

    #Grupo musical.
    #Diferencia clave vs ArtistaSolista:
    #- numero_miembros (dinámico)
    #- fecha_formacion (no debut)
    #- NO tiene edad (las bandas no envejecen como personas)


    def __init__(self, nombre: str, pais: str, numero_miembros: int, fecha_formacion: int, **kwargs: Any) -> None:

        #Inicializa banda.
        #- NO pasa edad a super(), ya que las bandas no tienen edad.
        #- fecha_formacion: año de creación del grupo.

        super().__init__(nombre=nombre, pais=pais, **kwargs)

        self.__numero_miembros: int = numero_miembros
        self.__fecha_formacion: int = fecha_formacion
        self.__es_banda: bool = True

    # ========================================================================
    # PROPERTIES: Acceso controlado (lectura)
    # ========================================================================

    @property
    def numero_miembros(self) -> int:
        return self.__numero_miembros

    @property
    def fecha_formacion(self) -> int:
        return self.__fecha_formacion

    @property
    def es_banda(self) -> bool:
        return self.__es_banda

    # ========================================================================
    # SETTERS: Validación antes de modificar
    # ========================================================================

    @numero_miembros.setter  # type: ignore[no-redef, attr-defined]
    def numero_miembros(self, valor: int) -> None:
        #El número de miembros debe ser positivo (>0).
        if isinstance(valor, int) and valor > 0:
            self.__numero_miembros = valor
        else:
            raise ValueError("El número de miembros debe ser positivo")

    @fecha_formacion.setter  # type: ignore[no-redef, attr-defined]
    def fecha_formacion(self, valor: int) -> None:

        #Validación de año de formación:
        #- Debe ser entero
        #- Entre 1900 y año actual (no futuro)

        anyo_actual = datetime.now().year
        if isinstance(valor, int) and 1900 < valor <= anyo_actual:
            self.__fecha_formacion = valor
        else:
            raise ValueError(f"La fecha de formación debe estar entre 1900 y {anyo_actual}")

    # ========================================================================
    # SOBRESCRITURA DE MÉTODOS: Polimorfismo
    # ========================================================================

    def info(self) -> str:

        #SOBRESCRITURA: Muestra numero_miembros (específico de bandas).
        #Diferencia vs ArtistaSolista: no muestra edad, muestra miembros.

        return f"La banda {self.nombre} tiene {self.__numero_miembros} miembros ({self.pais})"

    def tipo(self) -> str:
        #IMPLEMENTACIÓN abstracta: identifica como banda.
        return "Grupo musical"

    def anyos_carrera(self) -> str:

        #IMPLEMENTACIÓN abstracta: calcula desde fecha_formacion (no debut).
        #Fórmula: año_actual - fecha_formacion

        anyos = datetime.now().year - self.__fecha_formacion
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self, pais_gira: str, fecha_gira: str) -> None:
        #Mét. específico de bandas: anuncia gira con fecha y lugar.
        print(f"¡{self.nombre} anuncia gira en {pais_gira} ({fecha_gira})!")