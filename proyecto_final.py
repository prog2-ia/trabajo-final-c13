#proyecto_final.py

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
        if self.reproducciones_album==1:
            print(f"El álbum {self.titulo_album} tiene 1 reproducción")
        else:
            print(f"El álbum {self.titulo_album} tiene {self.reproducciones_album} reproducciones")

class Artista:
    total_artistas=0
    def __init__(self,nombre,pais,edad):
        self.nombre=nombre
        self.pais=pais
        self.edad=edad
        self.canciones=[]
        self.albumes=[]
        Artista.total_artistas+=1

    def agregar_canciones(self,cancion):
        self.canciones.append(cancion)

    def agregar_album(self,album):
        self.albumes.append(album)

    def total_canciones(self):
        total=0
        for album in self.albumes:
            total+=album.numero_canciones_album()
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
        print(f"{self.nombre_usuario} tiene {numero_playlists} playlists guardadas")
        return numero_playlists
class Genero:
    def __init__(self, nombre_genero, descripcion):
        self.nombre_genero = nombre_genero
        self.descripcion = descripcion
        self.canciones_este_genero = []

    def añadir_cancion_a_genero(self, cancion):
        self.canciones_este_genero.append(cancion)
        print(f"Canción '{cancion.titulo}' añadida a la categoría {self.nombre_genero}")

class EstadoAnimo:
    def __init__(self, tipo_animo, color):
        self.tipo_animo = tipo_animo
        self.color = color
        self.playlists_sugeridas = [] # Lista para guardar objetos de la clase Playlist de Alex

    def asociar_playlist(self, playlist):
        self.playlists_sugeridas.append(playlist)
        print(f"La playlist '{playlist.nombre}' ahora se recomienda para cuando estés {self.tipo_animo}")
class BibliotecaGlobal:
    total_canciones_biblioteca = 0

    def __init__(self, duenyo):
        self.duenyo = duenyo
        self.todas_las_canciones = []

    def registrar_nueva_cancion(self, cancion):
        self.todas_las_canciones.append(cancion)
        BibliotecaGlobal.total_canciones_biblioteca += 1
        print(f"Biblioteca de {self.duenyo}: Ahora hay {BibliotecaGlobal.total_canciones_biblioteca} canciones en total")




