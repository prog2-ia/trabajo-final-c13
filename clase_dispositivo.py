from abc import ABC, abstractmethod

# clase abstracta 
class Hardware(ABC):
    def __init__(self, **kwargs):
        # Preparado para herencia múltiple 
        super().__init__(**kwargs)

    @abstractmethod
    def conectar(self) -> None:
        """Contrato para asegurar que todo hardware implemente su conexión"""
        pass

# -clase dispositivo con encapsulamiento 
class Dispositivo(Hardware):
    def __init__(self, nombre: str, tipo: str, **kwargs):
        """
        Inicializador de la clase Dispositivo.
        Hereda de Hardware e inicializa atributos privados
        """
        super().__init__(**kwargs)
        # atributos privados 
        self.__nombre = nombre   
        self.__tipo = tipo      
        self.__volumen = 50      

    # atributos gestionados 
    @property
    def nombre(self) -> str:
        """Getter para el nombre del dispositivo"""
        return self.__nombre

    @property
    def volumen(self) -> int:
        """Acceso gestionado al nivel de volumen"""
        return self.__volumen

    @volumen.setter
    def volumen(self, valor: int):
        """
        Setter con validación: asegura que el volumen esté entre 0 y 100
        """
        if isinstance(valor, int):
            # Lógica de control para mantener el rango 0-100
            if valor < 0:
                self.__volumen = 0
            elif valor > 100:
                self.__volumen = 100
            else:
                self.__volumen = valor
        else:
            print("Error: El volumen debe ser un número entero[cite: 1403].")

    # métodos especiales 
    def __str__(self) -> str:
        return f"Dispositivo: {self.__nombre} ({self.__tipo}) - Vol: {self.__volumen}%"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nombre='{self.__nombre}', tipo='{self.__tipo}')"

    # -métodos de instancia 
    def conectar(self) -> None:
        """Implementación del método abstracto de Hardware"""
        print(f"Sincronizando {self.__nombre} con la librería musical...")

    def subir_volumen(self, incremento: int) -> None:
        """
        Aumenta el volumen usando el setter para validar el rango[cite: 959].
        """
        self.volumen = self.__volumen + incremento # Llama automáticamente al @volumen.setter
        print(f"Volumen en {self.__nombre} ajustado al {self.__volumen}%")

    # método estático
    @staticmethod
    def es_compatible(sistema: str) -> bool:
        """
        Método estático: Función de utilidad independiente de la instancia 
        """
        sistemas_validos = ["iOS", "Android", "Windows", "macOS"]
        return sistema in sistemas_validos