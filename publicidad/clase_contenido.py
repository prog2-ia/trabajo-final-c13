from abc import ABC, abstractmethod
from typing import Any, Union
__all__ = ['Podcast', 'Suscripcion']

# Clase Abstracta 'ContenidoReproducible': Es la base para cualquier elemento 
# que tenga un flujo de reproducción (canciones, podcasts, anuncios, etc.).
class ContenidoReproducible(ABC):
    def __init__(self, duracion: int = 0, metadatos: list[str] | None = None, **kwargs: Any) -> None:
        self.duracion: int = duracion
        self.metadatos: list[str] = metadatos if metadatos else []
        super().__init__(**kwargs)

    # Método Abstracto: Actúa como un contrato obligatorio.
    @abstractmethod
    def reproducir(self) -> None:
        """Método abstracto que deben implementar todos los contenidos"""
        pass

    # sobrecarga de operadores
    def __add__(self, otro: object) -> Any:
        if isinstance(otro, ContenidoReproducible):
            nueva_duracion: int = self.duracion + otro.duracion
            print(f"Calculando duración total combinada: {nueva_duracion} segundos.")
            return nueva_duracion 
        return NotImplemented

    
    # Utilizada para acceder a los metadatos del contenido por índice.
    def __getitem__(self, indice: Union[int, slice]) -> Union[str, list[str]]:
        try:
            # Delegamos la indexación o el troceado directamente en la lista interna
            return self.metadatos[indice]
        except IndexError:
            # TEMA 9: Si el índice no existe, devolvemos un mensaje informativo controlado
            return "Índice de metadato fuera de rango."