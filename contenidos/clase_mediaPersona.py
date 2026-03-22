# La diseñamos de forma independiente para poder usarla en cualquier clase
# que necesite un responsable (como un Podcast o una Entrevista).
class MediaPersona:
    def __init__(self, anfitrion: str, **kwargs):
        # Permite que, si esta clase se hereda junto con otra (como ContenidoDigital),
        # los argumentos que no son 'anfitrion' sigan su camino hacia el siguiente padre.
        super().__init__(**kwargs)
        # usamos el (_) para indicar que el anfrition 
        # siga su camino hacia el siguiente padre 
        self._anfitrion = anfitrion