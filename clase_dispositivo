class Dispositivo:
    def __init__(self, nombre: str, tipo: str):
        self.nombre: str = nombre # 'iPhone de Carla', 'PC Salón'
        self.tipo: str = tipo
        self.volumen: int = 50

    def __str__(self) -> str:
        return f"Dispositivo: {self.nombre} ({self.tipo}) - Vol: {self.volumen}%"

    def subir_volumen(self, incremento: int) -> None:
        """Método de instancia con lógica de control[cite: 11]."""
        nuevo_vol = self.volumen + incremento
        self.volumen = nuevo_vol if nuevo_vol <= 100 else 100
        print(f"Volumen en {self.nombre} subido al {self.volumen}%")

    @staticmethod
    def es_compatible(sistema: str) -> bool:
        """Método estático: Función de utilidad independiente[cite: 136]."""
        sistemas_validos = ["iOS", "Android", "Windows", "macOS"]
        return sistema in sistemas_validos