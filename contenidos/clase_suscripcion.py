from .clase_servicio import Servicio

class Suscripcion(Servicio):
    def __init__(self, tipo: str, precio: float, **kwargs):
        super().__init__(**kwargs)
        self.__tipo = tipo          
        self.__precio = precio      
        self.__activa = True        

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__precio = float(valor)
        else:
            print("Error: El precio debe ser un valor numérico positivo.")

    @property
    def tipo(self) -> str:
        return self.__tipo

    def __str__(self) -> str:
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Plan {self.__tipo}: {self.__precio}€ ({estado})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(tipo='{self.__tipo}', precio={self.__precio})"

    def cancelar_plan(self) -> None:
        self.__activa = False
        print(f"Suscripción {self.__tipo} cancelada correctamente.")

    def aplicar_descuento(self, porcentaje: float):
        self.__precio -= self.__precio * (porcentaje / 100)
        print(f"Nuevo precio aplicado tras descuento: {self.__precio}€")

    @classmethod
    def crear_plan_estudiante(cls):
        print("Generando suscripción automática con tarifa reducida para estudiantes...")
        return cls(tipo="Estudiante", precio=4.99)