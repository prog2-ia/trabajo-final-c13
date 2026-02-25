#proyecto_final.py

class Cancion:
    reproducciones=0
    def __init__(self,titulo,artista,duracion_seg,genero):
        self.titulo=titulo
        self.artista=artista
        self.duracion_seg=duracion_seg
        self.genero=genero
        self.reproducciones_cancion=0

    def repros(self):
        self.reproducciones_cancion+=1
        Cancion.reproducciones+=1
        print(f"Reproduciendo: {self.titulo}-{self.artista}")

class Album:
    def __init__(self,titulo_album,artista,anyo):
        self.titulo_album=titulo_album
        self.artista=artista
        self.anyo=anyo
        self.canciones=[]
        self.reproducciones_album=0

    def agrega_cancion(self,cancion):
        self.canciones.append(cancion)
        print(f" La canción {cancion} ha sido añadida al álbum {self.titulo_album}")

    def numero_canciones_album(self):
        cantidad_canciones_album=len(self.canciones)
        print(f"El álbum {self.titulo_album} tiene {cantidad_canciones_album} canciones")
        return cantidad_canciones_album

    def reproducir_album(self):
        self.reproducciones_album+=1
        print(f"El álbum tiene {self.reproducciones_album} reproducciones")

class Artista:
    total_artistas=0
    def __init__(self,nombre,pais,edad):
        self.nombre=nombre
        self.pais=pais
        self.edad=edad
        self.albumes=[]
    total_artistas+=1

    def agregar_album(self,album):
        self.albumes.append(album)
        cantidad_albumes_artista=len(self.albumes)
        print(f"La discografía de {self.nombre} posee un total de {cantidad_albumes_artista} álbumes")
        return cantidad_albumes_artista

    def total_canciones(self):
        total=0
        for album in self.albumes:
            total+=album.numero_canciones_album()
        print(f"{self.nombre} tiene {total} canciones en total")
        return total

    def numero_albumes(self):
        cantidad_albumes=len(self.albumes)
        print(f"El artista tiene {cantidad_albumes} álbum/es en total")
        return cantidad_albumes

class Playlist:
    def __init__(self,nombre):
        self.nombre=nombre
        self.canciones=[]

    def agregar_cancion(self,cancion):
        self.canciones.append(cancion)

    def contar_canciones(self):
        cantidad_canciones_playlist=len(self.canciones)
        print(f"Tu playlist llamada {self.nombre} tiene {cantidad_canciones_playlist} canciones")
        return cantidad_canciones_playlist

    def mostrar_canciones(self):
        if len(self.canciones)==0:
            print(f"No hay canciones en la playlist {self.nombre}")
        else:
            print(f"Contenido de la playlist {self.nombre}:")
            for cancion in self.canciones:
                print(f"{cancion.titulo}-{cancion.artista}")

class Usuario:
    def __init__(self,nombre_usuario,nombre_real):
        self.nombre_usuario=nombre_usuario
        self.nombre_real=nombre_real
        self.playlists_usuario=[]
        self.canciones_escuchadas=0

    def guardar_playlist(self,playlist):
        self.playlists_usuario.append(playlist)
        print(f"{self.nombre_usuario} ha guardado la playlist llamada {playlist.nombre}")

    def cantidad_playlists(self):
        numero_playlists=len(self.playlists_usuario)
        print(f"{self.playlists_usuario} tiene {numero_playlists} playlists guardadas")
        return numero_playlists



