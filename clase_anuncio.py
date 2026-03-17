from abc import ABC, abstractmethod # Necesario para la abstracción [cite: 1586]

# clase abstracta 
class ContenidoReproducible(ABC):
    def __init__(self, **kwargs):
        # Uso de kwargs para asegurar compatibilidad en jerarquías complejas
        super().__init__(**kwargs)

    @abstractmethod
    def reproducir(self) -> None:
        pass

# clase anuncio con herencia y encapsulamiento 
class Anuncio(ContenidoReproducible):
    def __init__(self, patrocinador: str, duracion: int, **kwargs):
        """
        Inicializador de la clase Anuncio. 
        Aplica herencia simple de ContenidoReproducible
        """
        super().__init__(**kwargs)
        # Atributos privados para cumplir con el encapsulamiento 
        self.__patrocinador = patrocinador
        self.__duracion = duracion

    # atributos gestionados
    @property
    def patrocinador(self) -> str:
        """Getter para el nombre del patrocinador"""
        return self.__patrocinador

    @property
    def duracion(self) -> int:
        """Getter para la duración en segundos."""
        return self.__duracion

    @duracion.setter
    def duracion(self, valor: int):
        """
        Setter con validación: impide duraciones negativas o nulas
        Protege la integridad lógica del objeto.
        """
        if isinstance(valor, int) and valor > 0:
            self.__duracion = valor
        else:
            print("Error: La duración del anuncio debe ser un entero positivo[cite: 1403].")

    # métodos especiales
    def __str__(self) -> str:
        """Representación para los usuarios"""
        return f"Publicidad: {self.__patrocinador} | Duración: {self.__duracion}s"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(patrocinador='{self.__patrocinador}', duracion={self.__duracion})"

    # métodos de instancia
    def reproducir(self) -> None:
        """
        Implementación del método abstracto 
        Simula la acción de emitir el anuncio.
        """
        print(f"[REPRODUCIENDO ANUNCIO] Patrocinado por: {self.__patrocinador}...")
        print(f"Por favor, espere {self.__duracion} segundos para continuar.")

    # método estático 
    @staticmethod
    def normativa_publicidad() -> str:
        """
        Método estático: no depende de la instancia ni de la clase
        Proporciona información general sobre la política de anuncios.
        """
        return "Normativa: Los anuncios no deben exceder los 30 segundos en cuentas estándar."