class Genero:
    # Atributo de clase (acumula canciones de TODOS los géneros creados)
    total_canciones_registradas = 0

    def __init__(self, nombre_genero, descripcion, capacidad_maxima=3):
        # Atributos de instancia
        self.nombre_genero = nombre_genero
        self.descripcion = descripcion
        self.canciones_este_genero = []
        # El "depósito" de nuestro género (capacidad de canciones)
        self.capacidad_maxima = capacidad_maxima 
        self.espacio_disponible = capacidad_maxima

    def añadir_cancion_a_genero(self, cancion):
        # Lógica tipo "Coche": Si no hay espacio (gasolina), da error
        if self.espacio_disponible > 0:
            self.canciones_este_genero.append(cancion)
            self.espacio_disponible -= 1 # Gastamos un espacio
            Genero.total_canciones_registradas += 1 # Aumentamos contador global
            print(f"✅ '{cancion.titulo}' añadida a {self.nombre_genero}. Espacio restante: {self.espacio_disponible}")
        else:
            # Error si se intenta añadir sin tener "cupo"
            print(f"ERROR: El género {self.nombre_genero} está lleno. No puedes añadir '{cancion.titulo}'.")

    def ampliar_capacidad(self, cantidad):
        # Equivalente a "Repostar": aumentamos el espacio disponible
        self.capacidad_maxima += cantidad
        self.espacio_disponible += cantidad
        print(f"Capacidad de {self.nombre_genero} ampliada. Ahora caben {self.espacio_disponible} más.")

    @classmethod
    def obtener_total_sistema(cls):
        # Método de clase: devuelve el total de canciones de todos los géneros
        print(f"Total de canciones en todos los géneros: {cls.total_canciones_registradas}")
        return cls.total_canciones_registradas