import pickle
import os
from typing import Any, Self, Union
from .clase_contenido_digital import ContenidoDigital
from .clase_mediaPersona import MediaPersona

# Herencia Múltiple: Podcast hereda de dos clases distintas.
class Podcast(ContenidoDigital, MediaPersona):
    def __init__(self, titulo: str, anfitrion: str, capitulos: int, **kwargs: Any) -> None:
        # 1. GUARDAMOS LA DURACIÓN DE FORMA LOCAL ANTES DE QUE SE LÍE EL SUPER()
        self._duracion_podcast: int = capitulos
        
        # Guardas tus variables privadas del podcast normalmente
        self.__titulo: str = titulo
        self.__anfitrion: str = anfitrion
        self.__capitulos: int = capitulos
        
        # Llamas al super enviando el anfitrión explícito para que no falle MediaPersona
        super().__init__(duracion=capitulos, anfitrion=anfitrion, **kwargs)     

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def capitulos(self) -> int:
        return self.__capitulos

    @capitulos.setter
    def capitulos(self, valor: int) -> None:
        # Excepciones en lugar de print()
        if not isinstance(valor, int):
            raise TypeError("El número de capítulos debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El número de capítulos debe ser un entero positivo.")
        self.__capitulos = valor

    def __str__(self) -> str:
        return f"Podcast: {self.__titulo} por {self._anfitrion} ({self.__capitulos} caps)"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(titulo='{self.__titulo}', anfitrion='{self._anfitrion}')"

    def __add__(self, otro: object) -> Any:
        if isinstance(otro, Podcast):
            # Sumamos los capítulos usando la variable local blindada que creamos arriba
            total_capitulos: int = self._duracion_podcast + otro._duracion_podcast
            print(f"Calculando duración total combinada de podcasts: {total_capitulos} capítulos/segundos.")
            return total_capitulos
        return NotImplemented

    def reproducir(self) -> None:
        print(f"Abriendo reproductor para el podcast: {self.__titulo}...")

    def reproducir_capitulo(self, num: int) -> None:
        #  Control de rango con excepciones estándar
        if not (1 <= num <= self.__capitulos):
            raise IndexError(f"Error: El capítulo {num} no existe en este podcast.")
        
        self.__reproducciones += 1
        print(f"Reproduciendo capítulo {num} de '{self.__titulo}'.")

    @classmethod
    def desde_diccionario(cls, datos: dict[str, Any]) -> Self:
        return cls(
            titulo=str(datos['titulo']), 
            anfitrion=str(datos['anfitrion']), 
            capitulos=int(datos['capitulos'])
        )

    
    
    def __len__(self) -> int:
        # La longitud del podcast equivale a su número de capítulos totales
        return self.__capitulos

    def __getitem__(self, idx: Union[int, slice]) -> Union[str, list[str]]:
        # Permite indexar con [] (ej: mi_podcast[3]) o trocear con slices (ej: mi_podcast)
        if isinstance(idx, slice):
            # Si se pide un rango (slice), calculamos los inicios/fines válidos
            inicio = idx.start if idx.start is not None else 1
            fin = idx.stop if idx.stop is not None else self.__capitulos + 1
            paso = idx.step if idx.step is not None else 1
            
            return [f"Capítulo {i} de '{self.__titulo}'" for i in range(inicio, fin, paso) if 1 <= i <= self.__capitulos]
        
        # Si pide un índice entero normal
        if not (1 <= idx <= self.__capitulos):
            raise IndexError(f"El capítulo {idx} está fuera de rango.")
        return f"Escuchando Capítulo {idx} de '{self.__titulo}'"
# sobrecarga matematica
    
    def __iadd__(self, extra_caps: int) -> Self:
        # El operador += modifica el propio objeto (self) y lo devuelve (return self)
        if not isinstance(extra_caps, int):
            raise TypeError("Solo puedes añadir una cantidad entera de capítulos.")
        if extra_caps < 0:
            raise ValueError("No se puede añadir una cantidad negativa de capítulos.")
            
        self.__capitulos += extra_caps
        print(f"Se han añadido {extra_caps} capítulos nuevos. Total actual: {self.__capitulos}")
        return self

    # ficheros de texto
    
    def guardar_reporte_txt(self, ruta_fichero: str) -> None:
        """Exporta una ficha técnica del podcast a un fichero legible (.txt)"""
        try:
            # Usamos context manager 'with open' con codificación UTF-8
            with open(ruta_fichero, "w", encoding="utf-8") as writer:
                writer.write(f"=== REPORTE TÉCNICO DE PODCAST ===\n")
                writer.write(f"Título: {self.__titulo}\n")
                writer.write(f"Anfitrión/Responsable: {self._anfitrion}\n")
                writer.write(f"Capítulos totales disponibles: {self.__capitulos}\n")
                writer.write(f"Total histórico de reproducciones de la sesión: {self.__reproducciones}\n")
            print(f"Reporte de texto exportado correctamente en: {ruta_fichero}")
        except OSError as e:
            print(f"Error de E/S al escribir el archivo de texto: {e.strerror}")

    # ficheros binarios
    
    def guardar_binario_pickle(self, ruta_fichero: str) -> None:
        """Serializa el objeto Podcast completo a un archivo binario usando dump()"""
        pickle_file = None
        try:
            # Modo 'wb': Escritura binaria
            pickle_file = open(ruta_fichero, "wb")
            pickle.dump(self, pickle_file)
            print(f"Copia de seguridad binaria guardada con éxito en: {ruta_fichero}")
        except OSError as e:
            print(f"Error de sistema al guardar el pickle: {e.strerror}")
        finally:
            # Estructura obligatoria try-finally para asegurar el cierre del recurso
            if pickle_file is not None:
                pickle_file.close()

    @classmethod
    def cargar_binario_pickle(cls, ruta_fichero: str) -> "Podcast":
        """Restaura un objeto Podcast completo desde un archivo binario usando load()"""
        # Verificamos si existe antes de abrir usando el módulo 'os'
        if not os.path.exists(ruta_fichero):
            raise FileNotFoundError(f"El archivo binario '{ruta_fichero}' no existe.")
            
        pickle_file = None
        try:
            # Modo 'rb': Lectura binaria
            pickle_file = open(ruta_fichero, "rb")
            objeto_restaurado: Podcast = pickle.load(pickle_file)
            
            if not isinstance(objeto_restaurado, cls):
                raise TypeError("El archivo binario no contiene una instancia válida de Podcast.")
                
            return objeto_restaurado
        except OSError as e:
            print(f"Error de sistema al leer el pickle: {e.strerror}")
            raise
        finally:
            if pickle_file is not None:
                pickle_file.close()