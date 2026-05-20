from abc import ABC, abstractmethod
from typing import Any

# Esta es mi clase base. No voy a crear "Entidades Musicales" sueltas, 
# sino que sirve para que otras clases hereden de ella.
class EntidadMusical(ABC):
    def __init__(self, nombre: str, **kwargs: Any) -> None:
        # Uso el super() con kwargs por si luego se complica la herencia 
        # con más capas. Así Python sabe repartir los datos sin liarse.
        self._nombre: str = nombre
        super().__init__(**kwargs)  # También pasamos **kwargs hacia arriba por si acaso

    # --- PROPIEDADES (GETTERS) ---
    # Esto permite hacer 'entidad.nombre' desde fuera de forma segura
    @property
    def nombre(self) -> str:
        return self._nombre

    # Es como un contrato obligatorio. Cualquier artista que yo cree luego 
    # (un solista, un grupo...) TIENE que tener su propio "mostrar_detalle"
    # o el programa nos dará un error.
    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass    

    # Lo usamos para saber si dos entidades son la misma por su nombre
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EntidadMusical):
            return False
        return self.nombre.lower() == other.nombre.lower()

    # Lo usamos para saber cómo ordenar una lista de artistas alfabéticamente
    def __lt__(self, other: object) -> Any:
        if not isinstance(other, EntidadMusical):
            return NotImplemented
        return self.nombre.lower() < other.nombre.lower()

    # Cambiamos el retorno a Any para unificar firmas de operadores mágicos
    def __add__(self, other: object) -> Any:
        if isinstance(other, EntidadMusical):
            return f"{self.nombre} ft. {other.nombre}"
        return NotImplemented

    # Cambiamos el retorno a Any para evitar conflictos estrictos con __add__
    def __iadd__(self, extra_info: Any) -> Any:
        print(f"Actualizando entidad {self.nombre}...")
        return self