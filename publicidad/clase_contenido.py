from abc import ABC, abstractmethod
# Clase Abstracta 'ContenidoReproducible': Es la base para cualquier elemento 
# que tenga un flujo de reproducción (canciones, podcasts, anuncios, etc.).
class ContenidoReproducible(ABC):
    def __init__(self, **kwargs):
        # Uso de **kwargs y super(): Esto es clave para la "herencia cooperativa".
        # Permite que los argumentos viajen por la cadena de clases padres (MRO)
        # sin que el programa se detenga si hay herencia múltiple.
        super().__init__(**kwargs)
    # Método Abstracto: Actúa como un contrato obligatorio.
    # Obliga a que cualquier clase hija (como Anuncio) implemente su propia
    # lógica de 'reproducir', asegurando que la interfaz sea consistente.
    @abstractmethod
    def reproducir(self) -> None:
        """Método abstracto que deben implementar todos los contenidos"""
        pass