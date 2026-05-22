# La diseñamos de forma independiente para poder usarla en cualquier clase
# que necesite un responsable (como un Podcast o una Entrevista).
from typing import Any
class MediaPersona:
    def __init__(self, anfitrion: str, **kwargs: Any) -> None:
        # Guardamos el anfitrión de forma local en la clase de tu compañero
        self.anfitrion = anfitrion
        
        # Extraemos el anfitrion de los kwargs para que no llegue a object.__init__
        kwargs.pop('anfitrion', None)
        
        # Llamamos al super final completamente limpio
        super().__init__(**kwargs)