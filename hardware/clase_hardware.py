from abc import ABC, abstractmethod
# Clase Abstracta 'Hardware': Define el estándar para cualquier componente físico.
# Usamos ABC para que nadie pueda crear un objeto 'Hardware' vacío por error.
class Hardware(ABC):
    def __init__(self, **kwargs):
        # Preparado para herencia múltiple cooperativa:
        # Usamos super().__init__(**kwargs) para que, si en el futuro
        # mezclamos hardware con otra clase, los datos no se bloqueen aquí.
        super().__init__(**kwargs)
    # Método Abstracto: Es el "contrato" obligatorio.
    # Cualquier dispositivo (ratón, auriculares, móvil) que conectemos 
    # a nuestra app de música DEBE implementar su propia lógica de conexión.
    @abstractmethod
    def conectar(self) -> None:
        """Contrato obligatorio para cualquier hardware"""
        pass