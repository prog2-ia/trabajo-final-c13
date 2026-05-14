# =============================================================================
# EJECUCIÓN DEL PROYECTO - BIBLIOTECA MUSICAL ESTILO SPOTIFY
# =============================================================================

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


from biblioteca import Genero, ArtistaTrap, Musico, Influencer
from hardware import Dispositivo
from publicidad import Anuncio
from contenidos import Podcast, Suscripcion


# =============================================================================
# CLASE CONTENEDORA: Gestiona todos los datos del sistema
# =============================================================================

class BibliotecaMusical:

    #Contenedor de todos los objetos del sistema.
    #Elimina la necesidad de variables globales.


    def __init__(self):
        #Inicializa todas las listas vacías.
        self.artistas = []
        self.canciones_solo = []
        self.canciones_colab = []
        self.albumes = []
        self.playlists = []
        self.usuarios = []
        self.dispositivos = []
        self.anuncios = []


# =============================================================================
# FUNCIÓN DE VALIDACIÓN DE INPUTS
# =============================================================================

def pedir_entero(mensaje, min_val=None, max_val=None):
    while True:
        valor = input(mensaje)
        if valor.isdigit() or (valor.startswith('-') and valor[1:].isdigit()):
            valor = int(valor)
            if min_val is not None and valor < min_val:
                print(f" El valor debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f" El valor debe ser menor o igual a {max_val}")
                continue
            return valor
        else:
            print(" Debe introducir un número válido")

# =============================================================================
# MENÚS (Todos excepto menu_adicionales reciben 'biblio' como parámetro)
# =============================================================================

def menu_artistas(biblio):
    #Menú para registrar artistas solistas y bandas.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Solista  2. Banda  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Registrar artista solista
            nombre = input("Nombre: ")
            pais = input("País: ")
            edad = pedir_entero("Edad: ", min_val=0)
            debut = pedir_entero("Año debut: ", min_val=1900)
            biblio.artistas.append(ArtistaSolista(nombre, pais, edad, debut))
            print(f" {nombre} registrado")

        elif opcion == "2":
            # Registrar banda
            nombre = input("Nombre banda: ")
            pais = input("País: ")
            miembros = pedir_entero("Miembros: ", min_val=1)
            formacion = pedir_entero("Año formación: ", min_val=1900)
            biblio.artistas.append(ArtistaBanda(nombre, pais, miembros, formacion))
            print(f" {nombre} registrada")

        elif opcion == "3":
            # Ver artistas registrados
            if biblio.artistas:
                for a in biblio.artistas:
                    a.info()
            else:
                print(" No hay artistas registrados")

        elif opcion == "4":
            continuar = False


def menu_canciones(biblio):
    #Menú para registrar canciones solo y colaboraciones.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Solo  2. Colab  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Canción solo: selecciona artista de la lista (objeto)
            if len(biblio.artistas) == 0:
                print(" No hay artistas registrados")
                continue

            print("\n--- Artistas Disponibles ---")
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx = pedir_entero("Selecciona artista: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = input("Título: ")
            duracion = pedir_entero("Duración (seg): ", min_val=1)
            genero = input("Género: ")
            album = input("Álbum (opcional): ") or None

            biblio.canciones_solo.append(CancionSolo(titulo, biblio.artistas[idx], duracion, genero, album))
            print(f" '{titulo}' de {biblio.artistas[idx].nombre} registrada")

        elif opcion == "2":
            # Colaboración: artista principal + secundarios (lista)
            if len(biblio.artistas) == 0:
                print(" No hay artistas registrados")
                continue

            print("\n--- Artistas Disponibles ---")
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx_principal = pedir_entero("Selecciona artista principal: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = input("Título: ")
            duracion = pedir_entero("Duración (seg): ", min_val=1)
            genero = input("Género: ")

            # Bucle para añadir múltiples artistas secundarios
            print("\n--- Selecciona artistas secundarios (escribe -1 para terminar) ---")
            secundarios = []
            continuar_secundarios = True
            while continuar_secundarios:
                for i, a in enumerate(biblio.artistas):
                    if biblio.artistas[i] != biblio.artistas[idx_principal]:
                        print(f"{i}. {a.nombre}")
                print("-1. Terminar selección")

                idx_sec = pedir_entero("Artista secundario: ", min_val=-1, max_val=len(biblio.artistas) - 1)
                if idx_sec == -1:
                    continuar_secundarios = False
                elif idx_sec == idx_principal:
                    print(" El artista principal no puede ser secundario")
                else:
                    secundarios.append(biblio.artistas[idx_sec])

            album = input("Álbum (opcional): ") or None

            biblio.canciones_colab.append(
                CancionColaboracion(titulo, biblio.artistas[idx_principal], duracion, genero, secundarios, album))
            print(f" '{titulo}' de {biblio.artistas[idx_principal].nombre} registrada")

        elif opcion == "3":
            # Ver todas las canciones
            for c in biblio.canciones_solo:
                print(f" {c.titulo} - {c.artista_principal.nombre}")
            for c in biblio.canciones_colab:
                nombres_sec = ", ".join([a.nombre for a in c.artistas_secundarios])
                print(f" {c.titulo} - {c.artista_principal.nombre} ft. {nombres_sec}")

        elif opcion == "4":
            continuar = False


def menu_albumes(biblio):
    #Menú para crear álbumes y añadir canciones.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Crear  2. Añadir canción  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Crear álbum con artista existente
            if len(biblio.artistas) == 0:
                print("No hay artistas")
                continue

            print("\n--- Artistas Disponibles ---")
            for i, a in enumerate(biblio.artistas):
                print(f"{i}. {a.nombre}")

            idx = pedir_entero("Selecciona artista: ", min_val=0, max_val=len(biblio.artistas) - 1)
            titulo = input("Título álbum: ")
            anyo = pedir_entero("Año: ", min_val=1900)

            biblio.albumes.append(Album(titulo, biblio.artistas[idx], anyo))
            print(f" Álbum '{titulo}' creado")

        elif opcion == "2":
            # Añadir canción a álbum existente
            if len(biblio.albumes) == 0:
                print(" No hay álbumes creados")
            elif len(biblio.canciones_solo) == 0:
                print(" No hay canciones registradas")
            else:
                idx_a = pedir_entero(f"Álbum (0-{len(biblio.albumes) - 1}): ", min_val=0,
                                     max_val=len(biblio.albumes) - 1)
                idx_c = pedir_entero(f"Canción (0-{len(biblio.canciones_solo) - 1}): ", min_val=0,
                                     max_val=len(biblio.canciones_solo) - 1)
                biblio.albumes[idx_a].agrega_cancion(biblio.canciones_solo[idx_c])

        elif opcion == "3":
            # Ver álbumes creados
            for album in biblio.albumes:
                album.numero_canciones_album()

        elif opcion == "4":
            continuar = False


def menu_playlists(biblio):
    #Menú para crear playlists y añadir canciones.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Crear  2. Añadir canción  3. Ver  4. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Crear playlist vacía
            nombre = input("Nombre playlist: ")
            biblio.playlists.append(Playlist(nombre))
            print(f" Playlist '{nombre}' creada")

        elif opcion == "2":
            # Añadir canción a playlist
            if len(biblio.playlists) == 0:
                print(" No hay playlists creadas")
            elif len(biblio.canciones_solo) == 0:
                print(" No hay canciones registradas")
            else:
                idx_p = pedir_entero(f"Playlist (0-{len(biblio.playlists) - 1}): ", min_val=0,
                                     max_val=len(biblio.playlists) - 1)
                idx_c = pedir_entero(f"Canción (0-{len(biblio.canciones_solo) - 1}): ", min_val=0,
                                     max_val=len(biblio.canciones_solo) - 1)
                biblio.playlists[idx_p].agregar_cancion(biblio.canciones_solo[idx_c])

        elif opcion == "3":
            # Ver contenido de playlists
            for p in biblio.playlists:
                p.mostrar_canciones()

        elif opcion == "4":
            if len(biblio.playlists) < 2:
                print("Necesitas al menos 2 playlists para fusionar")
                continue
            print("\n--- Playlists disponibles ---")
            for i, p in enumerate(biblio.playlists):
                print(f"{i}. {p.nombre} ({len(p.canciones)} canciones)")
            i1=pedir_entero("Índice Playlist 1: ",0,len(biblio.playlists)-1)
            i2=pedir_entero("Índice Playlist 2: ",0,len(biblio.playlists)-1)
            if i1==i2:
                print("Selecciona dos playlists diferentes")
                continue

            fusion=biblio.playlists[i1]+biblio.playlists[i2]
            biblio.playlists.append(fusion)
            print(f" Fusión creada: '{fusion.nombre}' ({len(fusion.canciones)} canciones)")

        elif opcion == "5":
            continuar=False


def menu_usuarios(biblio):
    #Menú para crear usuarios (Gratis/Premium) y guardar playlists.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Gratis  2. Premium  3. Ver  4. Guardar playlist  5. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            # Crear usuario Gratis
            user = input("Usuario: ")
            real = input("Nombre real: ")
            biblio.usuarios.append(UsuarioGratis(user, real))
            print(f" {user} creado")

        elif opcion == "2":
            # Crear usuario Premium (herencia múltiple con Mixins)
            user = input("Usuario: ")
            real = input("Nombre real: ")
            plan = input("Plan: ") or "Premium"
            biblio.usuarios.append(UsuarioPremium(user, real, plan))
            print(f" {user} creado")

        elif opcion == "3":
            # Ver usuarios registrados
            for u in biblio.usuarios:
                if isinstance(u, UsuarioGratis):
                    u.info_cuenta()
                else:
                    u.info_completa()

        elif opcion == "4":
            # Guardar playlist en usuario
            if len(biblio.usuarios) == 0:
                print(" No hay usuarios")
            elif len(biblio.playlists) == 0:
                print(" No hay playlists")
            else:
                idx_u = pedir_entero(f"Usuario (0-{len(biblio.usuarios) - 1}): ", min_val=0,
                                     max_val=len(biblio.usuarios) - 1)
                idx_p = pedir_entero(f"Playlist (0-{len(biblio.playlists) - 1}): ", min_val=0,
                                     max_val=len(biblio.playlists) - 1)
                biblio.usuarios[idx_u].guardar_playlist(biblio.playlists[idx_p])

        elif opcion == "5":
            #Estadísticas personales del usuario
            if not biblio.usuarios:
                print(" No hay usuarios registrados")
                continue

            idx=pedir_entero("Selecciona usuario:",0,len(biblio.usuarios)-1)
            usuario=biblio.usuarios[idx]

            print(f"|n--- Estadísticas de {usuario.nombre_usuario} ---")
            print(f" Total canciones escuchadas: {usuario.canciones_escuchadas}")
            print(f" Saltos realizados: {len(usuario.historial_saltos)}")

            #Canción más larga (usa operador >)
            mas_larga=usuario.cancion_mas_larga_escuchada()
            if mas_larga:
                print(f"Tu canción más larga: '{mas_larga.titulo}'")
            else:
                print("Aún no has escuchado canciones")

            #Canción más repetida
            cancion_rep,veces=usuario.cancion_mas_escuchada()
            if cancion_rep:
                print(f" Tu canción más repetida: '{cancion_rep.titulo}' ({veces} veces)")
            else:
                print("Aún no has repetido ninguna canción")

        elif opcion == "6":
            continuar = False


def menu_reproduccion(biblio):
    #Menú para reproducir playlists (delega a Playlist.reproducir).
    if not biblio.usuarios or not biblio.playlists:
        print("Crea usuarios y playlists primero")
        return

    print("\n--- Usuarios ---")
    for i, u in enumerate(biblio.usuarios):
        print(f"{i}. {u.nombre_usuario}")

    idx_u = pedir_entero("Usuario: ", min_val=0, max_val=len(biblio.usuarios) - 1)

    print("\n--- Playlists ---")
    for i, p in enumerate(biblio.playlists):
        print(f"{i}. {p.nombre} ({len(p.canciones)} canciones)")

    idx_p = pedir_entero("Playlist: ", min_val=0, max_val=len(biblio.playlists) - 1)

    biblio.usuarios[idx_u].reproducir_playlist(biblio.playlists[idx_p])


def menu_estadisticas(biblio):
    #Muestra estadísticas globales del sistema.
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

def menu_sobrecarga_operadores(biblio):
    """Menú para demostrar la implementación de métodos matemáticos """
    continuar = True
    while continuar:
        print("\n" + "===" * 5 + " LABORATORIO SOBRECARGA (T08) " + "===" * 5)
        print("1. Sumar Músicos (Operador +) -> Crear Colaboración")
        print("2. Comparar Hardware (Operador >) -> Potencia")
        print("3. Sumar Duraciones (Operador +) -> Contenidos")
        print("4. Ver Metadatos (Operador []) -> Indexación")
        print("5. Volver")
        print("=" * 60)
        
        opcion = input("Seleccione una prueba: ")

        if opcion == "1":
            # Demostración de Musico.__add__[cite: 1]
            print("\n--- Registro de Músicos para la Suma ---")
            n1 = input("Nombre Músico 1: ")
            i1 = input("Instrumento 1: ")
            n2 = input("Nombre Músico 2: ")
            i2 = input("Instrumento 2: ")
            
            m1 = Musico(n1, i1)
            m2 = Musico(n2, i2)
            
            # Operación matemática: La convención de T08 devuelve una NUEVA instancia
            colab = m1 + m2
            print("\n>>> RESULTADO DE LA SUMA (m1 + m2):")
            print(colab.mostrar_detalle())

        elif opcion == "2":
            # Demostración de Hardware.__gt__
            print("\n--- Comparativa de Potencia Hardware ---")
            p1 = pedir_entero("Potencia Dispositivo A (W): ", 0)
            p2 = pedir_entero("Potencia Dispositivo B (W): ", 0)
            
            h1 = Dispositivo(nombre="Dispositivo A", potencia=p1)
            h2 = Dispositivo(nombre="Dispositivo B", potencia=p2)
            
            if h1 > h2:
                print(f"\n>>> RESULTADO: {h1.nombre} es más potente que {h2.nombre}")
            else:
                print(f"\n>>> RESULTADO: {h1.nombre} NO es más potente que {h2.nombre}")

        elif opcion == "3":
            # Demostración de ContenidoReproducible.__add__
            d1 = pedir_entero("Duración Podcast 1 (seg): ", 1)
            d2 = pedir_entero("Duración Podcast 2 (seg): ", 1)
            
            pod1 = Podcast(titulo="Podcast A", duracion=d1)
            pod2 = Podcast(titulo="Podcast B", duracion=d2)
            
            # Suma de duraciones
            total = pod1 + pod2
            print(f"\n>>> RESULTADO: La duración combinada es de {total} segundos")

        elif opcion == "4":
            # Demostración de ContenidoReproducible.__getitem__
            tags = ["Comercial", "Verano", "HD", "Estéreo"]
            ad = Anuncio(titulo="Anuncio Pepsi", metadatos=tags)
            
            print(f"\nMetadatos disponibles: {tags}")
            idx = pedir_entero(f"Índice a consultar (0-{len(tags)-1}): ", 0, len(tags)-1)
            
            # Acceso mediante corchetes sobrecargados
            print(f">>> RESULTADO: El metadato en el índice {idx} es: '{ad[idx]}'")

        elif opcion == "5":
            continuar = False


def menu_adicionales():
    #Menú para probar clases adicionales (compañera).
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Dispositivo  2. Suscripción  3. Podcast  4. Anuncio  5. Volver")
        print("=" * 50)
        opcion = input("Opción: ")

        if opcion == "1":
            pc = Dispositivo(input("Nombre: "), input("Tipo: "))
            print(pc)
            pc.subir_volumen(pedir_entero("Volumen: ", min_val=0, max_val=100))
        elif opcion == "2":
            sub = Suscripcion.crear_plan_estudiante()
            sub.aplicar_descuento(pedir_entero("Descuento %: ", min_val=0, max_val=100))
            print(sub)
        elif opcion == "3":
            podcast = Podcast(input("Título: "), input("Anfitrión: "), pedir_entero("Capítulos: ", min_val=1))
            podcast.reproducir()
        elif opcion == "4":
            ad = Anuncio(input("Patrocinador: "), pedir_entero("Duración: ", min_val=1))
            ad.reproducir()
        elif opcion == "5":
            continuar = False



# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def main():
    print("\n" + "=" * 60)
    print(" SPOTIFY CLON - Alejandro & Carla (Edición T08)")
    print("=" * 60)

    biblio = BibliotecaMusical()

    continuar = True
    while continuar:
        print("\n" + "=" * 60)
        print("1. Artistas  2. Canciones  3. Álbumes  4. Playlists")
        print("5. Usuarios  6. Reproducir  7. Stats    8. Extra")
        print("9. SOBRECARGA MATEMÁTICA (T08)  0. Salir") # Nueva opción 9
        print("=" * 60)

        opcion = input("\nOpción: ")

        if opcion == "1":
            menu_artistas(biblio)
        elif opcion == "2":
            menu_canciones(biblio)
        elif opcion == "3":
            # Nota: Implementar lógica de álbumes aquí o llamar a tu función
            pass
        elif opcion == "4":
            # Nota: Implementar lógica de playlists aquí o llamar a tu función
            pass
        elif opcion == "5":
            menu_usuarios(biblio)
        elif opcion == "6":
            menu_reproduccion(biblio)
        elif opcion == "7":
            menu_estadisticas(biblio)
        elif opcion == "8":
            menu_adicionales()
        elif opcion == "9":
            menu_sobrecarga_operadores(biblio)
        elif opcion == "0":
            continuar = False
            print("\n ¡Gracias!")
        else:
            print(" Opción no válida")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    main()