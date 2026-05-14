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

    def cancion_mas_larga(self):
        #Devuelve la canción más larga del álbum usando operadores de sobrecarga
        if not self.canciones:
            return None

        #Empezamos con la primera como candidata
        mas_larga=self.canciones[0]

        #Recorremos el resto comparando con > (usa __gt__ de Cancion)
        for cancion in self.canciones[1:]:
            if cancion>mas_larga: #Aquí usamos __gt__ explícitamente
                mas_larga=cancion
        return mas_larga


    def __str__(self):
        return f"{self.titulo_album} ({self.anyo})"

    def __add__(self,otro_album):
        if not isinstance(otro_album, Album):
            return self

        nuevo_titulo=f"{self.titulo_album} + {otro_album.titulo_album}"
        nuevo= Album(nuevo_titulo, self.artista, max(self.anyo,otro_album.anyo))
        nuevo.canciones=self.canciones.copy()

        for c in otro_album.canciones:
            repetida=False
            for existente in nuevo.canciones:
                if existente.titulo.lower() == c.titulo.lower():
                    repetida=True
                    break
            if not repetida:
                nuevo.canciones.append(c)

        return nuevo