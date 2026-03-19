#clase_Cancion.py
from abc import ABC,abstractmethod
class Cancion(ABC):
    reproducciones=0
    def __init__(self,titulo,artista_principal,duracion_seg,genero,**kwargs):
        super().__init__(**kwargs)
        self.__titulo=titulo
        self.__artista_principal=artista_principal
        self.__duracion_seg=duracion_seg
        self.__genero=genero
        self.__reproducciones_cancion=0

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista_principal(self):
        return self.__artista_principal

    @property
    def duracion_seg(self):
        return self.__duracion_seg

    @property
    def genero(self):
        return self.__genero

    @property
    def reproducciones_cancion(self):
        return self.__reproducciones_cancion

    @titulo.setter
    def titulo(self,valor):
        if isinstance(valor,str) and len(valor)>0:
            self.__titulo=valor
        else:
            raise ValueError("El título debe ser un texto no vacío")

    @artista_principal.setter
    def artista_principal(self,valor):
        if isinstance(valor,str) and len(valor)>0:
            self.__artista_principal=valor
        else:
            raise ValueError("El artista debe ser un texto no vacío")

    @duracion_seg.setter
    def duracion_seg(self,valor):
        if isinstance(valor,int) and valor>0:
            self.__duracion_seg=valor
        else:
            raise ValueError("La duración debe ser un número positivo")

    @genero.setter
    def genero(self,valor):
        if isinstance(valor,str) and len(valor)>0:
            self.__genero=valor
        else:
            raise ValueError("El género debe ser un texto no vacío")


    def __str__(self):
        return f"{self.__titulo}"

    def repros(self):
        self.__reproducciones_cancion+=1
        Cancion.reproducciones+=1
        print(f"Reproduciendo: {self.__titulo}-{self.__artista_principal}")

    def numero_reproducciones(self):
        if self.__reproducciones_cancion==1:
            print(f"Se ha escuchado 1 vez la canción {self.__titulo} en toda la plataforma ")
        else:
            print(f"Se ha escuchado {self.__reproducciones_cancion} veces la canción {self.__titulo} en toda la plataforma")

        if Cancion.reproducciones==1:
            print(f"La plataforma lleva un total de 1 reproducción")
        else:
            print(f"La plataforma lleva un total de {Cancion.reproducciones} reproducciones")

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def get_numero_artista(self):
        pass