from typing import Any
from .clase_hardware import Hardware

# La clase Dispositivo hereda de Hardware. Representa un móvil, PC, altavoz, etc.
class Dispositivo(Hardware):
    def __init__(self, nombre: str, tipo: str, **kwargs: Any) -> None:
        # super().__init__ asegura que si Hardware tiene procesos internos, se ejecuten.
        super().__init__(**kwargs)
        # Encapsulamiento (Privado '__'): Blindamos el nombre, tipo y volumen.
        self.__nombre: str = nombre   
        self.__tipo: str = tipo      
        self.__volumen: int = 50  # volumen por defecto

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def volumen(self) -> int:
        return self.__volumen

    # control de excepciones
    @volumen.setter
    def volumen(self, valor: int) -> None:
        # Si el valor que intentan asignar no es un entero, lanzamos una excepción real
        if not isinstance(valor, int):
            raise TypeError("Error: El volumen debe ser un número entero.")
            
        # Si el tipo es correcto, controlamos los límites físicos del hardware de forma segura
        if valor < 0: 
            self.__volumen = 0
        elif valor > 100: 
            self.__volumen = 100
        else: 
            self.__volumen = valor

    def __str__(self) -> str:
        return f"Dispositivo: {self.__nombre} ({self.__tipo}) - Vol: {self.__volumen}%"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre='{self.__nombre}', tipo='{self.__tipo}')"

    def conectar(self) -> None:
        # Implementación polimórfica del método abstracto heredado
        print(f"Sincronizando {self.__nombre} con la librería musical...")

    def subir_volumen(self, valor: int) -> None:
        # Llamamos al setter (self.volumen = valor) para que él haga la validación.
        # Así no repetimos el código de comprobar el tipo ni los límites.
        self.volumen = valor
        print(f"Volumen en {self.__nombre} ajustado al {self.__volumen}%")

    # sugerencia de tipos
    @staticmethod
    def es_compatible(sistema: str) -> bool:
        # Método Estático: No necesita acceder a 'self'. Es una utilidad general.
        sistemas_validos: list[str] = ["iOS", "Android", "Windows", "macOS"]
        return sistema in sistemas_validos