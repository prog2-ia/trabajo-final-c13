#clase_Usuario.py
from clase_Usuario import Usuario
class UsuarioGratis(Usuario):
    def __init__(self,nombre_usuario,nombre_real,**kwargs):
        super().__init__(nombre_usuario=nombre_usuario,nombre_real=nombre_real,**kwargs)
        self.__tiene_anuncios=True
        self.__calidad_audio="Estándar"

    @property
    def tiene_anuncios(self):
        return self.__tiene_anuncios

    @property
    def calidad_audio(self):
        return self.__calidad_audio

    def ver_anuncio(self):
        if self.__tiene_anuncios:
            print("Viendo anuncio...(30 segundos)")
            return True
        return False

    def info_cuenta(self):
        return f"Usuario Gratis: {self.nombre_usuario} - Calidad: {self.__calidad_audio}"