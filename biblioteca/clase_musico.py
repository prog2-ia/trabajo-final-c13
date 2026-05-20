# Importo la base (EntidadMusical) para que este Musico 
# cumpla con las reglas generales de cualquier artista.
from .clase_entidad import EntidadMusical
from typing import Any

# Esta es la clase para los artistas que tocan instrumentos.
class Musico(EntidadMusical):
    def __init__(self, nombre: str, instrumento: str, **kwargs: Any) -> None:
        # Paso los argumentos hacia arriba con super() y **kwargs.
        # Esto es clave para que cuando hagamos la herencia múltiple con 
        # ArtistaTrap, no se pierda ningún dato por el camino.
        super().__init__(nombre=nombre, **kwargs)
        
        # Guardamos el instrumento de forma que sea accesible a través de la propiedad
        self._instrumento: str = instrumento 

    # Uso un decorador @property para que el nombre se pueda leer
    # como si fuera un atributo normal, pero de forma controlada.
    @property
    def nombre(self) -> str:
        return self._nombre

    # Añadimos la propiedad para el instrumento. Así tus compañeros pueden leerlo
    # desde fuera sin romper las restricciones ni poder modificarlo por error.
    @property
    def instrumento(self) -> str:
        return self._instrumento

    def mostrar_detalle(self) -> str:
        # Aquí implemento el método que me obligaba la clase abstracta.
        # Devuelvo un mensaje con el nombre y qué instrumento toca.
        return f"Músico: {self.nombre} | Instrumento principal: {self.instrumento}"

    # método de sobrecarga matemática
    # sumamos dos músicos y así creamos una colaboración o banda nueva 
    def __add__(self, otro: object) -> Any:
        if isinstance(otro, Musico):
            nuevo_nombre = f"Dúo: {self.nombre} y {otro.nombre}"
            nuevo_instrumento = f"Conjunto de {self.instrumento} y {otro.instrumento}"
            
            # Retornamos un nuevo objeto Musico con los datos combinados.
            return Musico(nombre=nuevo_nombre, instrumento=nuevo_instrumento)
        
        # Si intentamos sumar algo que no es un músico, devolvemos NotImplemented
        return NotImplemented