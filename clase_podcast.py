
from abc import ABC, abstractmethod

# clase abstracta 
class ContenidoDigital(ABC):
    def __init__(self, **kwargs):
        # Inicialización cooperativa para evitar romper el MRO
        super().__init__(**kwargs)

    @abstractmethod
    def reproducir(self) -> None:
        """Contrato obligatorio para cualquier contenido multimedia"""
        pass

#herencia simple 
class MediaPersona:
    def __init__(self, anfitrion: str, **kwargs):
        super().__init__(**kwargs)
        self._anfitrion = anfitrion # Atributo protegido

#herencia múltiple 
class Podcast(ContenidoDigital, MediaPersona):
    def __init__(self, titulo: str, anfitrion: str, capitulos: int, **kwargs):
        """
        Constructor que coordina múltiples padres mediante super() y **kwargs
        """
        super().__init__(anfitrion=anfitrion, **kwargs)
        self.__titulo = titulo          # Atributo privado 
        self.__capitulos = capitulos    # Atributo privado
        self.__reproducciones = 0        # Atributo privado

    # atributos gestionados 
    @property
    def titulo(self) -> str:
        """Getter para el título del podcast"""
        return self.__titulo

    @property
    def capitulos(self) -> int:
        return self.__capitulos

    @capitulos.setter
    def capitulos(self, valor: int):
        """Validación de datos: evita que el número de capítulos sea inconsistente"""
        if isinstance(valor, int) and valor > 0:
            self.__capacidad = valor
        else:
            print("Error: El número de capítulos debe ser un entero positivo")

    #métodos especiales
    def __str__(self) -> str:
        """Representación informal para el usuario"""
        return f"Podcast: {self.__titulo} por {self._anfitrion} ({self.__capitulos} caps)"

    def __repr__(self) -> str:
        """Representación formal para el programador"""
        return f"{type(self).__name__}(titulo='{self.__titulo}', anfitrion='{self._anfitrion}')"

    # métodos de instancia 
    def reproducir(self) -> None:
        """Implementación del método abstracto (Polimorfismo)."""
        print(f"Abriendo reproductor para el podcast: {self.__titulo}...")

    def reproducir_capitulo(self, num: int) -> None:
        """Lógica de control para reproducir episodios específicos"""
        if 1 <= num <= self.__capitulos: # Operadores de comparación
            self.__reproducciones += 1
            print(f"Reproduciendo capítulo {num} de '{self.__titulo}'.")
        else:
            print(f"Error: El capítulo {num} no existe en la base de datos.")

    #métodos de clase 
    @classmethod
    def desde_diccionario(cls, datos: dict):
        """
        Método de clase: permite crear un objeto Podcast a partir de un dict[cite: 1047].
        Útil para futuras integraciones con JSON/Ficheros.
        """
        return cls(titulo=datos['titulo'], anfitrion=datos['anfitrion'], capitulos=datos['capitulos'])