from .clase_contenido_digital import ContenidoDigital
from .clase_mediaPersona import MediaPersona
# Herencia Múltiple: Podcast hereda de dos clases distintas.
# Es un archivo que se reproduce Y tiene una persona responsable (anfitrión).
class Podcast(ContenidoDigital, MediaPersona):
    def __init__(self, titulo: str, anfitrion: str, capitulos: int, **kwargs):
        # super().__init__ gestiona el MRO (Method Resolution Order).
        # Pasamos 'anfitrion' directamente para que MediaPersona lo reciba,
        # y los 'kwargs' para que el resto de datos sigan fluyendo hacia arriba.
        super().__init__(anfitrion=anfitrion, **kwargs)
        # Encapsulamiento Estricto (Privado):
        # Usamos doble guion bajo (__) para que nadie pueda modificar 
        # el título o los capítulos desde fuera sin pasar por nuestras reglas.
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
    # Validación de datos: Evitamos que el sistema acepte valores absurdos
    # como capítulos negativos o letras donde esperamos números.
    def capitulos(self, valor: int):
        if isinstance(valor, int) and valor > 0:
            self.__capitulos = valor # Corregido de self.__capacidad a self.__capitulos
        else:
            print("Error: El número de capítulos debe ser un entero positivo")

    def __str__(self) -> str:
        # Sobrescritura de __str__: Define cómo se ve el Podcast al hacer un 'print'.
        # usamos self._anfitrion (heredado de MediaPersona).
        return f"Podcast: {self.__titulo} por {self._anfitrion} ({self.__capitulos} caps)"

    def __repr__(self) -> str:
        # lo usamos para depurar y ver el estado del objeto 
        return f"{type(self).__name__}(titulo='{self.__titulo}', anfitrion='{self._anfitrion}')"

    def reproducir(self) -> None:
        # Polimorfismo: Implementamos la forma específica de reproducir de un Podcast,
        # cumpliendo con el contrato de la clase abstracta ContenidoDigital.
        print(f"Abriendo reproductor para el podcast: {self.__titulo}...")

    def reproducir_capitulo(self, num: int) -> None:
        # Lógica de negocio: Controlamos que el capítulo solicitado exista.
        if 1 <= num <= self.__capitulos:
            self.__reproducciones += 1
            print(f"Reproduciendo capítulo {num} de '{self.__titulo}'.")
        else:
            print(f"Error: El capítulo {num} no existe.")

    @classmethod
    def desde_diccionario(cls, datos: dict):
        # Método de Clase: Permite crear un Podcast a partir de un diccionario.
        return cls(titulo=datos['titulo'], anfitrion=datos['anfitrion'], capitulos=datos['capitulos'])