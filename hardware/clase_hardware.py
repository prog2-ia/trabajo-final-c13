from abc import ABC, abstractmethod

class Hardware(ABC):
    def __init__(self, **kwargs):
        # Preparado para herencia múltiple cooperativa
        super().__init__(**kwargs)

    @abstractmethod
    def conectar(self) -> None:
        """Contrato obligatorio para cualquier hardware"""
        pass