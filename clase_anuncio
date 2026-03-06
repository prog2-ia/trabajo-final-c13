class Anuncio:
    def __init__(self, patrocinador: str, duracion: int):
        self.patrocinador: str = patrocinador
        self.duracion: int = duracion # Segundos

    def __str__(self) -> str:
        return f"Publicidad de {self.patrocinador} ({self.duracion}s)"

    def emitir(self) -> None:
        """Simula la emisión de publicidad[cite: 11]."""
        print(f"Reproduciendo anuncio: '{self.patrocinador}'... por favor espera {self.duracion} segundos.")

    @repr
    def __repr__(self) -> str:
        """Representación formal para el programador[cite: 74]."""
        return f"Anuncio(patrocinador='{self.patrocinador}', duracion={self.duracion})"