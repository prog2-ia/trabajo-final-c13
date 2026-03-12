class Artista:
    total_artistas=0
    def __init__(self,nombre,pais,edad=None):
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

    def info(self):
        if self.edad:
            return f"{self.nombre} es de {self.pais} y tiene {self.edad} años"
        else:
            return f"{self.nombre} es de {self.pais}"

class ArtistaSolista(Artista):
    def __init__(self,nombre,pais,edad,fecha_debut):
        super().__init__(nombre,pais,edad)
        self.fecha_debut=fecha_debut
        self.es_banda=False

    def info(self):
        return f"El artista es '{self.nombre}' empezó su carrera en el año {self.fecha_debut} y es de '{self.pais}'"

    def tipo(self):
        return "El artista es solista"

    def anyos_carrera(self):
        from datetime import datetime
        anyos=datetime.now().year-self.fecha_debut
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self,pais_gira,fecha_gira):
        print(f"¡{self.nombre} anuncia una gira en {pais_gira} en el año {fecha_gira}")

class ArtistaBanda(Artista):
    def __init__(self,nombre,pais,numero_miembros,fecha_formacion):
        super().__init__(nombre,pais)
        self.numero_miembros=numero_miembros
        self.fecha_formacion=fecha_formacion
        self.es_banda=True

    def info(self):
        return f"La banda se llama {self.nombre}, tiene {self.numero_miembros} miembros y se formó en {self.fecha_formacion}"

    def tipo(self):
        return "Grupo musical"

    def anyos_carrera(self):
        from datetime import datetime
        anyos=datetime.now().year-self.fecha_formacion
        return f"{self.nombre} lleva {anyos} años de carrera"

    def anunciar_gira(self,pais_gira,fecha_gira):
        print(f"¡{self.nombre} anuncia una gira en {pais_gira} en el año {fecha_gira}")
