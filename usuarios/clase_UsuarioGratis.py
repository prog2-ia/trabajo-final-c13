# HERENCIA: Extiende Usuario | SIN MIXINS (solo Premium los usa)

from usuarios.clase_Usuario import Usuario


class UsuarioGratis(Usuario):
    #Usuario gratuito: anuncios, calidad estándar, 6 saltos máximos.

    def __init__(self, nombre_usuario, nombre_real, **kwargs):
        #No usa Mixins. super() solo llama a Usuario.__init__().
        super().__init__(nombre_usuario=nombre_usuario, nombre_real=nombre_real, **kwargs)
        self.__tiene_anuncios = True
        self.__calidad_audio = "Estándar"

    @property
    def tiene_anuncios(self):
        return self.__tiene_anuncios

    @property
    def calidad_audio(self):
        return self.__calidad_audio

    def ver_anuncio(self):
        #Solo disponible para Gratis. Premium tiene sin_publicidad=True.
        if self.__tiene_anuncios:
            print("Viendo anuncio (30s)...")
            return True
        return False

    def info_cuenta(self):
        print(f"Gratis: {self.nombre_usuario} | Calidad: {self.__calidad_audio} | Anuncios: {self.__tiene_anuncios}")