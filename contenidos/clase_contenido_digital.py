from abc import ABC, abstractmethod
# No podemos crear un objeto 'ContenidoDigital' directamente, 
# solo sirve para que otras clases (como Podcast) hereden de ella.
class ContenidoDigital(ABC):
    def __init__(self, **kwargs):
        # Usamos **kwargs y super() para que la herencia múltiple funcione.
        # Esto permite que los datos "viajen" a la siguiente clase en la jerarquía
        # sin que el programa se rompa si hay varios padres.
        super().__init__(**kwargs)
# Método Abstracto: Es una obligación para las clases hijas.
    # Cualquier cosa que sea un 'ContenidoDigital' DEBE tener su propia
    # forma de "reproducir", o Python no dejará que el programa funcione.
    @abstractmethod
    def reproducir(self) -> None:
        pass