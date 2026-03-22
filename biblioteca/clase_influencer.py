from .clase_Entidad import EntidadMusical

class Influencer(EntidadMusical):
    def __init__(self, seguidores: int, red_social: str, **kwargs):
        super().__init__(**kwargs)
        self.__seguidores = seguidores
        self.__red_social = red_social

    def mostrar_detalle(self) -> str:
        return f"Influencer en {self.__red_social} con {self.__seguidores} seguidores"