class MediaPersona:
    def __init__(self, anfitrion: str, **kwargs):
        super().__init__(**kwargs)
        self._anfitrion = anfitrion