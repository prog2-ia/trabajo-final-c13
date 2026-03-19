class Notificaciones:
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__email=True
        self.__push=True
        self.__sms=False

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
        self.__email=True
        print("Notificaciones por email activadas")

    def desactivar_email(self):
        self.__email=False
        print("Notificaciones por email desactivadas")

    def activar_push(self):
        self.__push=True
        print("Notificaciones por push activadas")

    def desactivar_push(self):
        self.__push=False
        print("Notificaciones por push desactivadas")

    def estado_notificaciones(self):
        return f"Email:{self.__email},Push:{self.__push}"