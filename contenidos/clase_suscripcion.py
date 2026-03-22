# Importamos la base 'Servicio' para cumplir con el contrato de los pagos.
from .clase_servicio import Servicio
# La clase Suscripcion hereda de Servicio, obligándonos a gestionar el precio y descuentos.
class Suscripcion(Servicio):
    def __init__(self, tipo: str, precio: float, **kwargs):
        super().__init__(**kwargs)
        # Encapsulamiento (Atributos Privados '__'): 
        # Nadie puede cambiar el precio o el estado 'activa' por error desde fuera.
        self.__tipo = tipo          
        self.__precio = precio      
        self.__activa = True        

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        # Validación de negocio: Evitamos precios negativos o datos que no sean números.
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__precio = float(valor)
        else:
            print("Error: El precio debe ser un valor numérico positivo.")

    @property
    def tipo(self) -> str:
        return self.__tipo

    def __str__(self) -> str:
        # Método especial para que al imprimir el objeto salga legible para el usuario.
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Plan {self.__tipo}: {self.__precio:.2f}€ ({estado})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(tipo='{self.__tipo}', precio={self.__precio:.2f})"

    def cancelar_plan(self) -> None:
        self.__activa = False
        print(f"Suscripción {self.__tipo} cancelada correctamente.")

    def aplicar_descuento(self, porcentaje: float):
        # Implementación del método abstracto heredado de 'Servicio'.
        # Calcula el nuevo precio restando el porcentaje indicado.
        self.__precio -= self.__precio * (porcentaje / 100)
        print(f"Nuevo precio aplicado tras descuento: {self.__precio:.2f}€")

    @classmethod
    def crear_plan_estudiante(cls):
        # Método de Clase: Actúa como una "fábrica" de suscripciones.
        # Permite crear un objeto con valores ya predefinidos (Estudiante, 4.99€).
        print("Generando suscripción automática con tarifa reducida para estudiantes...")
        return cls(tipo="Estudiante", precio=4.99)