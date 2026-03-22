from .clase_Entidad import EntidadMusical

class Musico(EntidadMusical):
    def __init__(self, nombre: str, instrumento: str, **kwargs):
        super().__init__(**kwargs)
        self._nombre = nombre 
        self.__instrumento = instrumento 

    @property
    def nombre(self) -> str:
        return self._nombre

    def mostrar_detalle(self) -> str:
        return f"Músico: {self._nombre} (Instrumento: {self.__instrumento})"