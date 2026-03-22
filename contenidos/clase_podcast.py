from .clase_ContenidoDigital import ContenidoDigital
from .clase_MediaPersona import MediaPersona

class Podcast(ContenidoDigital, MediaPersona):
    def __init__(self, titulo: str, anfitrion: str, capitulos: int, **kwargs):
        # El uso de anfitrion=anfitrion aquí es clave para MediaPersona
        super().__init__(anfitrion=anfitrion, **kwargs)
        self.__titulo = titulo          
        self.__capitulos = capitulos    
        self.__reproducciones = 0        

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def capitulos(self) -> int:
        return self.__capitulos

    @capitulos.setter
    def capitulos(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self.__capitulos = valor # Corregido de self.__capacidad a self.__capitulos
        else:
            print("Error: El número de capítulos debe ser un entero positivo")

    def __str__(self) -> str:
        return f"Podcast: {self.__titulo} por {self._anfitrion} ({self.__capitulos} caps)"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(titulo='{self.__titulo}', anfitrion='{self._anfitrion}')"

    def reproducir(self) -> None:
        print(f"Abriendo reproductor para el podcast: {self.__titulo}...")

    def reproducir_capitulo(self, num: int) -> None:
        if 1 <= num <= self.__capitulos:
            self.__reproducciones += 1
            print(f"Reproduciendo capítulo {num} de '{self.__titulo}'.")
        else:
            print(f"Error: El capítulo {num} no existe.")

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(titulo=datos['titulo'], anfitrion=datos['anfitrion'], capitulos=datos['capitulos'])