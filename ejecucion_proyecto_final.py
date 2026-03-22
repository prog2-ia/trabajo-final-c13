# =============================================================================
# EJECUCIÓN DEL PROYECTO - BIBLIOTECA MUSICAL ESTILO SPOTIFY
# =============================================================================

# Importación de clases
from artistas.clase_ArtistaSolista import ArtistaSolista
from artistas.clase_ArtistaBanda import ArtistaBanda
from canciones.clase_CancionSolo import CancionSolo
from canciones.clase_CancionColaboracion import CancionColaboracion
from clase_Album import Album
from clase_Playlist import Playlist
from usuarios.clase_UsuarioGratis import UsuarioGratis
from usuarios.clase_UsuarioPremium import UsuarioPremium
from artistas.clase_Artista import Artista
from canciones.clase_Cancion import Cancion
from hardware.clase_dispositivo import Dispositivo
from contenidos.clase_suscripcion import Suscripcion
from contenidos.clase_podcast import Podcast
from publicidad.clase_anuncio import Anuncio


class BibliotecaMusical:

    # Contenedor de todos los datos del sistema.
    # Elimina variables globales usando encapsulamiento en una clase.

    def __init__(self):
        # Listas que almacenan todas las instancias creadas por el usuario
        self.artistas = []
        self.canciones_solo = []
        self.canciones_colab = []
        self.albumes = []
        self.playlists = []
        self.usuarios = []


