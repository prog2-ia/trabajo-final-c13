# Importo la base (EntidadMusical) para que este Influencer 
# siga las mismas reglas que cualquier otro artista del sistema.
from typing import Any
from .clase_entidad import EntidadMusical

# está clase es específica para las gente que vive de los seguidores y las redes 
class Influencer(EntidadMusical):
    def __init__(self, nombre: str, red_social: str, seguidores: int, **kwargs: Any) -> None:
        # El super() con **kwargs es muy importante aquí
        # Como luego lo vamos a mezclar con la clase Musico, 
        # esto hace que los datos "pasen de largo" hacia arriba sin romperse
        super().__init__(nombre=nombre, **kwargs)
        
        # Estos datos los pongo protegidos internamente.
        # Creamos las propiedades abajo para que se lean de forma controlada.
        self._red_social: str = red_social
        self._seguidores: int = seguidores 

    # --- PROPIEDADES DE CONTROL ---
    @property
    def red_social(self) -> str:
        return self._red_social

    @property
    def seguidores(self) -> int:
        return self._seguidores

    def mostrar_detalle(self) -> str:
        # Cumplo con el "contrato" de la clase de arriba (EntidadMusical).
        # Devuelvo un mensaje sencillo con los datos de la red social.
        # Corregido para que use las propiedades seguras sin el doble guion bajo erróneo
        return f"Influencer en {self.red_social} con {self.seguidores} seguidores"