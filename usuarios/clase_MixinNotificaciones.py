# MIXIN: Notificaciones | HERENCIA MÚLTIPLE con UsuarioPremium

class Notificaciones:

    #Mixin: Gestiona notificaciones (email, push, sms).
    #¿Por qué Mixin? UsuarioGratis NO necesita esto, solo Premium.


    def __init__(self, **kwargs):
        #super__() asegura que todas las clases en MRO se inicialicen.
        super().__init__(**kwargs)
        self.__email = True
        self.__push = True
        self.__sms = False

    @property
    def email_notificaciones(self):
        return self.__email

    @property
    def push_notificaciones(self):
        return self.__push

    @property
    def sms_notificaciones(self):
        return self.__sms

    def activar_email(self):
        self.__email = True
        print(" Email activado")

    def desactivar_email(self):
        self.__email = False
        print(" Email desactivado")

    def activar_push(self):
        self.__push = True
        print(" Push activado")

    def desactivar_push(self):
        self.__push = False
        print(" Push desactivado")

    def estado_notificaciones(self):
        return f"Email:{self.__email}, Push:{self.__push}"