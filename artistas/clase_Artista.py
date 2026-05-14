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
        from excepciones import ValorInvalidoError
        if not isinstance(valor,str) or len(valor.strip()) == 0:
            raise ValorInvalidoError("nombre",valor,"debe ser un texto no vacío")
        self.__nombre = valor

    @pais.setter
    def pais(self, valor):
        from excepciones import ValorInvalidoError
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValorInvalidoError("país",valor,"debe ser un texto no vacío")
        self.__pais = valor

    @edad.setter
    def edad(self, valor):
        from excepciones import ValorInvalidoError
        if valor is None:
            self.__edad = None
        elif not isinstance(valor,int):
            raise ValorInvalidoError("edad",valor, "debe ser un número entero")
        elif valor < 0 or valor > 110:
            raise ValorInvalidoError("edad",valor,"debe estar entre 0 y 110 años")
        self.__edad = valor

    def __str__(self):
        return f"{self.nombre}({self.pais})"

    def __add__(self, otro):
        #artista1 + artista2 → string de colaboración
        if not isinstance(otro, Artista):
            return str(self)
        return f"{self.nombre} + {otro.nombre} -> Colaboración pendiente"

    def __eq__(self, otro):
        #Dos artistas son iguales si coinciden nombre y país
        if not isinstance(otro, Artista):
            return False
        return (self.nombre.lower() == otro.nombre.lower() and
                self.pais.lower() == otro.pais.lower())

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
        print(f"\n Total artistas registrados: {cls.total_artistas}")