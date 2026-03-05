class Suscripcion:
    def __init__(self, tipo: str, precio: float):
        self.tipo: str = tipo  # 'Premium', 'Gratis', 'Familiar'
        self.precio: float = precio
        self.activa: bool = True

    def __str__(self) -> str:
        """Método especial para ver el plan[cite: 68]."""
        estado = "Activa" if self.activa else "Inactiva"
        return f"Plan {self.tipo}: {self.precio}€ ({estado})"

    def cancelar_plan(self) -> None:
        """Método de instancia que cambia el estado[cite: 11]."""
        self.activa = False
        print(f"Suscripción {self.tipo} cancelada correctamente.")

    @classmethod
    def crear_plan_estudiante(cls):
        """Método de clase: Constructor alternativo con descuento[cite: 108]."""
        return cls("Estudiante", 4.99)