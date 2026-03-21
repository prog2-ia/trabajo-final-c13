# CLASE BASE: Usuario | HERENCIA: UsuarioGratis y UsuarioPremium extienden esta


class Usuario:
    #Clase base para usuarios. **kwargs permite herencia múltiple con Mixins.

    def __init__(self, nombre_usuario, nombre_real, **kwargs):

        #**kwargs es CRUCIAL para UsuarioPremium (hereda Usuario + 2 Mixins).
        #Sin esto, los argumentos no llegarían a BeneficiosPremium y Notificaciones.

        super().__init__(**kwargs)
        self.nombre_usuario = nombre_usuario
        self.nombre_real = nombre_real
        self.playlists_usuario = []
        self.canciones_escuchadas = 0
        self.saltos_maximos = 6  # Gratis: 6 saltos | Premium: float('inf')
        self.saltos_actuales = 0
        self.historial_saltos = []

    def guardar_playlist(self, playlist):
        #Añade una playlist a las guardadas por el usuario.
        self.playlists_usuario.append(playlist)
        print(f"{self.nombre_usuario} guardó '{playlist.nombre}'")

    def cantidad_playlists(self):
        #Muestra y retorna la cantidad de playlists guardadas.
        print(f"{self.nombre_usuario} tiene {len(self.playlists_usuario)} playlists")
        return len(self.playlists_usuario)

    def avanzar_cancion(self, cancion, playlist_origen=None):

        #Gestiona salto de canción con límite. Registra en historial para estadísticas.
        #Verifica si tiene saltos infinitos (Premium) o límite (Gratis).

        # Verifica si tiene saltos infinitos (Premium)
        if self.saltos_maximos == float('inf'):
            saltos_mostrar = "Ilimitados"
            tiene_limite = False
        else:
            saltos_mostrar = f"{self.saltos_actuales + 1}/{self.saltos_maximos}"
            tiene_limite = True

        if tiene_limite and self.saltos_actuales >= self.saltos_maximos:
            print(f" Límite de {self.saltos_maximos} saltos alcanzado")
            return False

        self.saltos_actuales += 1
        self.historial_saltos.append((cancion, playlist_origen))
        nombre = playlist_origen.nombre if playlist_origen else "Aleatorio"
        print(f" Saltada '{cancion.titulo}' de '{nombre}' (Saltos: {saltos_mostrar})")
        return True

    def recargar_saltos(self, cantidad):
        #max(0, ...) evita valores negativos si recarga más de lo gastado.
        if self.saltos_maximos == float('inf'):
            print(" Saltos ilimitados (no necesita recarga)")
            return

        self.saltos_actuales = max(0, self.saltos_actuales - cantidad)
        disponibles = self.saltos_maximos - self.saltos_actuales
        print(f" Recargados {cantidad} saltos ({disponibles}/{self.saltos_maximos})")

    def escuchar_cancion(self, cancion):
        #Registra reproducción: actualiza contador usuario Y de la canción.
        self.canciones_escuchadas += 1
        cancion.repros()

    @classmethod
    def canciones_saltadas_de_artista(cls, historial, nombre_artista):
        #Filtra historial por artista. Método de clase (no necesita instancia).
        filtradas = [c for c, p in historial if c.artista_principal.nombre == nombre_artista]
        print(f"Canciones saltadas de {nombre_artista}: {len(filtradas)}")
        return filtradas

    @classmethod
    def canciones_saltadas_de_playlist(cls, historial, playlist):
        #Filtra historial por playlist. Método de clase.
        filtradas = [c for c, p in historial if p == playlist]
        print(f"Canciones saltadas de '{playlist.nombre}': {len(filtradas)}")
        return filtradas

    @classmethod
    def total_saltos_usuario(cls, historial):
        #Muestra y retorna el total de saltos del usuario.
        print(f"Total saltos: {len(historial)}")
        return len(historial)

    def reproducir_playlist(self, playlist):
        #Delega reproducción a playlist (invierte dirección de llamada).
        playlist.reproducir(self)