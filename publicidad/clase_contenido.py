from abc import ABC, abstractmethod

class ContenidoReproducible(ABC):
    def __init__(self, **kwargs):
        # Uso de kwargs para asegurar compatibilidad en jerarquías complejas
        super().__init__(**kwargs)

    @abstractmethod
    def reproducir(self) -> None:
        """Método abstracto que deben implementar todos los contenidos"""
        pass