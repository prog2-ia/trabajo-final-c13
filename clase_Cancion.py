#clase_Cancion.py

class Cancion:
    reproducciones=0
    def __init__(self,titulo,artista,duracion_seg,genero):
        self.titulo=titulo
        self.artista=artista
        self.duracion_seg=duracion_seg
        self.genero=genero
        self.reproducciones_cancion=0

    def __str__(self):
        return f"{self.titulo}"

    def repros(self):
        self.reproducciones_cancion+=1
        Cancion.reproducciones+=1
        print(f"Reproduciendo: {self.titulo}-{self.artista}")

    def numero_reproducciones(self):
        if self.reproducciones_cancion==1:
            print(f"Se ha escuchado 1 vez la canción {self.titulo} en toda la plataforma ")
        else:
            print(f"Se ha escuchado {self.reproducciones_cancion} veces la canción {self.titulo} en toda la plataforma")

        if Cancion.reproducciones==1:
            print(f"La plataforma lleva un total de 1 reproducción")
        else:
            print(f"La plataforma lleva un total de {Cancion.reproducciones} reproducciones")