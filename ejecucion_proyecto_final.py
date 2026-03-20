# =============================================================================
# EJECUCIÓN DEL PROYECTO - BIBLIOTECA MUSICAL ESTILO SPOTIFY
# =============================================================================

from clase_ArtistaSolista import ArtistaSolista
from clase_ArtistaBanda import ArtistaBanda
from clase_CancionSolo import CancionSolo
from clase_CancionColaboracion import CancionColaboracion
from clase_Album import Album
from clase_Playlist import Playlist
from clase_UsuarioGratis import UsuarioGratis
from clase_UsuarioPremium import UsuarioPremium
from clase_Artista import Artista
from clase_Cancion import Cancion

from clase_dispositivo import Dispositivo
from clase_suscripcion import Suscripcion
from clase_Genero import Genero, ArtistaTrap
from clase_podcast import Podcast
from clase_anuncio import Anuncio


def main():
    """
    Función principal que ejecuta el proyecto.
    Demuestra todas las funcionalidades de ambas partes del equipo.
    """

    # ==========================================================================
    # SECCIÓN 1: ARTISTAS
    # ==========================================================================
    print("=" * 60)
    print("1. REGISTRO DE ARTISTAS")
    print("=" * 60)

    bad_bunny = ArtistaSolista('Bad Bunny', 'Puerto Rico', 29, 2016)
    ysy_a = ArtistaSolista('YSY A', 'Argentina', 27, 2018)
    eminem = ArtistaSolista('Eminem', 'Estados Unidos', 53, 1996)

    coldplay = ArtistaBanda('Coldplay', 'Reino Unido', 4, 1996)
    imagine_dragons = ArtistaBanda('Imagine Dragons', 'Estados Unidos', 4, 2008)
    bts = ArtistaBanda('BTS', 'Corea del Sur', 7, 2013)

    print("\n--- Solistas ---")
    bad_bunny.info()
    ysy_a.info()
    eminem.info()

    print("\n--- Bandas ---")
    coldplay.info()
    imagine_dragons.info()
    bts.info()

    # ==========================================================================
    # SECCIÓN 2: CANCIONES
    # ==========================================================================
    print("\n" + "=" * 60)
    print("2. REGISTRO DE CANCIONES")
    print("=" * 60)

    canciones_solo = [
        CancionSolo('Callaita', 'Bad Bunny', 190, 'Reggaeton', 'OASIS'),
        CancionSolo('Moscow Mule', 'Bad Bunny', 210, 'Reggaeton', 'Un Verano Sin Ti'),
        CancionSolo('Tití Me Preguntó', 'Bad Bunny', 204, 'Reggaeton', 'Un Verano Sin Ti'),
        CancionSolo('FULL ICE', 'YSY A', 157, 'Trap', None),
        CancionSolo('Uzbekistán', 'YSY A', 185, 'Trap', 'Saturación Pop'),
        CancionSolo('Fan De Tus Batallas', 'YSY A', 194, 'House', 'Saturación Pop'),
        CancionSolo('Till I Collapse', 'Eminem', 204, 'Rap', 'The Eminem Show'),
        CancionSolo('Lose Yourself', 'Eminem', 326, 'Rap', '8 Mile'),
        CancionSolo('Yellow', 'Coldplay', 266, 'Rock', 'Parachutes'),
        CancionSolo('The Scientist', 'Coldplay', 309, 'Rock', 'A Rush of Blood'),
        CancionSolo('Believer', 'Imagine Dragons', 204, 'Rock', 'Evolve'),
        CancionSolo('Thunder', 'Imagine Dragons', 187, 'Rock', 'Evolve'),
        CancionSolo('Dynamite', 'BTS', 199, 'K-Pop', 'BE'),
        CancionSolo('Butter', 'BTS', 164, 'K-Pop', None),
    ]

    canciones_colab = [
        CancionColaboracion('I Like It', 'Cardi B', 253, 'Latin Trap', ['Bad Bunny', 'J Balvin'],
                            'Invasion of Privacy'),
        CancionColaboracion('Modo Diablo', 'YSY A', 201, 'Trap', ['Duki', 'Neo Pistea'], 'Trampa N Trap'),
        CancionColaboracion('My Universe', 'BTS', 228, 'K-Pop', ['Coldplay'], 'Music of the Spheres'),
    ]

    CancionSolo.estadisticas_canciones_solo()
    CancionColaboracion.estadisticas_colaboraciones()

    # ==========================================================================
    # SECCIÓN 3: ÁLBUMES
    # ==========================================================================
    print("\n" + "=" * 60)
    print("3. CREACIÓN DE ÁLBUMES")
    print("=" * 60)

    album1 = Album('Un Verano Sin Ti', 'Bad Bunny', 2022)
    album1.agrega_cancion(canciones_solo[1])
    album1.agrega_cancion(canciones_solo[2])

    album2 = Album('Saturación Pop', 'YSY A', 2025)
    album2.agrega_cancion(canciones_solo[4])
    album2.agrega_cancion(canciones_solo[5])

    album3 = Album('The Eminem Show', 'Eminem', 2002)
    album3.agrega_cancion(canciones_solo[6])
    album3.agrega_cancion(canciones_solo[7])

    album4 = Album('Parachutes', 'Coldplay', 2000)
    album4.agrega_cancion(canciones_solo[8])
    album4.agrega_cancion(canciones_solo[9])

    album5 = Album('Evolve', 'Imagine Dragons', 2017)
    album5.agrega_cancion(canciones_solo[10])
    album5.agrega_cancion(canciones_solo[11])

    for album in [album1, album2, album3, album4, album5]:
        album.numero_canciones_album()

    # ==========================================================================
    # SECCIÓN 4: PLAYLISTS
    # ==========================================================================
    print("\n" + "=" * 60)
    print("4. CREACIÓN DE PLAYLISTS")
    print("=" * 60)

    playlist_estudiar = Playlist('Estudiar')
    playlist_estudiar.agregar_cancion(canciones_solo[6])
    playlist_estudiar.agregar_cancion(canciones_solo[8])
    playlist_estudiar.agregar_cancion(canciones_solo[9])

    playlist_fiesta = Playlist('Fiesta')
    playlist_fiesta.agregar_cancion(canciones_solo[0])
    playlist_fiesta.agregar_cancion(canciones_solo[1])
    playlist_fiesta.agregar_cancion(canciones_solo[3])
    playlist_fiesta.agregar_cancion(canciones_colab[0])

    playlist_colabs = Playlist('Colaboraciones')
    for colab in canciones_colab:
        playlist_colabs.agregar_cancion(colab)

    playlist_estudiar.contar_canciones()
    playlist_fiesta.contar_canciones()
    playlist_colabs.contar_canciones()

    # ==========================================================================
    # SECCIÓN 5: USUARIOS
    # ==========================================================================
    print("\n" + "=" * 60)
    print("5. REGISTRO DE USUARIOS")
    print("=" * 60)

    usuario_gratis = UsuarioGratis('alex_11', 'Alejandro Navarro')
    usuario_premium = UsuarioPremium('Valeriaa_29', 'Valeria Lake', plan='Premium')

    usuario_gratis.info_cuenta()
    usuario_premium.info_completa()

    # ==========================================================================
    # SECCIÓN 6: GUARDAR PLAYLISTS
    # ==========================================================================
    print("\n" + "=" * 60)
    print("6. GUARDAR PLAYLISTS")
    print("=" * 60)

    usuario_gratis.guardar_playlist(playlist_estudiar)
    usuario_premium.guardar_playlist(playlist_fiesta)
    usuario_premium.guardar_playlist(playlist_colabs)

    usuario_gratis.cantidad_playlists()
    usuario_premium.cantidad_playlists()

    # ==========================================================================
    # SECCIÓN 7: REPRODUCCIÓN
    # ==========================================================================
    print("\n" + "=" * 60)
    print("7. REPRODUCCIÓN DE MÚSICA")
    print("=" * 60)

    print(f"\n--- {usuario_gratis.nombre_usuario} ---")
    usuario_gratis.escuchar_cancion(canciones_solo[6])
    usuario_gratis.escuchar_cancion(canciones_solo[8])

    print(f"\n--- {usuario_premium.nombre_usuario} ---")
    usuario_premium.escuchar_cancion(canciones_solo[0])
    usuario_premium.escuchar_cancion(canciones_colab[0])

    print("\n--- Estadísticas de Reproducción ---")
    canciones_solo[0].numero_reproducciones()

    # ==========================================================================
    # SECCIÓN 8: SALTOS
    # ==========================================================================
    print("\n" + "=" * 60)
    print("8. SISTEMA DE SALTOS")
    print("=" * 60)

    print(f"\n--- {usuario_gratis.nombre_usuario} (Límite: {usuario_gratis.saltos_maximos}) ---")
    usuario_gratis.avanzar_cancion(canciones_solo[6], playlist_estudiar)
    usuario_gratis.avanzar_cancion(canciones_solo[8], playlist_estudiar)

    print(f"\n--- {usuario_premium.nombre_usuario} (Límite: {usuario_premium.saltos_maximos}) ---")
    usuario_premium.avanzar_cancion(canciones_solo[0], playlist_fiesta)
    usuario_premium.avanzar_cancion(canciones_colab[0], playlist_fiesta)

    # ==========================================================================
    # SECCIÓN 9: ANUNCIOS Y BENEFICIOS
    # ==========================================================================
    print("\n" + "=" * 60)
    print("9. ANUNCIOS Y BENEFICIOS")
    print("=" * 60)

    print(f"\n--- {usuario_gratis.nombre_usuario} (Gratis) ---")
    usuario_gratis.ver_anuncio()
    usuario_gratis.recargar_saltos(2)

    print(f"\n--- {usuario_premium.nombre_usuario} (Premium) ---")
    usuario_premium.estado_cuenta()
    usuario_premium.precio_con_descuento()
    usuario_premium.anyadir_puntos(100)
    usuario_premium.canjear_puntos(50)
    usuario_premium.activar_todo()

    # ==========================================================================
    # SECCIÓN 10: ESTADÍSTICAS FINALES (TUS CLASES)
    # ==========================================================================
    print("\n" + "=" * 60)
    print("10. ESTADÍSTICAS FINALES")
    print("=" * 60)

    Artista.estadisticas_artistas()
    CancionSolo.estadisticas_canciones_solo()
    CancionColaboracion.estadisticas_colaboraciones()
    canciones_solo[0].numero_reproducciones()

    print("\n--- Historial de Saltos ---")
    UsuarioGratis.total_saltos_usuario(usuario_gratis.historial_saltos)
    UsuarioPremium.total_saltos_usuario(usuario_premium.historial_saltos)

    # ==========================================================================
    # SECCIÓN 11: CLASES DE TU COMPAÑERA
    # ==========================================================================
    print("\n" + "=" * 60)
    print("11. PRUEBA DE CLASES ADICIONALES")
    print("=" * 60)

    # --- Dispositivo ---
    print("\n--- Dispositivo ---")
    pc = Dispositivo(nombre="PC Salón", tipo="Ordenador")
    print(pc)
    pc.subir_volumen(60)
    pc.subir_volumen(10)

    # --- Suscripción ---
    print("\n--- Suscripción ---")
    sub = Suscripcion.crear_plan_estudiante()
    sub.aplicar_descuento(10)
    print(sub)

    # --- Género y ArtistaTrap ---
    print("\n--- Género y ArtistaTrap ---")
    trap = Genero("Trap", capacidad_maxima=2)
    bad_bunny_trap = ArtistaTrap(
        nombre="Bad Bunny",
        instrumento="Voz",
        seguidores=45000000,
        red_social="Instagram",
        estilo="Latino"
    )
    trap.registrar_artista(bad_bunny_trap)
    print(trap)

    # --- Podcast ---
    print("\n--- Podcast ---")
    mi_podcast = Podcast(titulo="Charlando Tranquilamente", anfitrion="Ibai", capitulos=15)
    mi_podcast.reproducir()
    mi_podcast.reproducir_capitulo(1)
    print(mi_podcast)

    # --- Anuncio ---
    print("\n--- Anuncio ---")
    spoty_ad = Anuncio(patrocinador="Coca-Cola", duracion=20)
    print(spoty_ad)
    spoty_ad.reproducir()
    print(Anuncio.normativa_publicidad())

    # ==========================================================================
    # RESUMEN FINAL
    # ==========================================================================

    print("=" * 60)
    print("PROYECTO FINALIZADO CORRECTAMENTE")
    print("=" * 60)


# =============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    main()