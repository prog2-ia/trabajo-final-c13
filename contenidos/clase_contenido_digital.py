from abc import ABC, abstractmethod
from typing import Any

# No podemos crear un objeto 'ContenidoDigital' directamente, 
# solo sirve para que otras clases (como Podcast) hereden de ella.
class ContenidoDigital(ABC):
    def __init__(self, **kwargs: Any) -> None:
        # Extraemos de forma segura los parámetros que pertenecen a la rama de 
        # ContenidoReproducible para que no sigan viajando hacia arriba por el MRO
        # y no terminen colándose en la clase base object.
        kwargs.pop('duracion', None)
        kwargs.pop('metadatos', None)
        
        # Ahora que el saco de kwargs está limpio de datos de contenido, 
        # pasamos el resto hacia arriba con total seguridad
        super().__init__(**kwargs)

    # Método Abstracto: Es una obligación para las clases hijas.
    # Cualquier cosa que sea un 'ContenidoDigital' DEBE tener su propia
    # forma de "reproducir", o Python no dejará que el programa funcione.
    @abstractmethod
    def reproducir(self) -> None:
        pass