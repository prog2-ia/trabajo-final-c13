from abc import ABC, abstractmethod

class EntidadMusical(ABC):
    def __init__(self, **kwargs):
        super().__init__()

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass