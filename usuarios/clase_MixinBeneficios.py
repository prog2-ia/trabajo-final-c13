# MIXIN: BeneficiosPremium | HERENCIA MÚLTIPLE con UsuarioPremium

class BeneficiosPremium:

    #Mixin: Clase diseñada para combinarse con otras (no se usa sola).
    #Añade: descuento 20%, calidad Hi-Fi, sin anuncios, saltos ilimitados.


    def __init__(self, **kwargs):

        #super().__init__() es CRUCIAL para cadena MRO.
        #Sin esto, Notificaciones no se inicializaría en UsuarioPremium.

        super().__init__(**kwargs)
        self.__descuento = 0.2
        self.__calidad_audio = "Hi-Fi"
        self.__saltos_ilimitados = True
        self.__sin_publicidad = True

    @property
    def descuento(self):
        return self.__descuento

    @property
    def calidad_audio(self):
        return self.__calidad_audio

    @property
    def sin_publicidad(self):
        return self.__sin_publicidad

    def aplicar_descuento(self, precio):
        #Aplica 20% descuento.
        return precio * (1 - self.__descuento)

    def tiene_beneficio(self, beneficio):
        beneficios = {"sin_publicidad": self.__sin_publicidad,
                      "saltos_ilimitados": self.__saltos_ilimitados}
        return beneficios.get(beneficio, False)