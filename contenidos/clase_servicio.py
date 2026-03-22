from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @abstractmethod
    def aplicar_descuento(self, porcentaje: float):
        pass