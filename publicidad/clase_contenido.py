from abc import ABC, abstractmethod
# Clase Abstracta 'ContenidoReproducible': Es la base para cualquier elemento 
# que tenga un flujo de reproducción (canciones, podcasts, anuncios, etc.).
class ContenidoReproducible(ABC):
    def __init__(self,duracion: int = 0,metadatos: list = None, **kwargs):
        # Uso de **kwargs y super(): Esto es clave para la "herencia cooperativa".
        # Permite que los argumentos viajen por la cadena de clases padres (MRO)
        # sin que el programa se detenga si hay herencia múltiple.
        self.duracion = duracion
        self.metadatos = metadatos if metadatos else []
        super().__init__(**kwargs)
    # Método Abstracto: Actúa como un contrato obligatorio.
    # Obliga a que cualquier clase hija (como Anuncio) implemente su propia
    # lógica de 'reproducir', asegurando que la interfaz sea consistente.
    @abstractmethod
    def reproducir(self) -> None:
        """Método abstracto que deben implementar todos los contenidos"""
        pass
    # métodos de sobrecarga 
    def __add__(self, otro):
        # Suma las duraciones de dos contenidos reproducibles.
        if isinstance(otro, ContenidoReproducible):
            nueva_duracion = self.duracion + otro.duracion[cite: 1]
            print(f"Calculando duración total combinada: {nueva_duracion} segundos.")
            return nueva_duracion 
        return NotImplemented

    # Utilizada para acceder a los metadatos del contenido por índice.
    def __getitem__(self, indice):
        try:
            return self.metadatos[indice][cite: 1]
        except IndexError:
            return "Índice de metadato fuera de rango."