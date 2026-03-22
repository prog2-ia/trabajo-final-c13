from .clase_Musico import Musico
from .clase_Influencer import Influencer

class ArtistaTrap(Musico, Influencer):
    def __init__(self, nombre: str, instrumento: str, seguidores: int, red_social: str, estilo: str):
        # MRO Cooperativo: enviamos todo hacia arriba
        super().__init__(
            nombre=nombre, 
            instrumento=instrumento, 
            seguidores=seguidores, 
            red_social=red_social
        )
        self.__estilo = estilo

    def mostrar_detalle(self) -> str:
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre} | Estilo: {self.__estilo}"