# CLASE ABSTRACTA: Base para todos los artistas
# IMPLEMENTA: ABC, Encapsulamiento (__atributo), Herencia

from abc import ABC, abstractmethod
from datetime import datetime


class Artista(ABC):
    #Clase base abstracta. Obliga a subclases a implementar tipo() y anyos_carrera().

    total_artistas = 0  # Variable de clase: compartida entre las instancias

    def __init__(self, nombre, pais, edad=None, **kwargs):
        #Inicializa artista. **kwargs permite herencia múltiple con Mixins.
        #super().__init__(**kwargs) es CRUCIAL para que funcione ABC + Mixins.

        super().__init__(**kwargs)

        # Encapsulamiento: __atributo obliga a usar properties (control de acceso)
        self.__nombre = nombre
        self.__pais = pais
        self.__edad = edad
        self.__canciones = []
        self.__albumes = []
        Artista.total_artistas += 1

    # PROPERTIES: Acceso controlado (lectura)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def pais(self):
        return self.__pais

    @property
    def edad(self):
        return self.__edad

    @property
    def canciones(self):
        return self.__canciones

    @property
    def albumes(self):
        return self.__albumes

    # SETTERS: Validación antes de modificar (integridad de datos)
    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self.__nombre = valor
        else:
            raise ValueError("El nombre debe ser un texto no vacío")

    @pais.setter
    def pais(self, valor):
        if isinstance(valor, str) and len(valor) > 0:
            self.__pais = valor
        else:
            raise ValueError("El país debe ser un texto no vacío")

    @edad.setter
    def edad(self, valor):
        if valor is None:
            self.__edad = None
        elif isinstance(valor, int) and valor > 0:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser un número positivo")

    def __str__(self):
        return f"{self.nombre}({self.pais})"

    def agregar_canciones(self, cancion):
        self.canciones.append(cancion)

    def agregar_album(self, album):
        self.albumes.append(album)

    def total_canciones(self):
        #Calcula total: canciones de álbumes + singles individuales.
        total = sum(len(album.canciones) for album in self.albumes)
        total += len(self.canciones)
        print(f"{self.nombre} tiene {total} canciones en total")
        return total

    def numero_albumes(self):
        print(f"{self.nombre} tiene {len(self.albumes)} álbumes en total")
        return len(self.albumes)

    def info(self):
        #Información básica. Subclases sobrescriben para datos específicos.
        if self.edad:
            return f"{self.nombre} es de {self.pais} y tiene {self.edad} años"
        return f"{self.nombre} es de {self.pais}"

    # MÉTODOS ABSTRACTOS: Si subclase no los implementa da error al instanciar
    @abstractmethod
    def tipo(self):
        #Polimorfismo: cada subclase define su tipo (solista/banda)
        pass

    @abstractmethod
    def anyos_carrera(self):
        #Polimorfismo: cada subclase calcula años diferentes (debut/formación)
        pass

    @classmethod
    def estadisticas_artistas(cls):
        #Método de clase: usa cls (no self) para acceder a variable de clase.
        print(f"\n✓ Total artistas registrados: {cls.total_artistas}")