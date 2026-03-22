# crear clase abstracta 
from abc import ABC, abstractmethod
# Esta es mi clase base. No voy a crear "Entidades Musicales" sueltas, 
# sino que sirve para que otras clases hereden de ella.
class EntidadMusical(ABC):
    def __init__(self, **kwargs):
        # Uso el super() con kwargs por si luego se complica la herencia 
        # con más capas. Así Python sabe repartir los datos sin liarse.
        super().__init__()
    # Aquí viene lo importante: el @abstractmethod
    # Es como un contrato obligatorio. Cualquier artista que yo cree luego 
    # (un solista, un grupo...) TIENE que tener su propio "mostrar_detalle"
    # o el programa me dará un error.
    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass