from .clase_hardware import Hardware
# La clase Dispositivo hereda de Hardware. Representa un móvil, PC, altavoz, etc.
class Dispositivo(Hardware):
    def __init__(self, nombre: str, tipo: str, **kwargs):
        # super().__init__ asegura que si Hardware tiene procesos internos, se ejecuten.
        super().__init__(**kwargs)
        # Encapsulamiento (Privado '__'): Blindamos el nombre, tipo y volumen.
        # Nadie debería poder poner el volumen a 200% o cambiar el nombre a lo loco.
        self.__nombre = nombre   
        self.__tipo = tipo      
        self.__volumen = 50  # volumen por defecto

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def volumen(self) -> int:
        return self.__volumen

    @volumen.setter
    def volumen(self, valor: int):
        # Encapsulamiento (Privado '__'): Blindamos el nombre, tipo y volumen.
        # Nadie debería poder poner el volumen a 200% o cambiar el nombre a lo loco.
        if isinstance(valor, int):
            if valor < 0: self.__volumen = 0
            elif valor > 100: self.__volumen = 100
            else: self.__volumen = valor
        else:
            print("Error: El volumen debe ser un número entero.")

    def __str__(self) -> str:
        return f"Dispositivo: {self.__nombre} ({self.__tipo}) - Vol: {self.__volumen}%"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre='{self.__nombre}', tipo='{self.__tipo}')"

    def conectar(self) -> None:
        print(f"Sincronizando {self.__nombre} con la librería musical...")

    def subir_volumen(self, valor: int) -> None:
        # Llamamos al setter (self.volumen = valor) para que él haga la validación.
        # Así no repetimos el código de "si es mayor que 100...".
        self.volumen = valor
        print(f"Volumen en {self.__nombre} ajustado al {self.__volumen}%")

    @staticmethod
    def es_compatible(sistema: str) -> bool:
        # Método Estático: No necesita acceder a 'self' porque es una utilidad general.
        # Comprueba si el sistema operativo del usuario funcionará con nuestra app.
        sistemas_validos = ["iOS", "Android", "Windows", "macOS"]
        return sistema in sistemas_validos