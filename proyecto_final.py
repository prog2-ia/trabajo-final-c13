#proyecto_final.py




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
        self.playlists_sugeridas = []
    def asociar_playlist(self, playlist):
        self.playlists_sugeridas.append(playlist)
        print(f"La playlist '{playlist.nombre}' ahora se recomienda para cuando estés {self.tipo_animo}")
class BibliotecaGlobal:

    def __init__(self, duenyo):
        self.duenyo = duenyo
        self.todas_las_canciones = []
        self.total_canciones_biblioteca = 0

    def registrar_nueva_cancion(self, cancion):
        self.todas_las_canciones.append(cancion)
        self.total_canciones_biblioteca += 1
        print(f"Biblioteca de {self.duenyo}: Ahora hay {self.total_canciones_biblioteca} canciones en total")




