#clase_Usuario.py

from clase_Cancion import Cancion
from clase_Playlist import Playlist

class Usuario:
    def __init__(self,nombre_usuario,nombre_real,**kwargs):
        super().__init__(**kwargs)
        self.nombre_usuario=nombre_usuario
        self.nombre_real=nombre_real
        self.playlists_usuario=[]
        self.canciones_escuchadas=0
        self.saltos_maximos=6
        self.saltos_actuales=0
        self.historial_saltos=[]

    def guardar_playlist(self,playlist):
        self.playlists_usuario.append(playlist)
        print(f"{self.nombre_usuario} ha guardado la playlist llamada {playlist.nombre}")

    def cantidad_playlists(self):
        numero_playlists=len(self.playlists_usuario)
        print(f"{self.nombre_usuario} tiene {numero_playlists} playlists guardadas")
        return numero_playlists

    def avanzar_cancion(self,cancion,playlist_origen=None):
        if self.saltos_actuales >= self.saltos_maximos:
            print(f"ERROR: Has alcanzado el límite de {self.saltos_maximos} saltos ")
            return False
        else:
            self.saltos_actuales+=1
            self.historial_saltos.append((cancion,playlist_origen))

            if playlist_origen:
                nombre_playlist=playlist_origen.nombre
            else:
                nombre_playlist="Reproducción aleatoria"

            print(f"Canción '{cancion.titulo}' saltada desde la playlist '{nombre_playlist}'(Saltos que llevas: {self.saltos_actuales} de {self.saltos_maximos})")
            return True

    def recargar_saltos(self,cantidad):
        self.saltos_actuales-=cantidad
        if self.saltos_actuales<0:
            self.saltos_actuales=0
        else:
            pass

        saltos_disponibles=self.saltos_maximos-self.saltos_actuales
        print(f"¡Se han recargado los saltos! Ahora tienes {saltos_disponibles} saltos disponibles de {self.saltos_maximos} saltos máximos ")

    def escuchar_cancion(self,cancion):
        self.canciones_escuchadas+=1
        cancion.repros()

    @classmethod
    def canciones_saltadas_de_artista(cls,historial_saltos,nombre_artista):
        filtradas=[]

        for cancion,playlist in historial_saltos:
            if cancion.artista == nombre_artista:
                filtradas.append(cancion)

        if len(filtradas) == 0:
            print(f"No hay canciones saltadas de {nombre_artista}")
        else:
            print(f"Canciones saltadas de {nombre_artista}: {len(filtradas)}")
            for c in filtradas:
                print(f"-{c.titulo}")

        return filtradas

    @classmethod
    def canciones_saltadas_de_playlist(cls,historial_saltos,playlist):
        filtradas=[]
        for cancion,playlist_origen in historial_saltos:
            if playlist_origen==playlist:
                filtradas.append(cancion)

        if len(filtradas) == 0:
            print(f"No hay canciones saltadas de '{playlist.nombre}'")
        else:
            print(f"Canciones saltadas de '{playlist.nombre}': {len(filtradas)}")
            for c in filtradas:
                print(f"-{c.titulo}-{c.artista}")

        return filtradas

    @classmethod
    def total_saltos_usuario(cls,historial_saltos):
        print(f"Total de saltos: {len(historial_saltos)}")
        return len(historial_saltos)
