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
        #Añade canción si no está duplicada (evita repetidos por título).
        for c in self.canciones:
            if c.titulo == cancion.titulo:
                print(f"La canción {cancion.titulo} ya está en el álbum")
                return
        self.canciones.append(cancion)
        print(f" {cancion.titulo} añadida al álbum {self.titulo_album}")

    def numero_canciones_album(self):
        print(f"El álbum {self.titulo_album} tiene {len(self.canciones)} canciones")
        return len(self.canciones)

    def reproducir_album(self):
        #Reproduce todas las canciones. Delega repros() a cada canción.
        self.reproducciones_album += 1
        for cancion in self.canciones:
            cancion.repros()
        print(f"Álbum reproducido {self.reproducciones_album} veces")

    def __str__(self):
        return f"{self.titulo_album} ({self.anyo})"