from .clase_Hardware import Hardware

class Dispositivo(Hardware):
    def __init__(self, nombre: str, tipo: str, **kwargs):
        super().__init__(**kwargs)
        self.__nombre = nombre   
        self.__tipo = tipo      
        self.__volumen = 50      

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def volumen(self) -> int:
        return self.__volumen

    @volumen.setter
    def volumen(self, valor: int):
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

    def subir_volumen(self, incremento: int) -> None:
        # Aquí usamos el setter para que valide automáticamente el rango 0-100
        self.volumen = self.__volumen + incremento 
        print(f"Volumen en {self.__nombre} ajustado al {self.__volumen}%")

    @staticmethod
    def es_compatible(sistema: str) -> bool:
        sistemas_validos = ["iOS", "Android", "Windows", "macOS"]
        return sistema in sistemas_validos