from clase_MixinBeneficios import BeneficiosPremium
from clase_MixinNotificaciones import Notificaciones
from clase_Usuario import Usuario
class UsuarioPremium(Usuario,BeneficiosPremium,Notificaciones):
    def __init__(self,nombre_usuario,nombre_real,plan="Premium",**kwargs):
        super().__init__(nombre_usuario=nombre_usuario,nombre_real=nombre_real,**kwargs)
        self.plan=plan
        self.puntos_fidelidad=0
        self.saltos_maximos=999

    @property
    def precio_mensual(self):
        precios={"Premium":9.99,"Premium Anual":99.99,"Familiar":14.99}
        return precios.get(self.plan,9.99)

    def info_completa(self):
        return f"{self.nombre_usuario} - Plan {self.plan} - Calidad: {self.calidad_audio} - Precio: {self.precio_mensual}€"

    def precio_con_descuento(self,precio=None):
        if precio is None:
            precio=self.precio_mensual

        precio_final=self.aplicar_descuento(precio)
        print(f"Precio base:{precio}€ y precio con descuento:{precio_final}€")

    def anyadir_puntos(self,puntos):
        self.puntos_fidelidad+=puntos
        print(f"+{puntos} puntos. Total: {self.puntos_fidelidad}")

    def canjear_puntos(self,puntos):
        if puntos<=self.puntos_fidelidad:
            self.puntos_fidelidad-=puntos
            print(f"Canjeados {puntos} puntos. Quedan: {self.puntos_fidelidad}")
            return True
        print(f"ERROR: No tienes suficientes puntos(tienes {self.puntos_fidelidad})")
        return False

    def activar_todo(self):
        self.activar_email()
        self.activar_push()
        print("Todas las notificaciones activadas")

    def estado_cuenta(self):
        print("="*50)
        print(f"USUARIO PREMIUM: {self.nombre_usuario}")
        print(f"Plan: {self.plan}")
        print(f"Precio Mensual: {self.precio_mensual}€")
        print(f"Calidad Audio: {self.calidad_audio}")
        print(f"Sin Publicidad: {self.sin_publicidad}")
        print(f"Saltos Máximos: {self.saltos_maximos}")
        print(f"Notificaciones: {self.estado_notificaciones()}")
        print(f"Puntos Fidelidad: {self.puntos_fidelidad}")
        print("="*50)