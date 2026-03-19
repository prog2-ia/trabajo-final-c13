#clase_CancionColaboracion.py
from clase_Cancion import Cancion
class CancionColaboracion(Cancion):
    def __init__(self,titulo,artista_principal,duracion_seg,genero,artistas_secundarios,album=None,**kwargs):
        super().__init__(titulo=titulo,artista_principal=artista_principal,duracion_seg=duracion_seg,genero=genero,**kwargs)
        self.__artistas_secundarios=artistas_secundarios
        self.__album=album
        self.__numero_artistas=1+len(artistas_secundarios)

    @property
    def artistas_secundarios(self):
        return self.__artistas_secundarios

    @property
    def album(self):
        return self.__album

    @property
    def numero_artistas(self):
        return self.__numero_artistas

    @artistas_secundarios.setter
    def artistas_secundarios(self,valor):
        if isinstance(valor,list):
            self.__artistas_secundarios=valor
            self.__numero_artistas=1+len(valor)
        else:
            raise ValueError("Los artistas secundarios deben ser una lista")

    @album.setter
    def album(self,valor):
        if valor is None or (isinstance(valor,str) and len(valor)>0):
            self.__album=valor
        else:
            raise ValueError("El álbum debe ser None o un texto no vacío")

    def info(self):
        todos = self.__artista_principal
        if self.__artistas_secundarios:
            todos+=" ft. "+", ".join(self.__artistas_secundarios)

        if self.__album:
            return f"La canción se llama '{self.titulo}' los cantantes son '{todos}' y es del álbum '{self.__album}'"
        else:
            return f"La canción se llama '{self.titulo}' los cantantes son '{todos}' y es un single"

    def get_numero_artista(self):
        return f"La cantidad de artistas de la canción es de {self.__numero_artistas}"