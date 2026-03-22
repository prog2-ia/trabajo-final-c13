# Importo la base (EntidadMusical) para que este Influencer 
# siga las mismas reglas que cualquier otro artista del sistema.
from .clase_Entidad import EntidadMusical
# está clase es específica para las gente que vive de los seguidores y las redes 
class Influencer(EntidadMusical):
    def __init__(self, seguidores: int, red_social: str, **kwargs):
        # El super() con **kwargs es muy importante aquí
        # Como luego lo vamos a mezclar con la clase Musico, 
        # esto hace que los datos "pasen de largo" hacia arriba sin romperse
        super().__init__(**kwargs)
        # Estos datos los pongo privados (__). 
        # Solo me interesa que se vean o cambien desde aquí dentro.
        self.__seguidores = seguidores
        self.__red_social = red_social

    def mostrar_detalle(self) -> str:
        # Cumplo con el "contrato" de la clase de arriba (EntidadMusical).
        # Devuelvo un mensaje sencillo con los datos de la red social.
        return f"Influencer en {self.__red_social} con {self.__seguidores} seguidores"