#proyecto_final.py


class Album:
    def __init__(self,titulo_album,artista,anyo):
        self.titulo_album=titulo_album
        self.artista=artista
        self.anyo=anyo
        self.canciones=[]
        self.reproducciones_album=0

    def agrega_cancion(self,cancion):
        for cancion_existente in self.canciones:
            if cancion_existente.titulo==cancion.titulo and cancion_existente.artista==cancion.artista:
                print(f"La canción llamada {cancion.titulo} ya está en el álbum {self.titulo_album}")
                return
        self.canciones.append(cancion)
        print(f" La canción {cancion} ha sido añadida al álbum {self.titulo_album}")

    def numero_canciones_album(self):
        cantidad_canciones_album=len(self.canciones)
        print(f"El álbum {self.titulo_album} tiene {cantidad_canciones_album} canciones")
        return cantidad_canciones_album

    def reproducir_album(self):
        self.reproducciones_album+=1
        for cancion in self.canciones:
            cancion.repros()
        if self.reproducciones_album==1:
            print(f"El álbum {self.titulo_album} tiene 1 reproducción")
        else:
            print(f"El álbum {self.titulo_album} tiene {self.reproducciones_album} reproducciones")

    def __str__(self):
        return f"{self.titulo_album} ({self.anyo})"

class Artista:
    total_artistas=0
    def __init__(self,nombre,pais,edad):
        self.nombre=nombre
        self.pais=pais
        self.edad=edad
        self.canciones=[]
        self.albumes=[]
        Artista.total_artistas+=1

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







