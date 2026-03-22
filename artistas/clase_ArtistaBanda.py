# HERENCIA: Extiende Artista | POLIMORFISMO: Implementa métodos abstractos

from artistas.clase_Artista import Artista
from datetime import datetime


class ArtistaBanda(Artista):
    #Grupo musical. Diferencia clave: tiene numero_miembros y fecha_formacion.

    def __init__(self, nombre, pais, numero_miembros, fecha_formacion, **kwargs):
        #Inicializa banda. No pasa edad a super(), ya que las bandas no tienen edad.
        super().__init__(nombre=nombre, pais=pais, **kwargs)
        self.__numero_miembros = numero_miembros
        self.__fecha_formacion = fecha_formacion
        self.__es_banda = True

    @property
    def numero_miembros(self):
        return self.__numero_miembros

    @property
    def fecha_formacion(self):
        return self.__fecha_formacion

    @property
    def es_banda(self):
        return self.__es_banda

    @numero_miembros.setter
    def numero_miembros(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__numero_miembros = valor
        else:
            raise ValueError("El número de miembros debe ser positivo")

    @fecha_formacion.setter
    def fecha_formacion(self, valor):
        from datetime import datetime
        anyo_actual = datetime.now().year

        if isinstance(valor, int) and 1900 < valor <= anyo_actual:
            self.__fecha_formacion = valor
        else:
            raise ValueError(f"La fecha de formación debe estar entre 1900 y {anyo_actual}")

    def info(self):
        #SOBRESCRITURA: Muestra numero_miembros (específico de bandas).
        print(f"La banda {self.nombre} tiene {self.__numero_miembros} miembros ({self.pais})")

    def tipo(self):
        #IMPLEMENTACIÓN abstracta: identifica como banda.
        return "Grupo musical"

    def anyos_carrera(self):
        #IMPLEMENTACIÓN abstracta: calcula desde fecha_formacion (no debut).
        anyos = datetime.now().year - self.__fecha_formacion
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self, pais_gira, fecha_gira):
        print(f"¡{self.nombre} anuncia gira en {pais_gira} ({fecha_gira})!")