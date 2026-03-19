#clase_MixinBeneficios.py

class BeneficiosPremium:
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__descuento=0.2
        self.__calidad_audio="Hi-Fi"
        self.__saltos_ilimitados=True
        self.__sin_publicidad=True

    @property
    def descuento(self):
        return self.__descuento

    @property
    def calidad_audio(self):
        return self.__calidad_audio

    @property
    def sin_publicidad(self):
        return self.__saltos_ilimitados

    def aplicar_descuento(self,precio):
        return precio*(1-self.__descuento)

    def tiene_beneficio(self,beneficio):
        beneficios={"sin_publicidad":self.__sin_publicidad,
                    "saltos_ilimitados":self.__saltos_ilimitados}
        return beneficios.get(beneficio,False)