from typing import Any
from .clase_musico import Musico
from .clase_influencer import Influencer

# Aquí aplico la herencia múltiple: un Artista de Trap es músico e influencer a la vez
class ArtistaTrap(Musico, Influencer):
    nombre: str  # Unifica la propiedad de nombre para evitar el choque en el diamante de herencia

    def __init__(
        self, 
        nombre: str, 
        red_social: str, 
        instrumento: str = "Voz", 
        seguidores: int = 0, 
        estilo: str = "Modern Trap", 
        **kwargs: Any
    ) -> None:
        # Uso super() para mandarle todos los datos a las clases de arriba.
        # Es la forma limpia de que Python reparta cada dato a su dueño (MRO)
        super().__init__(
            nombre=nombre, 
            instrumento=instrumento, 
            seguidores=seguidores, 
            red_social=red_social,
            **kwargs
        )
        # Este es el toque único del trap: el estilo (encapsulado como protegido)
        self._estilo: str = estilo

    # Getter para poder acceder al estilo si lo necesitas desde fuera
    @property
    def estilo(self) -> str:
        return self._estilo

    def mostrar_detalle(self) -> str:
        # Si Musico e Influencer tienen implementado super().mostrar_detalle(),
        # esta línea llamará a toda la cadena correctamente gracias al MRO.
        detalle_padre: str = super().mostrar_detalle()
        return f"{detalle_padre} | Estilo de Trap: {self._estilo}"