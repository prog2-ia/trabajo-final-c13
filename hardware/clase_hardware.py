from abc import ABC, abstractmethod
# Clase Abstracta 'Hardware': Define el estándar para cualquier componente físico.
# Usamos ABC para que nadie pueda crear un objeto 'Hardware' vacío por error.
class Hardware(ABC):
    def __init__(self,potencia:int = 0, **kwargs):
        # Preparado para herencia múltiple cooperativa:
        # Usamos super().__init__(**kwargs) para que, si en el futuro
        # mezclamos hardware con otra clase, los datos no se bloqueen aquí.
        self.potencia = potencia 
        super().__init__(**kwargs)
    # Método Abstracto: Es el "contrato" obligatorio.
    # Cualquier dispositivo (ratón, auriculares, móvil) que conectemos 
    # a nuestra app de música DEBE implementar su propia lógica de conexión.
    @abstractmethod
    def conectar(self) -> None:
        """Contrato obligatorio para cualquier hardware"""
        pass
    # sobrecarga de operadores en este caso comparación 
    def __gt__(self, otro):
        #compara si un hardware es más potente que otro
        if not isinstance(otro, Hardware):
            # Si no es un objeto de tipo Hardware, no sabemos cómo comparar
            return NotImplemented 
        
        # Comparamos basándonos en el atributo potencia
        return self.potencia > otro.potencia