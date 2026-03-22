# Me traigo a los "padres" de esta clase desde sus propios archivos
# para que la herencia funcione aunque estén separados
from .clase_musico import Musico
from .clase_influencer import Influencer
# Aquí aplico la herencia múltiple: un Artista de Trap es músico e influencer a la vez
class ArtistaTrap(Musico, Influencer):
    def __init__(self, nombre: str, instrumento: str, seguidores: int, red_social: str, estilo: str):
        # Uso super() para mandarle todos los datos a las clases de arriba.
        # Es la forma limpia de que Python reparta cada dato a su dueño (MRO)
        # sin que se nos olvide inicializar nada por el camino.
        super().__init__(
            nombre=nombre, 
            instrumento=instrumento, 
            seguidores=seguidores, 
            red_social=red_social
        )
        # este el toque único del trap que es el estilo 
        self.__estilo = estilo

    def mostrar_detalle(self) -> str:
        # Aquí aprovecho lo que ya saben hacer mis "padres" (Musico e Influencer)
        # Guardo su información en una variable y luego le añado el estilo propio
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre} | Estilo: {self.__estilo}"