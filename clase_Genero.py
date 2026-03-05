class Genero:
    # Atributo de clase (común a todos los géneros)
    total_canciones_registradas: int = 0

    def __init__(self, nombre_genero: str, descripcion: str, capacidad_maxima: int = 3):
        self.nombre_genero: str = nombre_genero
        self.descripcion: str = descripcion
        self.canciones_este_genero: list = []
        self.capacidad_maxima: int = capacidad_maxima 
        self.espacio_disponible: int = capacidad_maxima

    # MÉTODO ESPECIAL (Dunder) [cite: 60]
    def __str__(self) -> str:
        return f"Género: {self.nombre_genero} ({len(self.canciones_este_genero)} canciones)"

    # MÉTODO DE INSTANCIA (Usa self) 
    def añadir_cancion_a_genero(self, cancion) -> None:
        if self.espacio_disponible > 0:
            self.canciones_este_genero.append(cancion)
            self.espacio_disponible -= 1 
            Genero.total_canciones_registradas += 1 
            print(f"Añadida: {cancion.titulo}")
        else:
            print(f"Error: {self.nombre_genero} lleno.")

    # MÉTODO DE CLASE (Usa cls) [cite: 104]
    @classmethod
    def obtener_total_sistema(cls) -> int:
        return cls.total_canciones_registradas