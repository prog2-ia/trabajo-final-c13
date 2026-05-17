from abc import ABC, abstractmethod

# Esta es mi clase base. No voy a crear "Entidades Musicales" sueltas, 
# sino que sirve para que otras clases hereden de ella.
class EntidadMusical(ABC):
    def __init__(self, nombre, **kwargs):
        # Uso el super() con kwargs por si luego se complica la herencia 
        # con más capas. Así Python sabe repartir los datos sin liarse.
        
    
        self._nombre = nombre
        super().__init__(**kwargs) # También pasamos **kwargs hacia arriba por si acaso

    # Aquí viene lo importante: el @abstractmethod
    # Es como un contrato obligatorio. Cualquier artista que yo cree luego 
    # (un solista, un grupo...) TIENE que tener su propio "mostrar_detalle"
    # o el programa me dará un error.
    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass    

    # implemento la sobrecarga de operadores 
    # lo usamos para saber si dos entidades son la misma por su nombre
    def __eq__(self, other):
        if not isinstance(other, EntidadMusical):
            return False
        return self._nombre.lower() == other.nombre.lower()

    # lo usamos para saber cómo ordenar una lista de artistas alfabéticamente
    def __lt__(self, other):
        if not isinstance(other, EntidadMusical):
            return NotImplemented
        return self._nombre.lower() < other.nombre.lower()

    def __add__(self, other):
        if isinstance(other, EntidadMusical):
            nuevo_nombre = f"{self._nombre} ft. {other.nombre}"
            # Al ser abstracta, esto tendrá sentido en las clases hijas
            # que deberán manejar cómo se crea una colaboración.
            print(f"Creando colaboración: {nuevo_nombre}")
            return nuevo_nombre 
        return NotImplemented

    def __iadd__(self, extra_info):
        print(f"Actualizando entidad {self._nombre}...")
        return self