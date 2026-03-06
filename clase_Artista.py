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
