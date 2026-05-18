from abc import ABC, abstractmethod
from typing import Any, Self

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
    def __lt__(self, other: object) -> bool | type(NotImplemented):
        if not isinstance(other, EntidadMusical):
            return NotImplemented
        return self.nombre.lower() < other.nombre.lower()

    # Operador suma  para colaboraciones
    def __add__(self, other: 'EntidadMusical') -> str | type(NotImplemented):
        if isinstance(other, EntidadMusical):
            nuevo_nombre: str = f"{self.nombre} ft. {other.nombre}"
            # Al ser abstracta, esto tendrá sentido en las clases hijas
            # que deberán manejar cómo se crea una colaboración.
            print(f"Creando colaboración: {nuevo_nombre}")
            return nuevo_nombre 
        return NotImplemented

    # Operador de asignación compuesta (+=)
    def __iadd__(self, extra_info: Any) -> Self:
        print(f"Actualizando entidad {self.nombre}...")
        return self