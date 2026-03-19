from clase_Artista import Artista
from datetime import datetime

class ArtistaSolista(Artista):
    def __init__(self,nombre,pais,edad,fecha_debut,**kwargs):
        super().__init__(nombre=nombre,pais=pais,edad=edad,**kwargs)
        self.__fecha_debut=fecha_debut
        self.__es_banda=False

@property
def fecha_debut(self):
    return self.__fecha_debut

@property
def es_banda(self):
    return self.__es_banda

@fecha_debut.setter
def fecha_debut(self,valor):
    if isinstance(valor,int) and valor>1900:
        self.__fecha_debut=valor
    else:
        raise ValueError("La fecha de debut debe ser un año válido")

def info(self):
    return f"El artista es '{self.nombre}' empezó su carrera en el año {self.__fecha_debut} y es de '{self.pais}'"


def tipo(self):
    return "El artista es solista"

def anyos_carrera(self):
    anyos=datetime.now().year-self.__fecha_debut
    return f"{self.nombre} lleva {anyos} años de carrera"

def anunciar_gira(self,pais_gira,fecha_gira):
    print(f"¡{self.nombre} anuncia una gira en {pais_gira} en el año {fecha_gira}")