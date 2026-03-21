# HERENCIA: Extiende Artista | POLIMORFISMO: Implementa métodos abstractos

from artistas.clase_Artista import Artista
from datetime import datetime


class ArtistaSolista(Artista):
    #Artista individual. Diferencia clave: tiene fecha_debut (no formación).

    def __init__(self, nombre, pais, edad, fecha_debut, **kwargs):
        #Inicializa solista. super() pasa datos a Artista.__init__().
        super().__init__(nombre=nombre, pais=pais, edad=edad, **kwargs)
        self.__fecha_debut = fecha_debut
        self.__es_banda = False  # Flag para diferenciar de bandas

    @property
    def fecha_debut(self):
        return self.__fecha_debut

    @property
    def es_banda(self):
        return self.__es_banda

    @fecha_debut.setter
    def fecha_debut(self, valor):
        if isinstance(valor, int) and valor > 1900:
            self.__fecha_debut = valor
        else:
            raise ValueError("La fecha de debut debe ser un año válido")

    def info(self):
        #SOBRESCRITURA: Añade fecha_debut (específico de solistas).
        print(f"El artista es '{self.nombre}', debutó en {self.__fecha_debut} y es de '{self.pais}'")

    def tipo(self):
        #IMPLEMENTACIÓN abstracta: identifica como solista.
        return "El artista es solista"

    def anyos_carrera(self):
        #IMPLEMENTACIÓN abstracta: calcula desde fecha_debut (no formación).
        anyos = datetime.now().year - self.__fecha_debut
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self, pais_gira, fecha_gira):
        print(f"¡{self.nombre} anuncia gira en {pais_gira} ({fecha_gira})!")