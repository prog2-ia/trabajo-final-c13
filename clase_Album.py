# CLASE: Álbum | RELACIÓN: Agregación con Artista (objeto, no string)

class Album:
    #Álbum musical. artista es OBJETO Artista (permite navegación de relaciones).

    def __init__(self, titulo_album, artista, anyo):

        #Inicializa álbum. artista es OBJETO (no string) para:
        #- Acceder a artista.nombre, artista.info()
        #- Mantener integridad (si cambia nombre, se actualiza)

        self.titulo_album = titulo_album
        self.artista = artista
        self.anyo = anyo
        self.canciones = []
        self.reproducciones_album = 0

    def agrega_cancion(self, cancion):
        #Añade canción con validación de duplicados
        from excepciones import CancionDuplicadaError, ValorInvalidoError

        if cancion is None:
            raise ValorInvalidoError("canción",None,"no puede ser None")

        for c in self.canciones:
            if cancion.titulo.lower() == c.titulo.lower():
                raise CancionDuplicadaError(cancion.titulo,f"el álbum '{self.titulo_album}'")

        self.canciones.append(cancion)


    def numero_canciones_album(self):
        print(f"El álbum {self.titulo_album} tiene {len(self.canciones)} canciones")
        return len(self.canciones)

    def reproducir_album(self):
        #Reproduce todas las canciones. Delega repros() a cada canción.
        self.reproducciones_album += 1
        for cancion in self.canciones:
            cancion.repros()
        print(f"Álbum reproducido {self.reproducciones_album} veces")

    def cancion_mas_larga(self):
        #Devuelve la canción más larga usando >
        from excepciones import SinCancionesError

        if not self.canciones:
            raise SinCancionesError("álbum",self.titulo_album)

        mas_larga=self.canciones[0]
        for cancion in self.canciones[1:]:
            if cancion > mas_larga:
                mas_larga = cancion

        return mas_larga

    def __str__(self):
        return f"{self.titulo_album} ({self.anyo})"
