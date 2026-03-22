from .clase_contenido import ContenidoReproducible

class Anuncio(ContenidoReproducible):
    def __init__(self, patrocinador: str, duracion: int, **kwargs):
        super().__init__(**kwargs)
        self.__patrocinador = patrocinador
        self.__duracion = duracion

    @property
    def patrocinador(self) -> str:
        return self.__patrocinador

    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            if valor > 30:
                self.__duracion = 30
                print(" La duración máxima es 30 segundos. Ajustado a 30.")
            else:
                self.__duracion = valor
        else:
            print("Error: La duración del anuncio debe ser un entero positivo.")

    def __str__(self) -> str:
        return f"Publicidad: {self.__patrocinador} | Duración: {self.__duracion}s"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(patrocinador='{self.__patrocinador}', duracion={self.__duracion})"

    def reproducir(self) -> None:
        print(f"[REPRODUCIENDO ANUNCIO] Patrocinado por: {self.__patrocinador}...")
        print(f"Por favor, espere {self.__duracion} segundos para continuar.")

    @staticmethod
    def normativa_publicidad() -> str:
        return "Normativa: Los anuncios no deben exceder los 30 segundos en cuentas estándar."