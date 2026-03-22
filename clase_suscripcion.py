
from abc import ABC, abstractmethod # Importación para manejo de abstracción

# clase abstracta
# La clase hereda de ABC para evitar ser instanciada directamente
class Servicio(ABC):
    def __init__(self, **kwargs):
        """
        Constructor cooperativo: usa **kwargs para pasar argumentos a través 
        del MRO en herencia múltiple
        """
        super().__init__(**kwargs)
    
    @abstractmethod
    def aplicar_descuento(self, porcentaje: float):
        """
        Método abstracto: define un 'contrato' y obligación para que las 
        subclases implementen su propia lógica de descuentos
        """
        pass

# subclase
# Suscripcion 'es un tipo de' Servicio
class Suscripcion(Servicio):
    def __init__(self, tipo: str, precio: float, **kwargs):
        """
        Inicializador de la clase Suscripcion.
        Llama a super() para asegurar la inicialización cooperativa
        """
        super().__init__(**kwargs)
        self.__tipo = tipo          # Atributo privado: nombre del plan
        self.__precio = precio      # Atributo privado: coste mensual
        self.__activa = True        # Atributo privado: estado de la cuenta

    @property
    def precio(self) -> float:
        """
        Método Getter: permite acceder al atributo privado __precio 
        como si fuera un atributo público
        """
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        """
        Método Setter: protege el estado del objeto validando que el 
        precio sea un número positivo antes de asignar
        """
        # Validación de tipos (int o float) y valor lógico 
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__precio = float(valor)
        else:
            # Notifica error si el dato es inválido 
            print("Error: El precio debe ser un valor numérico positivo.")

    @property
    def tipo(self) -> str:
        """Getter para el tipo de plan"""
        return self.__tipo

    # métodos especiales 
    def __str__(self) -> str:
        """
        Representación INFORMAL: dirigida al usuario final
        """
        estado = "Activa" if self.__activa else "Inactiva"
        return f"Plan {self.__tipo}: {self.__precio:.2f}€ ({estado})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(tipo='{self.__tipo}', precio={self.__precio})"

    # métodos de instancia 
    def cancelar_plan(self) -> None:
        """
        Método de instancia: modifica el estado interno del objeto 
        accediendo a sus atributos privados mediante self
        """
        self.__activa = False
        print(f"Suscripción {self.__tipo} cancelada correctamente.")

    def aplicar_descuento(self, porcentaje: float):
        """
        Implementación del método abstracto heredado. 
        Calcula el nuevo precio
        """
        self.__precio -= self.__precio * (porcentaje / 100)
        print(f"Nuevo precio aplicado tras descuento: {self.__precio:.2f}€")

    # método de clase 
    @classmethod
    def crear_plan_estudiante(cls):
        """
        Método de Clase: funciona como constructor alternativo. 
        Recibe la referencia a la clase e instancia un objeto específico
        """
        print("Generando suscripción automática con tarifa reducida para estudiantes...")
        # Llama a la propia clase para crear el objeto [cite: 1057]
        return cls(tipo="Estudiante", precio=4.99)