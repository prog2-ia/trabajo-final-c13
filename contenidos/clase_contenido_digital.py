from abc import ABC, abstractmethod

class ContenidoDigital(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @abstractmethod
    def reproducir(self) -> None:
        pass