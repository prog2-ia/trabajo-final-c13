from abc import ABC, abstractmethod
import math

# Se define una interfaz que todas las subclases deben implementar [cite: 1575, 1587]
class EntidadMusical(ABC):
    def __init__(self, **kwargs):
        super().__init__()

    @abstractmethod
    def mostrar_detalle(self) -> str:
        """Método abstracto que obliga a las subclases a implementarlo"""
        pass

# uso de herencia simple
class Musico(EntidadMusical):
    def __init__(self, nombre: str, instrumento: str, **kwargs):
        # Delegamos en super() usando **kwargs para no saltarnos el MRO
        super().__init__(**kwargs)
        self._nombre = nombre # Atributo protegido 
        self.__instrumento = instrumento # Atributo privado

    @property
    def nombre(self) -> str:
        """Uso de @property para acceder al atributo protegido como un atributo gestionado"""
        return self._nombre

    def mostrar_detalle(self) -> str:
        """Implementación del método abstracto"""
        return f"Músico: {self._nombre} (Instrumento: {self.__instrumento})"

class Influencer(EntidadMusical):
    def __init__(self, seguidores: int, red_social: str, **kwargs):
        super().__init__(**kwargs)
        self.__seguidores = seguidores
        self.__red_social = red_social

    def mostrar_detalle(self) -> str:
        return f"Influencer en {self.__red_social} con {self.__seguidores} seguidores"

# uso de herencia múltiple
# ArtistaTrap hereda de Musico e Influencer de forma simultánea 
class ArtistaTrap(Musico, Influencer):
    def __init__(self, nombre: str, instrumento: str, seguidores: int, red_social: str, estilo: str):
        # Se llama a super() una sola vez enviando todos los argumentos necesarios
        super().__init__(
            nombre=nombre, 
            instrumento=instrumento, 
            seguidores=seguidores, 
            red_social=red_social
        )
        self.__estilo = estilo

    def mostrar_detalle(self) -> str:
        """Extiende la funcionalidad de los padres (Polimorfismo)"""
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre} | Estilo: {self.__estilo}"

# uso de clases, objetos y métodos 
class Genero:
    # Atributo de clase (común a todas las instancias)
    __total_registros_sistema: int = 0 

    def __init__(self, nombre_genero: str, capacidad_maxima: int = 3):
        # Atributos de instancia
        self.__nombre: str = nombre_genero # Encapsulamiento privado
        self.__capacidad: int = capacidad_maxima
        self.__artistas: list[EntidadMusical] = [] # Tipo de dato complejo (Lista) 

    
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def capacidad(self) -> int:
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor: int):
        """Setter con validación de datos para proteger el estado del objeto"""
        if isinstance(valor, int) and valor > 0: # Conversión y comprobación de tipos
            self.__capacidad = valor
        else:
            print("Error: La capacidad debe ser un número entero positivo")

    # uso de métodos especiales
    def __str__(self) -> str:
        """Representación para el usuario"""
        return f"Género: {self.__nombre} ({len(self.__artistas)}/{self.__capacidad} artistas)"

    def __repr__(self) -> str:
        """Representación  que usa el programador"""
        return f"{type(self).__name__}(nombre='{self.__nombre}', capacidad={self.__capacidad})"

    # métodos de instancia 
    def registrar_artista(self, artista: EntidadMusical) -> None:
        """Añade un artista si hay espacio, aprovechando el polimorfismo """
        if len(self.__artistas) < self.__capacidad: # Operadores de comparación 
            self.__artistas.append(artista)
            # Uso de type(self) para acceder al atributo de clase de forma limpia
            type(self).__total_registros_sistema += 1 
            print(f"Éxito: {artista.nombre} añadido al género {self.__nombre}.")
        else:
            print(f"Error: Capacidad máxima de {self.__nombre} alcanzada.")

    # método de clase 
    @classmethod
    def obtener_total_global(cls) -> int:
        """Usa cls para acceder a atributos de clase """
        return cls.__total_registros_sistema

    # métodos estático
    @staticmethod
    def info_sistema() -> None:
        """Método que no requiere ni la instancia ni la clase"""
        print("Sistema de Gestión de Librería Musical v1.0")