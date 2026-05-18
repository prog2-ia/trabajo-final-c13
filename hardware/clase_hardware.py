from abc import ABC, abstractmethod
from typing import Any

# Clase Abstracta 'Hardware': Define el estándar para cualquier componente físico.
# Usamos ABC para que nadie pueda crear un objeto 'Hardware' vacío por error.
class Hardware(ABC):
    def __init__(self, potencia: int = 0, **kwargs: Any) -> None:
        # Preparado para herencia múltiple cooperativa:
        # Usamos super().__init__(**kwargs) para que, si en el futuro
        # mezclamos hardware con otra clase, los datos no se bloqueen aquí.
        self.potencia: int = potencia 
        super().__init__(**kwargs)

    
    # Cualquier dispositivo (ratón, auriculares, móvil) que conectemos 
    # a nuestra app de música DEBE implementar su propia lógica de conexión.
    @abstractmethod
    def conectar(self) -> None:
        """Contrato obligatorio para cualquier hardware"""
        pass

    # sobrecarga de operadores
    # Tipamos con 'object' el operando
    def __gt__(self, otro: object) -> bool | type[NotImplemented]:
        # Compara si un hardware es más potente que otro
        if not isinstance(otro, Hardware):
            # Si no es un objeto de tipo Hardware, devolvemos la constante del sistema
            return NotImplemented 
        
        # Comparamos basándonos en el atributo potencia
        return self.potencia > otro.potencia