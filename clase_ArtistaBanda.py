from clase_Artista import Artista
from datetime import datetime

class ArtistaBanda(Artista):
    def __init__(self,nombre,pais,numero_miembros,fecha_formacion,**kwargs):
        super().__init__(nombre=nombre,pais=pais,**kwargs)
        self.__numero_miembros=numero_miembros
        self.__fecha_formacion=fecha_formacion
        self.__es_banda=True

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
    def numero_miembros(self,valor):
        if isinstance(valor,int) and valor>0:
            self.__numero_miembros=valor
        else:
            raise ValueError("El número de miembros debe ser positivo")

    @fecha_formacion.setter
    def fecha_formacion(self,valor):
        if isinstance(valor,int) and valor>1900:
            self.__fecha_formacion=valor
        else:
            raise ValueError("La fecha de formación debe ser un año válido")

    def info(self):
        print(f"La banda se llama {self.nombre}, tiene {self.__numero_miembros} miembros, se formó en {self.fecha_formacion} y es de {self.pais}")

    def tipo(self):
        return "Grupo musical"

    def anyos_carrera(self):
        anyos = datetime.now().year - self.__fecha_formacion
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self, pais_gira, fecha_gira):
        print(f"¡{self.nombre} anuncia una gira en {pais_gira} en el año {fecha_gira}")