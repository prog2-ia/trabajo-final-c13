from typing import Any
from .clase_contenido import ContenidoReproducible

# La clase Anuncio representa la publicidad que escuchan los usuarios "Gratis"
class Anuncio(ContenidoReproducible):
    def __init__(self, patrocinador: str, duracion: int, **kwargs: Any) -> None:
        # Pasamos de forma explícita la duracion al constructor del padre (ContenidoReproducible)
        # y dejamos los kwargs para otros posibles atributos de la herencia.
        super().__init__(duracion=duracion, **kwargs)
        # Encapsulamiento (Privado '__'): Protegemos los datos del anunciante.
        self.__patrocinador: str = patrocinador
        # Llamamos al setter interno para que aplique el reajuste automático de los 30s
        self.duracion = duracion

    @property
    def patrocinador(self) -> str:
        return self.__patrocinador

    @property
    def duracion(self) -> int:
        return self.__duracion

    # control de excepciones
    @duracion.setter
    def duracion(self, valor: int) -> None:
        """Aplica la normativa de la empresa controlando tipos y valores erróneos"""
        # Si el usuario intenta introducir un tipo incorrecto (str, float, etc.) lanzamos TypeError
        if not isinstance(valor, int):
            raise TypeError("Error: La duración del anuncio debe ser un número entero.")
            
        # Si el tipo es correcto pero el valor es negativo o cero, lanzamos ValueError
        if valor <= 0:
            raise ValueError("Error: La duración del anuncio debe ser un entero positivo.")
            
        # Lógica de Negocio: Si pasa las validaciones pero excede el límite comercial 
        if valor > 30:
            self.__duracion = 30
            print(" La duración máxima es 30 segundos. Ajustado a 30 automáticamente.")
        else:
            self.__duracion = valor

    def __str__(self) -> str:
        return f"Publicidad: {self.__patrocinador} | Duración: {self.__duracion}s"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(patrocinador='{self.__patrocinador}', duracion={self.__duracion})"

    def reproducir(self) -> None:
        # Polimorfismo: Implementamos 'reproducir' de forma distinta a una canción o podcast.
        print(f"[REPRODUCIENDO ANUNCIO] Patrocinado por: {self.__patrocinador}...")
        print(f"Por favor, espere {self.__duracion} segundos para continuar.")

    # sugerencia de tipos 
    @staticmethod
    def normativa_publicidad() -> str:
        # Método Estático: Es una utilidad informativa general de la empresa.
        return "Normativa: Los anuncios no deben exceder los 30 segundos en cuentas estándar."