from abc import ABC, abstractmethod
# Clase Abstracta 'Servicio': Define el comportamiento común para productos de pago.
# Hereda de ABC para asegurar que no se puedan crear instancias de 'Servicio' directamente.
class Servicio(ABC):
    def __init__(self, **kwargs):
        # super().__init__(**kwargs) es fundamental para mantener la cadena de
        # herencia abierta y permitir que esta clase se combine con otras en el futuro.
        super().__init__(**kwargs)
    # Obliga a cualquier clase que herede de 'Servicio' (como Suscripcion)
    # a implementar su propia lógica para aplicar descuentos.
    @abstractmethod
    def aplicar_descuento(self, porcentaje: float):
        pass