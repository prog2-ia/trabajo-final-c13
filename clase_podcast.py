class Podcast:
    def __init__(self, titulo: str, anfitrion: str, capitulos: int):
        self.titulo: str = titulo
        self.anfitrion: str = anfitrion
        self.capitulos: int = capitulos
        self.reproducciones: int = 0

    def __str__(self) -> str:
        return f"Podcast: {self.titulo} por {self.anfitrion}"

    def reproducir_capitulo(self, num: int) -> None:
        if 1 <= num <= self.capitulos:
            self.reproducciones += 1
            print(f"Reproduciendo capítulo {num} de '{self.titulo}'")
        else:
            print(f"El capítulo {num} no existe.")