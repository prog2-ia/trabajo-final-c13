#clase_Cancion.py

class Cancion:
    reproducciones=0
    def __init__(self,titulo,artista_principal,duracion_seg,genero):
        self.titulo=titulo
        self.artista_principal=artista_principal
        self.duracion_seg=duracion_seg
        self.genero=genero
        self.reproducciones_cancion=0

    def __str__(self):
        return f"{self.titulo}"

    def repros(self):
        self.reproducciones_cancion+=1
        Cancion.reproducciones+=1
        print(f"Reproduciendo: {self.titulo}-{self.artista_principal}")

    def numero_reproducciones(self):
        if self.reproducciones_cancion==1:
            print(f"Se ha escuchado 1 vez la canción {self.titulo} en toda la plataforma ")
        else:
            print(f"Se ha escuchado {self.reproducciones_cancion} veces la canción {self.titulo} en toda la plataforma")

        if Cancion.reproducciones==1:
            print(f"La plataforma lleva un total de 1 reproducción")
        else:
            print(f"La plataforma lleva un total de {Cancion.reproducciones} reproducciones")

    def info(self):
        return f"{self.titulo} | {self.duracion_seg} | {self.genero}"

class CancionSolo(Cancion):
    def __init__(self,titulo,artista_principal,duracion_seg,genero,album=None):
        super().__init__(titulo,artista_principal,duracion_seg,genero)
        self.album=album
        self.numero_artistas=1

    def info(self):
        if self.album:
            return f"La canción es '{self.titulo}' de {self.artista_principal} y pertenece al álbum '{self.album}'"
        else:
            return f"La canción es '{self.titulo}' de {self.artista_principal} y es un single"

class CancionColaboracion(Cancion):
    def __init__(self,titulo,artista_principal,duracion_seg,genero,artistas_secundarios,album=None):
        super().__init__(titulo,artista_principal,duracion_seg,genero)
        self.artistas_secundarios=artistas_secundarios
        self.album=album
        self.numero_artistas=1+len(self.artistas_secundarios)

    def info(self):
        todos = self.artista_principal
        if self.artistas_secundarios:
            todos+=" ft. "+", ".join(self.artistas_secundarios)

        if self.album:
            return f"La canción se llama '{self.titulo}' los cantantes son '{todos}' y es del álbum '{self.album}'"
        else:
            return f"La canción se llama '{self.titulo}' los cantantes son '{todos}' y es un single"

    def cantidad_artistas(self):
        return f"La cantidad de artistas de la canción es de {self.numero_artistas}"

