#excepciones.py
#Excepciones personalizadas

class LimiteSaltosExcedidoError(Exception):
    #Se lanza cuando un usuario gratuito supera sus saltos permitidos
    def __init__(self,maximo,actuales):
        super().__init__(f"Límite de {maximo} saltos alcanzado. Has usado {actuales} saltos. ¡Actualiza a Premium!")
        self.maximo = maximo
        self.actuales = actuales

class RecursoNoEncontradoError(Exception):
    #Se lanza cuando no se encuentra un recurso (artista,canción,playlist,álbum)
    def __init__(self,tipo,identificador):
        super().__init__(f"{tipo} '{identificador}' no encontrado en la biblioteca")
        self.tipo = tipo
        self.identificador = identificador

class CancionDuplicadaError(Exception):
    #Se lanza al intentar añadir una canción duplicada a playlist, álbum o biblioteca
    def __init__(self,titulo,destino):
        super().__init__(f"La canción '{titulo}' ya existe en {destino}")
        self.titulo = titulo
        self.destino = destino

class ValorInvalidoError(Exception):
    #Se lanza cuando un valor no cumple las validaciones (edad,duración,año,etc.)
    def __init__(self,campo,valor,mensaje):
        super().__init__(f"Valor inválido para {campo} ({valor}): {mensaje}")
        self.campo = campo
        self.valor = valor
        self.mensaje = mensaje

class ArchivoNoEncontradoError(Exception):
    #Se lanza cuando no se encuentra un archivo al intentar leerlo
    def __init__(self,ruta):
        super().__init__(f"El archivo '{ruta}' no existe o no se puede acceder")
        self.ruta = ruta

class FormatoArchivoError(Exception):
    #Se lanza cuando un archivo tiene formato incorrecto al importar
    def __init__(self,linea,numero_linea,esperado):
        super().__init__(f"Error en línea {numero_linea}: '{linea}'. Formato esperado: {esperado}")
        self.linea = linea
        self.numero_linea = numero_linea
        self.esperado = esperado

class SinCancionesError(Exception):
    #Se lanza al intentar reproducir una playlist/álbum vacío
    def __init__(self,tipo,nombre):
        super().__init__(f"No se puede reproducir {tipo} '{nombre}': no tiene canciones")
        self.tipo = tipo
        self.nombre = nombre

class ArtistaDuplicadoError(Exception):
    #Se lanza cuando se intenta registrar un artista que ya existe
    def __init_(self,nombre):
        super().__init__(f"El artista '{nombre}' ya está registrado en la plataforma")
        self.nombre = nombre