def pedir_entero(mensaje, min_val=None, max_val=None):
    # Valida que el usuario introduzca un número entero dentro del rango.
    # Acepta negativos (-1) para permitir terminar selecciones múltiples.

    while True:
        valor = input(mensaje)
        # Acepta positivos y negativos (ej: -1 para terminar selección)
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            valor = int(valor)
            if min_val is not None and valor < min_val:
                print(f" El valor debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f" El valor debe ser menor o igual a {max_val}")
                continue
            return valor
        print(" Debe introducir un número válido")


def tiene_letras(texto):
    # Comprueba si un texto tiene al menos una letra.
    # Evita que se introduzcan solo números o símbolos ($, %, etc.).

    for caracter in texto:
        if caracter.isalpha():
            return True
    return False


def validar_texto(mensaje, campo):
    # Valida que un campo de texto no esté vacío.
    # Se reutiliza en múltiples menús para evitar código duplicado.

    valor = input(mensaje)
    while len(valor) == 0:
        print(f" {campo} no puede estar vacío")
        valor = input(mensaje)
    return valor


def es_pais_valido(texto):
    # Valida que el país solo tenga letras y espacios.
    # Rechaza números, símbolos y caracteres especiales.

    for caracter in texto:
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True


def validar_pais(mensaje):
    # Valida país: solo letras y espacios.
    # Rechaza números, símbolos y caracteres especiales ($, %, etc.).

    valor = input(mensaje)
    while len(valor) == 0:
        print("El país no puede estar vacío")
        valor = input(mensaje)
    while not es_pais_valido(valor):
        print("No es válido(números y símbolos detectados)")
        valor = input(mensaje)
    return valor


def validar_genero(mensaje):
    # Valida género: solo letras y espacios.
    # Rechaza números, símbolos y caracteres especiales.

    valor = input(mensaje)
    while len(valor) == 0:
        print(" El género no puede estar vacío")
        valor = input(mensaje)
    while not es_pais_valido(valor):  # Reusa la misma validación que país
        print("Género no válido(números y símbolos detectados")
        valor = input(mensaje)
    return valor


def buscar_album(biblio, titulo_album):
    # Busca un álbum por título y artista.
    # Devuelve el álbum si existe, None si no existe.

    for album in biblio.albumes:
        if album.titulo_album == titulo_album:
            return album
    return None


def menu_artistas(biblio):
    # Menú para registrar artistas solistas y bandas.
    # Valida: nombre no vacío, país con letras, año 1900-2026.

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Solista  2. Banda  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Artista solista: requiere nombre, país, edad y año de debut
            nombre = validar_texto("Nombre: ", "El nombre")
            pais = validar_pais("País: ")
            edad = pedir_entero("Edad: ", min_val=0)
            # Año de debut no puede ser futuro (máx 2026)
            debut = pedir_entero("Año debut: ", min_val=1900, max_val=2026)
            biblio.artistas.append(ArtistaSolista(nombre, pais, edad, debut))
            print(f" {nombre} registrado")

        elif opcion == "2":
            # Banda: requiere nombre, país, miembros y año de formación
            nombre = validar_texto("Nombre banda: ", "El nombre")
            pais = validar_pais("País: ")
            miembros = pedir_entero("Miembros: ", min_val=2)
            # Año de formación no puede ser futuro (máx 2026)
            formacion = pedir_entero("Año formación: ", min_val=1900, max_val=2026)
            biblio.artistas.append(ArtistaBanda(nombre, pais, miembros, formacion))
            print(f" {nombre} registrada")

        elif opcion == "3":
            # Muestra todos los artistas registrados usando polimorfismo (info())
            if biblio.artistas:
                for a in biblio.artistas:
                    a.info()
            else:
                print(" No hay artistas registrados")

        elif opcion == "4":
            continuar = False


def menu_canciones(biblio):
    # Menú para registrar canciones solo y colaboraciones.
    # Requiere que existan artistas previamente registrados.
    # Si se especifica álbum: lo busca por título+artista, si no existe lo crea automáticamente y añade la canción.

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Solo  2. Colab  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Canción solo: necesita al menos 1 artista registrado
            if not biblio.artistas:
                print(" Registra artistas primero")
                continue

            print("\n--- Artistas Disponibles ---")
            # enumerate() devuelve índice (i) y valor (a) de cada elemento
            # i = posición (0, 1, 2...), a = objeto artista (para acceder a a.nombre)
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx = pedir_entero("Selecciona artista: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = validar_texto("Título: ", "El título")
            duracion = pedir_entero("Duración (seg): ", min_val=1)
            genero = validar_genero("Género: ")
            # Álbum opcional: si existe lo usa, si no lo crea automáticamente y añade la canción
            album_input = input("Álbum (opcional, Enter para single): ")
            album_nombre = None
            album_obj = None
            if len(album_input) > 0:
                album_nombre = album_input
                # Busca si el álbum ya existe para este artista
                album_encontrado = buscar_album(biblio, album_nombre)
                if album_encontrado:
                    print(f" Usando álbum existente: {album_nombre}")
                    album_obj = album_encontrado
                else:
                    # Crea el álbum automáticamente con año actual
                    print(f" Álbum '{album_nombre}' no existe. Creándolo automáticamente...")
                    anyo_album = pedir_entero("Año del álbum: ", min_val=1900, max_val=2026)
                    album_obj = Album(album_nombre, biblio.artistas[idx], anyo_album)
                    biblio.albumes.append(album_obj)
                    print(f" Álbum '{album_nombre}' creado")

            cancion_solo = CancionSolo(titulo, biblio.artistas[idx], duracion, genero, album_nombre)
            biblio.canciones_solo.append(cancion_solo)

            # AÑADIR CANCIÓN AL ÁLBUM SI EXISTE
            if album_obj is not None:
                album_obj.agrega_cancion(cancion_solo)

            print(f" '{titulo}' de {biblio.artistas[idx].nombre} registrada")

        elif opcion == "2":
            # Colaboración: 1 artista principal + N secundarios (lista)
            if not biblio.artistas:
                print(" Registra artistas primero")
                continue

            print("\n--- Artistas Disponibles ---")
            # enumerate() devuelve índice (i) y valor (a) de cada elemento
            # i = posición (0, 1, 2...), a = objeto artista (para acceder a a.nombre)
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx_principal = pedir_entero("Artista principal: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = validar_texto("Título: ", "El título")
            duracion = pedir_entero("Duración (seg): ", min_val=1)
            genero = validar_genero("Género: ")

            # Bucle para selección múltiple: -1 termina, no puede repetir principal
            # Usamos variable continuar_secundarios para controlar el bucle
            secundarios = []
            continuar_secundarios = True
            while continuar_secundarios:
                print("\n--- Selecciona secundarios (-1 para terminar) ---")
                for i, a in enumerate(biblio.artistas):
                    if i != idx_principal:
                        print(f"{i}. {a.nombre}")
                print("-1. Terminar selección")

                idx_sec = pedir_entero("Artista secundario: ", min_val=-1, max_val=len(biblio.artistas) - 1)
                if idx_sec == -1:
                    continuar_secundarios = False  # ← Sale del bucle sin break
                elif idx_sec == idx_principal:
                    print(" El principal no puede ser secundario")
                else:
                    secundarios.append(biblio.artistas[idx_sec])

            # Álbum opcional: si existe lo usa, si no lo crea automáticamente y añade la canción
            album_input = input("Álbum (opcional, Enter para single): ")
            album_nombre = None
            album_obj = None
            if len(album_input) > 0:
                album_nombre = album_input
                # Busca si el álbum ya existe para este artista principal
                album_encontrado = buscar_album(biblio, album_nombre)
                if album_encontrado:
                    print(f" Usando álbum existente: {album_nombre}")
                    album_obj = album_encontrado
                else:
                    # Crea el álbum automáticamente con año actual
                    print(f" Álbum '{album_nombre}' no existe. Creándolo automáticamente...")
                    anyo_album = pedir_entero("Año del álbum: ", min_val=1900, max_val=2026)
                    album_obj = Album(album_nombre, biblio.artistas[idx_principal], anyo_album)
                    biblio.albumes.append(album_obj)
                    print(f" Álbum '{album_nombre}' creado")

            cancion_colab = CancionColaboracion(titulo, biblio.artistas[idx_principal], duracion, genero, secundarios,
                                                album_nombre)
            biblio.canciones_colab.append(cancion_colab)

            # AÑADIR CANCIÓN AL ÁLBUM SI EXISTE
            if album_obj is not None:
                album_obj.agrega_cancion(cancion_colab)

            print(f" '{titulo}' de {biblio.artistas[idx_principal].nombre} registrada")

        elif opcion == "3":
            # Muestra todas las canciones (solo y colab con formato diferente)
            for c in biblio.canciones_solo:
                print(f" {c.titulo} - {c.artista_principal.nombre}")
            for c in biblio.canciones_colab:
                nombres = ", ".join([a.nombre for a in c.artistas_secundarios])
                print(f" {c.titulo} - {c.artista_principal.nombre} ft. {nombres}")

        elif opcion == "4":
            continuar = False


def menu_albumes(biblio):
    # Menú para crear álbumes y añadir canciones.
    # Relación: álbum pertenece a artista + contiene múltiples canciones.

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Crear  2. Añadir canción  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Crear álbum: requiere artista existente
            if not biblio.artistas:
                print("No hay artistas")
                continue

            print("\n--- Artistas Disponibles ---")
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx = pedir_entero("Selecciona artista: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = validar_texto("Título álbum: ", "El título")
            # Año de álbum no puede ser futuro (máx 2026)
            anyo = pedir_entero("Año: ", min_val=1900, max_val=2026)

            biblio.albumes.append(Album(titulo, biblio.artistas[idx], anyo))
            print(f" Álbum '{titulo}' creado")

        elif opcion == "2":
            # Añadir canción a álbum: valida que existan ambos
            if not biblio.albumes:
                print("No hay álbumes")
            elif not biblio.canciones_solo:
                print("No hay canciones")
            else:
                idx_a = pedir_entero(f"Álbum (0-{len(biblio.albumes) - 1}): ", min_val=0,
                                     max_val=len(biblio.albumes) - 1)
                # Muestra las canciones (solo + colab)
                print("\n--- Canciones Disponibles ---")
                todas_canciones = []

                for i, c in enumerate(biblio.canciones_solo):
                    print(f"{i}. {c.titulo} - {c.artista_principal.nombre} (Solo)")
                    todas_canciones.append(c)

                for j, c in enumerate(biblio.canciones_colab):
                    idx = len(biblio.canciones_solo) + j
                    nombres_sec = ", ".join([a.nombre for a in c.artistas_secundarios])
                    print(f"{idx}. {c.titulo} - {c.artista_principal.nombre} ft. {nombres_sec} (Colab)")
                    todas_canciones.append(c)

                idx_c = pedir_entero(f"Canción (0-{len(todas_canciones) - 1}): ", min_val=0,
                                     max_val=len(todas_canciones) - 1)
                biblio.albumes[idx_a].agrega_cancion(todas_canciones[idx_c])

        elif opcion == "3":
            # Muestra número de canciones por álbum
            for album in biblio.albumes:
                album.numero_canciones_album()

        elif opcion == "4":
            continuar = False


def menu_playlists(biblio):
    # Menú para crear playlists y añadir canciones.
    # Las playlists son contenedores que luego se reproducen.

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Crear  2. Añadir canción  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Crear playlist: nombre no vacío
            nombre = validar_texto("Nombre playlist: ", "El nombre")
            biblio.playlists.append(Playlist(nombre))
            print(f" Playlist '{nombre}' creada")

        elif opcion == "2":
            # Añadir canción: valida que existan playlist y canciones
            if not biblio.playlists:
                print("No hay playlists")
            elif not biblio.canciones_solo:
                print("No hay canciones")
            else:
                idx_p = pedir_entero(f"Playlist (0-{len(biblio.playlists) - 1}): ", min_val=0,
                                     max_val=len(biblio.playlists) - 1)
                # Muestra las canciones (solo + colab) en una lista combinada
                print("\n--- Canciones Disponibles ---")
                todas_canciones = []

                # Primero las solo
                for i, c in enumerate(biblio.canciones_solo):
                    print(f"{i}. {c.titulo} - {c.artista_principal.nombre} (Solo)")
                    todas_canciones.append(c)

                # Luego las colaboraciones
                for j, c in enumerate(biblio.canciones_colab):
                    idx = len(biblio.canciones_solo) + j
                    nombres_sec = ", ".join([a.nombre for a in c.artistas_secundarios])
                    print(f"{idx}. {c.titulo} - {c.artista_principal.nombre} ft. {nombres_sec} (Colab)")
                    todas_canciones.append(c)

                idx_c = pedir_entero(f"Canción (0-{len(todas_canciones) - 1}): ", min_val=0,
                                     max_val=len(todas_canciones) - 1)
                biblio.playlists[idx_p].agregar_cancion(todas_canciones[idx_c])

        elif opcion == "3":
            # Muestra contenido de todas las playlists
            for p in biblio.playlists:
                p.mostrar_canciones()

        elif opcion == "4":
            continuar = False


def menu_usuarios(biblio):
    # Menú para crear usuarios Gratis y Premium.
    # Premium usa herencia múltiple con Mixins (Beneficios + Notificaciones).

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Gratis  2. Premium  3. Ver  4. Guardar playlist  5. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Usuario Gratis: 6 saltos máximos, calidad estándar, con anuncios
            user = validar_texto("Usuario: ", "El nombre de usuario")
            real = validar_texto("Nombre real: ", "El nombre real")
            biblio.usuarios.append(UsuarioGratis(user, real))
            print(f" {user} creado")

        elif opcion == "2":
            # Usuario Premium: saltos ilimitados, Hi-Fi, sin anuncios, 20% descuento
            user = validar_texto("Usuario: ", "El nombre de usuario")
            real = validar_texto("Nombre real: ", "El nombre real")
            plan = input("Plan: ")
            # Si no introduce plan, usa Premium por defecto
            if len(plan) == 0:
                plan = "Premium"
            biblio.usuarios.append(UsuarioPremium(user, real, plan))
            print(f" {user} creado")

        elif opcion == "3":
            # Muestra info diferente según tipo de usuario (polimorfismo)
            for u in biblio.usuarios:
                if isinstance(u, UsuarioGratis):
                    u.info_cuenta()
                else:
                    u.info_completa()

        elif opcion == "4":
            # Guardar playlist en usuario: valida que existan ambos
            if not biblio.usuarios:
                print(" No hay usuarios")
            elif not biblio.playlists:
                print(" No hay playlists")
            else:
                idx_u = pedir_entero(f"Usuario (0-{len(biblio.usuarios) - 1}): ", min_val=0,
                                     max_val=len(biblio.usuarios) - 1)
                idx_p = pedir_entero(f"Playlist (0-{len(biblio.playlists) - 1}): ", min_val=0,
                                     max_val=len(biblio.playlists) - 1)
                biblio.usuarios[idx_u].guardar_playlist(biblio.playlists[idx_p])

        elif opcion == "5":
            continuar = False


def menu_reproduccion(biblio):
    # Reproducción de playlists. Delega a Playlist.reproducir().
    # Import tardío en Playlist para evitar circular import con Usuario.

    if not biblio.usuarios or not biblio.playlists:
        print(" Crea usuarios y playlists primero")
        return

    print("\n--- Usuarios ---")
    for i, u in enumerate(biblio.usuarios):
        print(f"{i}. {u.nombre_usuario}")

    idx_u = pedir_entero("Usuario: ", min_val=0, max_val=len(biblio.usuarios) - 1)

    print("\n--- Playlists ---")
    for i, p in enumerate(biblio.playlists):
        print(f"{i}. {p.nombre} ({len(p.canciones)} canciones)")

    idx_p = pedir_entero("Playlist: ", min_val=0, max_val=len(biblio.playlists) - 1)

    # Delega la reproducción a la playlist (contiene lógica de saltos/escuchar)
    biblio.usuarios[idx_u].reproducir_playlist(biblio.playlists[idx_p])


def menu_estadisticas(biblio):
    # Muestra contadores globales del sistema.
    # Usa métodos de clase para acceder a variables compartidas.

    print("\n" + "=" * 50)
    print(" ESTADÍSTICAS")
    print("=" * 50)
    Artista.estadisticas_artistas()
    CancionSolo.estadisticas_canciones_solo()
    CancionColaboracion.estadisticas_colaboraciones()
    print(f" Álbumes: {len(biblio.albumes)}")
    print(f" Playlists: {len(biblio.playlists)}")
    print(f" Usuarios: {len(biblio.usuarios)}")
    print(f" Reproducciones: {Cancion.reproducciones}")


def menu_adicionales():
    # Menú que incluye: Dispositivo, Suscripción, Podcast, Anuncio.

    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Dispositivo  2. Suscripción  3. Podcast  4. Anuncio  5. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Dispositivo: nombre y tipo no vacíos, volumen 0-100
            nombre = validar_texto("Nombre: ", "El nombre")
            tipo = validar_texto("Tipo: ", "El tipo")
            pc = Dispositivo(nombre, tipo)
            print(pc)
            pc.subir_volumen(pedir_entero("Volumen: ", min_val=0, max_val=100))
        elif opcion == "2":
            # Suscripción: crea plan estudiante, aplica descuento 0-100%
            sub = Suscripcion.crear_plan_estudiante()
            sub.aplicar_descuento(pedir_entero("Descuento %: ", min_val=0, max_val=100))
            print(sub)
        elif opcion == "3":
            # Podcast: título y anfitrión no vacíos, capítulos >= 1
            titulo = validar_texto("Título: ", "El título")
            anfitrion = validar_texto("Anfitrión: ", "El anfitrión")
            podcast = Podcast(titulo, anfitrion, pedir_entero("Capítulos: ", min_val=1))
            podcast.reproducir()
        elif opcion == "4":
            # Anuncio: patrocinador no vacío, duración >= 1 seg
            patrocinador = validar_texto("Patrocinador: ", "El patrocinador")
            ad = Anuncio(patrocinador, pedir_entero("Duración: ", min_val=1,max_val=30))
            ad.reproducir()
        elif opcion == "5":
            continuar = False


def main():
    # Punto de entrada del programa.
    # Crea el contenedor BibliotecaMusical y coordina todos los menús.

    print("\n" + "=" * 60)
    print("SPOTIFY CLON - Alejandro & Carla")
    print("=" * 60)

    # Crear contenedor de datos (elimina variables globales)
    biblio = BibliotecaMusical()

    continuar = True
    while continuar:
        print("\n" + "=" * 60)
        print("1. Artistas  2. Canciones  3. Álbumes  4. Playlists")
        print("5. Usuarios  6. Reproducir  7. Stats  8. Extra  0. Salir")
        print("=" * 60)

        opcion = input("\nOpción: ")

        if opcion == "1":
            menu_artistas(biblio)
        elif opcion == "2":
            menu_canciones(biblio)
        elif opcion == "3":
            menu_albumes(biblio)
        elif opcion == "4":
            menu_playlists(biblio)
        elif opcion == "5":
            menu_usuarios(biblio)
        elif opcion == "6":
            menu_reproduccion(biblio)
        elif opcion == "7":
            menu_estadisticas(biblio)
        elif opcion == "8":
            menu_adicionales()
        elif opcion == "0":
            continuar = False
            print("\n ¡Gracias!")
        else:
            print(" Opción no válida")


if __name__ == "__main__":
    main()