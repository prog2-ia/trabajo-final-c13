
#clase_Playlist.py

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

    def __str__(self):
        return f"Playlist {self.nombre} ({len(self.canciones)} canciones)"