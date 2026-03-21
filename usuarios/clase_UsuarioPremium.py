# HERENCIA MÚLTIPLE: Usuario + BeneficiosPremium + Notificaciones
# MRO: UsuarioPremium → Usuario → BeneficiosPremium → Notificaciones → object

from clase_MixinBeneficios import BeneficiosPremium
from clase_MixinNotificaciones import Notificaciones
from usuarios.clase_Usuario import Usuario


class UsuarioPremium(Usuario, BeneficiosPremium, Notificaciones):

    #Herencia múltiple: combina 3 clases.
    #Orden IMPORTA: Python busca métodos en orden MRO (left-to-right).


    def __init__(self, nombre_usuario, nombre_real, plan="Premium", **kwargs):

        #super().__init__() llama a TODAS las clases padre en orden MRO.
        #Esto inicializa: Usuario + BeneficiosPremium + Notificaciones.

        super().__init__(nombre_usuario=nombre_usuario, nombre_real=nombre_real, **kwargs)
        self.plan = plan
        self.puntos_fidelidad = 0
        self.saltos_maximos = float('inf')  #Valor de infinito

    @property
    def precio_mensual(self):
        #Devuelve el precio según el plan seleccionado.
        precios = {"Premium": 9.99, "Premium Anual": 99.99, "Familiar": 14.99}
        return precios.get(self.plan, 9.99)

    def info_completa(self):
        #Muestra información completa de la cuenta Premium.
        print(f"{self.nombre_usuario} | {self.plan} | {self.calidad_audio} | {self.precio_mensual}€")

    def precio_con_descuento(self, precio=None):

        #Muestra el precio con descuento Premium (20%).
        #Usa el método aplicar_descuento() del Mixin BeneficiosPremium.

        if precio is None:
            precio = self.precio_mensual

        final = self.aplicar_descuento(precio)
        print(f"Base: {precio}€. Con descuento: {final}€")

    def anyadir_puntos(self, puntos):
        #Añade puntos de fidelidad al usuario.
        self.puntos_fidelidad += puntos
        print(f"+{puntos} puntos (Total: {self.puntos_fidelidad})")

    def canjear_puntos(self, puntos):

        #Canjea puntos de fidelidad si hay suficientes.
        #Retorna True si el canje fue exitoso.

        if puntos <= self.puntos_fidelidad:
            self.puntos_fidelidad -= puntos
            print(f"Canjeados {puntos} puntos (Restan: {self.puntos_fidelidad})")
            return True
        print(f"Insuficientes puntos ({self.puntos_fidelidad})")
        return False

    def activar_todo(self):

        #Activa todas las notificaciones disponibles.
        #Usa los métodos del Mixin Notificaciones.

        self.activar_email()
        self.activar_push()
        print("Todas las notificaciones activadas")

    def estado_cuenta(self):

        #Muestra un resumen completo del estado de la cuenta Premium.
        #Incluye datos de Usuario + ambos Mixins (Beneficios + Notificaciones).

        print("=" * 50)
        print(f"PREMIUM: {self.nombre_usuario}")
        print(f"Plan: {self.plan} | Precio: {self.precio_mensual}€")
        print(f"Calidad: {self.calidad_audio} | Sin anuncios: {self.sin_publicidad}")
        print(f"Saltos: Ilimitados | Puntos: {self.puntos_fidelidad}")
        print(f"Notificaciones: {self.estado_notificaciones()}")
        print("=" * 50)