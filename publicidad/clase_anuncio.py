# Importamos la base de contenido reproducible para que el anuncio 
# pueda entrar en la cola de reproducción de la app.
from .clase_contenido import ContenidoReproducible
# La clase Anuncio representa la publicidad que escuchan los usuarios "Gratis"
class Anuncio(ContenidoReproducible):
    def __init__(self, patrocinador: str, duracion: int, **kwargs):
        super().__init__(**kwargs)
        # Encapsulamiento (Privado '__'): Protegemos los datos del anunciante.
        self.__patrocinador = patrocinador
        self.__duracion = duracion

    @property
    def patrocinador(self) -> str:
        return self.__patrocinador

    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, valor: int):
        # Lógica de Negocio: Aplicamos la normativa de la empresa.
        # Si intentan poner un anuncio de más de 30 segundos, lo capamos a 30.
        if isinstance(valor, int) and valor > 0:
            if valor > 30:
                self.__duracion = 30
                print(" La duración máxima es 30 segundos. Ajustado a 30.")
            else:
                self.__duracion = valor
        else:
            print("Error: La duración del anuncio debe ser un entero positivo.")

    def __str__(self) -> str:
        return f"Publicidad: {self.__patrocinador} | Duración: {self.__duracion}s"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(patrocinador='{self.__patrocinador}', duracion={self.__duracion})"

    def reproducir(self) -> None:
        # Polimorfismo: Implementamos 'reproducir' de forma distinta a una canción.
        # Un anuncio no se puede saltar, solo se puede esperar a que termine.
        print(f"[REPRODUCIENDO ANUNCIO] Patrocinado por: {self.__patrocinador}...")
        print(f"Por favor, espere {self.__duracion} segundos para continuar.")

    @staticmethod
    def normativa_publicidad() -> str:
        # Método Estático: Es una información informativa general de la empresa.
        # No necesita datos de un anuncio concreto, por eso es @staticmethod.
        return "Normativa: Los anuncios no deben exceder los 30 segundos en cuentas estándar."