from abc import ABC,abstractmethod
from datetime import datetime

class Artista(ABC):
    total_artistas=0
    def __init__(self,nombre,pais,edad=None,**kwargs):
        super().__init__(**kwargs)
        self.__nombre=nombre
        self.__pais=pais
        self.__edad=edad
        self.__canciones=[]
        self.__albumes=[]
        Artista.total_artistas+=1

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pais(self):
        return self.__pais

    @property
    def edad(self):
        return self.__edad

    @property
    def canciones(self):
        return self.__canciones

    @property
    def albumes(self):
        return self.__albumes

    @nombre.setter
    def nombre(self,valor):
        if isinstance(valor,str) and len(valor)>0:
            self.__nombre=valor
        else:
            raise ValueError("El nombre debe ser un texto no vacío")

    @pais.setter
    def pais(self,valor):
        if isinstance(valor,str) and len(valor)>0:
            self.__pais=valor
        else:
            raise ValueError("El país debe ser un texto no vacío")

    @edad.setter
    def edad(self,valor):
        if valor is None:
            self.__edad=None
        elif isinstance(valor,int) and valor>0:
            self.__edad=valor
        else:
            raise ValueError("La edad debe ser un número positivo")

    def __str__(self):
        return f"{self.nombre}({self.pais})"

    def agregar_canciones(self,cancion):
        self.canciones.append(cancion)

    def agregar_album(self,album):
        self.albumes.append(album)

    def total_canciones(self):
        total=0
        for album in self.albumes:
            total+=len(album.canciones)
        total+=len(self.canciones)
        if total==1:
            print(f"{self.nombre} tiene 1 canción en total")
        else:
            print(f"{self.nombre} tiene {total} canciones en total")
        return total

    def numero_albumes(self):
        cantidad_albumes=len(self.albumes)
        if cantidad_albumes==1:
            print(f"{self.nombre} tiene 1 álbum en total")
        else:
            print(f"{self.nombre} tiene {cantidad_albumes} álbumes en total")
        return cantidad_albumes

    def info(self):
        if self.edad:
            return f"{self.nombre} es de {self.pais} y tiene {self.edad} años"
        else:
            return f"{self.nombre} es de {self.pais}"

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def anyos_carrera(self):
        pass