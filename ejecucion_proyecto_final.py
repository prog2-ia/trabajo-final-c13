# =============================================================================
# EJECUCIÓN DEL PROYECTO - BIBLIOTECA MUSICAL ESTILO SPOTIFY
# =============================================================================
import os
import pickle
from pathlib import Path

def inicializar_directorios():
    #Creo la estructura de directorios para organizar los ficheros
    directorios={
        'data':'data',
        'data/binarios':'data/binarios',
        'data/texto':'data/texto',
        'data/logs':'data/logs',
        'data/backups':'data/backups',
    }

    for ruta in directorios.values():
        try:
            os.makedirs(ruta,exist_ok=True)
            print(f"Directorio '{ruta}' verificado")
        except OSError as e:
            print(f" Error al crear '{ruta}': {e}")

    return directorios

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


from biblioteca import ArtistaTrap, Musico, Influencer
from hardware import Dispositivo
from publicidad import Anuncio
from contenidos import Podcast, Suscripcion
from excepciones import (
    LimiteSaltosExcedidoError,
    RecursoNoEncontradoError,
    CancionDuplicadaError,
    ValorInvalidoError,
    SinCancionesError,
    ArtistaDuplicadoError
)

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

    def guardar_binario(self,directorio='data/binarios'):
        #Guarda toda la biblioteca en fichero binario usando pickle
        try:
            #Crear diccionario con todos los datos
            datos={
                'artistas':self.artistas,
                'canciones_solo':self.canciones_solo,
                'canciones_colab':self.canciones_colab,
                'albumes':self.albumes,
                'playlists':self.playlists,
                'usuarios':self.usuarios
            }

            ruta_archivo = os.path.join(directorio, 'biblioteca.dat')

            #Modo 'wb'=escritura binaria
            with open(ruta_archivo,'wb') as archivo_binario:
                pickle.dump(datos,archivo_binario,protocol=pickle.HIGHEST_PROTOCOL)

            print(f"Datos guardados en binario: '{ruta_archivo}'")
            return True

        except Exception as e:
            print(f"Error al guardar en binario: {e}")
            return False

    def cargar_binario(self,directorio='data/binarios'):
        #Carga toda la biblioteca desde fichero binario usando pickle
        ruta_archivo=os.path.join(directorio,'biblioteca.dat')

        try:
            #Modo 'rb'=lectura binaria
            with open(ruta_archivo,'rb') as archivo_binario:
                datos=pickle.load(archivo_binario)

            #Restaurar todos los objetos
            self.artistas=datos.get('artistas',[])
            self.canciones_solo=datos.get('canciones_solo',[])
            self.canciones_colab=datos.get('canciones_colab',[])
            self.albumes=datos.get('albumes',[])
            self.playlists=datos.get('playlists',[])
            self.usuarios=datos.get('usuarios',[])

            print(f"Datos cargados desde binario: '{ruta_archivo}'")
            return True

        except FileNotFoundError:
            print("Primera ejecución: no existe fichero binario")
            return False
        except Exception as e:
            print(f"Error al cargar desde binario: {e}")
            return False

    def exportar_a_texto(self,directorio='data/texto'):
        #Exporta datos en formato texto legible (.txt)
        try:
            os.makedirs(directorio,exist_ok=True)
            #1.Exportar artistas
            ruta_artistas=os.path.join(directorio,'artistas.txt')
            with open(ruta_artistas,'w',encoding='utf-8') as f:
                f.write("=== ARTISTAS REGISTRADOS ===\n\n")
                for a in self.artistas:
                    tipo = "Solista" if hasattr(a,'fecha_debut') else "Banda"
                    f.write(f"-{a.nombre} ({a.pais}) - Tipo: {tipo}\n")
                f.write(f"\nTotal: {len(self.artistas)} artistas\n")
            print(f"Artistas exportados a: '{ruta_artistas}'")

            #2. Exportar canciones
            ruta_canciones=os.path.join(directorio,'canciones.txt')
            with open(ruta_canciones,'w',encoding='utf-8') as f:
                f.write("=== CANCIONES REGISTRADAS ===\n\n")
                f.write("--- Canciones Solo ---\n")
                for c in self.canciones_solo:
                    f.write(f"- {c.titulo} | {c.artista_principal.nombre} | {c.duracion_seg}s\n")
                f.write("\n--- Colaboraciones ---\n")
                for c in self.canciones_colab:
                    sec=", ".join([art.nombre for art in c.artistas_secundarios])
                    f.write(f"- {c.titulo} | {c.artista_principal.nombre} ft. {sec}\n")
                f.write(f"\nTotal: {len(self.canciones_solo)+len(self.canciones_colab)} canciones\n")
            print(f" Canciones exportadas a: '{ruta_canciones}'")

            #3. Exportar playlists
            ruta_playlists=os.path.join(directorio,'playlists.txt')
            with open(ruta_playlists,'w',encoding='utf-8') as f:
                f.write("=== PLAYLISTS ===\n\n")
                for p in self.playlists:
                    f.write(f"\n {p.nombre}\n")
                    f.write(f"Canciones: {len(p.canciones)}\n")
                    for i, c in enumerate(p.canciones,1):
                        f.write(f" {i}. {c.titulo} - {c.artista_principal.nombre}\n")
                f.write(f"\nTotal: {len(self.playlists)} playlists\n")
            print(f"Playlists exportadas a : '{ruta_playlists}'")

            #4. Exportar usuarios
            ruta_usuarios=os.path.join(directorio,'usuarios.txt')
            with open(ruta_usuarios,'w',encoding='utf-8') as f:
                f.write("=== USUARIOS REGISTRADOS ===\n\n")
                for u in self.usuarios:
                    tipo = "Premium" if isinstance(u,UsuarioPremium) else "Gratis"
                    f.write(f"{u.nombre_usuario} ({u.nombre_real})\n")
                    f.write(f"Tipo: {tipo}\n")
                    f.write(f"Canciones escuchadas: {u.canciones_escuchadas}\n")
                    f.write(f"Saltos:{u.saltos_actuales}/{u.saltos_maximos}\n")
                    if hasattr(u,'historial_canciones') and u.historial_canciones:
                        f.write(f"Historial: {len(u.historial_canciones)} canciones\n")
                    f.write("\n")
                f.write(f"Total: {len(self.usuarios)} usuarios\n")
            print(f"Usuarios exportados a:'{ruta_usuarios}'")
            return True

        except Exception as e:
            print(f"Error al exportar a texto: {e}")
            return False

    @staticmethod
    def guardar_log_actividad(mensaje,directorio='data/logs'):
        #Guarda registro de actividad en fichero log (modo 'a' - append)
        try:
            from datetime import datetime

            ruta_log=os.path.join(directorio,'actividad.log')
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #Modo 'a'=append
            with open(ruta_log,'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {mensaje}\n")

        except Exception as e:
            print(f"Error al guardar log: {e}")


    def guardar_datos(self):
        #Guarda el estado al completo de la biblioteca en ficheros .txt
        try:
            #1.Artistas:nombre|país|edad|tipo|extra(miembros)
            with open("artistas.txt","w",encoding="utf-8") as f:
                for a in self.artistas:
                    tipo='solista' if hasattr(a,'fecha_debut') else "banda"
                    fecha= getattr(a,'fecha_debut',getattr(a, 'fecha_formacion',0))
                    extra= getattr(a,'numero_miembros',0) if tipo == "banda" else 0
                    edad=a.edad if a.edad is not None else "None"
                    f.write(f"{a.nombre}|{a.pais}|{edad}|{tipo}|{fecha}|{extra}\n")

            #2. Canciones Solo: titulo|artista|duracion|genero|album
            with open("canciones_solo.txt","w",encoding="utf-8") as f:
                for c in self.canciones_solo:
                    album=c.album if c.album else "None"
                    f.write(f"{c.titulo}|{c.artista_principal.nombre}|{c.duracion_seg}|{c.genero}|{album}\n")

            #3. Canciones Colaboración: titulo|principal|duracion|genero|secundarios|album
            with open("canciones_colab.txt","w",encoding="utf-8") as f:
                for c in self.canciones_colab:
                    album=c.album if c.album else "None"
                    sec= ",".join([art.nombre for art in c.artistas_secundarios])
                    f.write(f"{c.titulo}|{c.artista_principal.nombre}|{c.duracion_seg}|{c.genero}|{sec}|{album}\n")

            #4. Álbumes:titulo|artista|año
            with open("albumes.txt","w",encoding="utf-8") as f:
                for alb in self.albumes:
                    f.write(f"{alb.titulo_album}|{alb.artista.nombre}|{alb.anyo}\n")

            #5. Playlists: nombre|cancion1,cancion2....
            with open("playlists.txt","w",encoding="utf-8") as f:
                for p in self.playlists:
                    canciones_str = ";".join([c.titulo for c in p.canciones])
                    f.write(f"{p.nombre}|{canciones_str}\n")

            #6. Usuarios: user|real|tipo|plan|saltos_max|saltos_act|escuchadas
            with open("usuarios.txt","w",encoding="utf-8") as f:
                for u in self.usuarios:
                    es_premium = "Premium" if isinstance(u,UsuarioPremium) else "Gratis"
                    plan = getattr(u,'plan',"N/A")
                    f.write(f"{u.nombre_usuario}|{u.nombre_real}|{es_premium}|{plan}|{u.saltos_maximos}|{u.saltos_actuales}|{u.canciones_escuchadas}\n")

            print("Datos guardados correctamente en ficheros .txt")

        except IOError as e:
            print(f" Error de E/S al guardar: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    def cargar_datos(self):
        #Reconstruye la biblioteca desde los ficheros .txt guardados
        try:
            #1. Cargar Artistas (primero porque el resto depende de ellos)
            with open("artistas.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 6:
                        nombre,pais,edad_str,tipo,fecha_str,extra_str=partes
                        edad=int(edad_str) if edad_str!="None" else None
                        fecha=int(fecha_str)
                        if tipo == "solista":
                            self.artistas.append(ArtistaSolista(nombre,pais,edad,fecha))
                        elif tipo == "banda":
                            self.artistas.append(ArtistaBanda(nombre,pais,int(extra_str),fecha))

            #2. Cargar Canciones Solo
            with open("canciones_solo.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 5:
                        titulo,art_nombre,dur,genero,album=partes
                        artista=next((a for a in self.artistas if a.nombre == art_nombre), None)
                        if artista:
                            alb=album if album != "None" else None
                            self.canciones_solo.append(CancionSolo(titulo,artista,int(dur),genero,alb))

            #3. Cargar Canciones Colaboración
            with open("canciones_colab.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 6:
                        titulo,art_princ,dur,genero,sec_str,album=partes
                        artista_p=next((a for a in self.artistas if a.nombre == art_princ), None)
                        if artista_p:
                            secundarios=[next((a for a in self.artistas if a.nombre==n),None) for n in sec_str.split(",") if n]
                            secundarios=[a for a in secundarios if a is not None]
                            alb=album if album!="None" else None
                            self.canciones_colab.append(CancionColaboracion(titulo,artista_p,int(dur),genero,secundarios,alb))

            #4. Cargar Álbumes
            with open("albumes.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 3:
                        titulo,art_nombre,anyo=partes
                        artista=next((a for a in self.artistas if a.nombre == art_nombre),None)
                        if artista:
                            self.albumes.append(Album(titulo,artista,int(anyo)))

            #5. Cargar Playlists
            with open("playlists.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 2:
                        nombre,canciones_str=partes
                        playlist = Playlist(nombre)
                        if canciones_str:
                            titulos=canciones_str.split(";")
                            todas=self.canciones_solo+self.canciones_colab
                            for t in titulos:
                                c=next((c for c in todas if c.titulo==t),None)
                                if c:
                                    playlist.canciones.append(c)
                        self.playlists.append(playlist)

            #6. Cargar Usuarios
            with open("usuarios.txt","r",encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split("|")
                    if len(partes) == 7:
                        user,real,tipo,plan,saltos_max,saltos_act,escuchadas=partes
                        saltos_max=float(saltos_max)
                        if tipo=="Premium":
                            u=UsuarioPremium(user,real,plan)
                        else:
                            u=UsuarioGratis(user,real)
                        u.saltos_maximos=saltos_max
                        u.saltos_actuales=int(saltos_act)
                        u.canciones_escuchadas=int(escuchadas)
                        self.usuarios.append(u)

            print("Datos cargados correctamente desde ficheros .txt")

        except FileNotFoundError:
            print("Primera ejecución: no se encontraron datos guardados.")
        except Exception as e:
            print(f"Error al cargar datos:{e}")




# =============================================================================
# FUNCIÓN DE VALIDACIÓN DE INPUTS
# =============================================================================

def pedir_entero(mensaje, min_val=None, max_val=None):
    while True:
        try:

            valor = int(input(mensaje))
            if min_val is not None and valor < min_val:
                print(f"El valor debe ser mayor o igual a {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f"El valor debe ser menor o igual a {max_val}")
                continue
            return valor
        except ValueError:
            print("Debes introducir un número entero válido")
        except KeyboardInterrupt:
            print("\n Operación cancelada por el usuario")
            return None

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
            try:

                # Registrar artista solista
                nombre = input("Nombre: ")
                artista_existe=False
                for a in biblio.artistas:
                    if a.nombre.lower() == nombre.lower():
                        artista_existe=True
                        break
                if artista_existe:
                    raise ArtistaDuplicadoError(nombre)

                pais = input("País: ")
                edad = pedir_entero("Edad: ", min_val=0)
                if edad is None:
                    continue
                debut = pedir_entero("Año debut: ", min_val=1900)
                if debut is None:
                    continue

                artista=ArtistaSolista(nombre,pais,edad,debut)
                biblio.artistas.append(artista)
                print(f"{nombre} registrado")

            except ArtistaDuplicadoError as e:
                print(f" {e}")
            except ValorInvalidoError as e:
                print(f"Error de validación:{e}")
            except Exception as e:
                print(f"Error inesperado al registrar artista: {e}")


        elif opcion == "2":
            try:
                # Registrar banda
                nombre = input("Nombre banda: ")
                artista_existe=False
                for a in biblio.artistas:
                    if a.nombre.lower() == nombre.lower():
                        artista_existe = True
                        break
                if artista_existe:
                    raise ArtistaDuplicadoError(nombre)

                pais = input("País: ")
                miembros = pedir_entero("Miembros: ", min_val=1)
                if miembros is None:
                    continue
                formacion = pedir_entero("Año formación: ", min_val=1900)
                if formacion is None:
                    continue

                banda=ArtistaBanda(nombre,pais,miembros,formacion)
                biblio.artistas.append(banda)
                print(f" {nombre} registrada")

            except ArtistaDuplicadoError as e:
                print(f" {e}")
            except ValorInvalidoError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error inesperado al registrar banda: {e}")

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
            album_nombre = input("Álbum (opcional): ").strip()

            album_obj=None
            if album_nombre:
                #Buscamos si este álbum ya existe
                album_obj = next((alb for alb in biblio.albumes if alb.titulo_album.lower()==album_nombre.lower()
                                  and alb.artista==biblio.artistas[idx]), None)

            #Si no existe, lo creamos automáticamente
            if not album_obj:
                anyo_actual=2026
                album_obj=Album(album_nombre,biblio.artistas[idx],anyo_actual)
                biblio.albumes.append(album_obj)
                print(f"Álbum '{album_nombre}' creado automáticamente")

            cancion=CancionSolo(titulo,biblio.artistas[idx],duracion,genero,album_obj)
            biblio.canciones_solo.append(cancion)

            #Añadimos canción al álbum si existe
            if album_obj:
                album_obj.agrega_cancion(cancion)

            print(f"'{titulo}' de {biblio.artistas[idx].nombre} registrada")

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
            try:
                nombre = input("Nombre playlist: ")
                if not nombre.strip():
                    print(f"El nombre no puede estar vacío")
                    continue
                biblio.playlists.append(Playlist(nombre))
                print(f"Playlist '{nombre}' creada")
            except Exception as e:
                print(f" Error al crear playlist: {e}")

        elif opcion == "2":
            # Añadir canción a playlist
            try:
                if len(biblio.playlists) == 0:
                    print(" No hay playlists creadas")
                    continue
                if len(biblio.canciones_solo) == 0:
                    print(" No hay canciones registradas")
                    continue

                idx_p = pedir_entero(f"Playlist (0-{len(biblio.playlists) - 1}): ", min_val=0,)

                if idx_p is None:
                    continue
                idx_c = pedir_entero(f"Canción (0-{len(biblio.canciones_solo) - 1}): ", min_val=0, max_val=len(biblio.canciones_solo) - 1)

                if idx_c is None:
                    continue

                from excepciones import CancionDuplicadaError
                try:
                    biblio.playlists[idx_p] += biblio.canciones_solo[idx_c]
                    print(f"'{biblio.canciones_solo[idx_c].titulo}' añadida")
                except CancionDuplicadaError as e:
                    print(f"{e}")

            except (IndexError, ValueError) as e:
                print(f" Índice inválido: {e}")
            except Exception as e:
                print(f"Error al añadir canción: {e}")

        elif opcion == "3":
            # Ver contenido de playlists
            if not biblio.playlists:
                print("No hay playlists creadas")
                continue
            try:
                for i, p in enumerate(biblio.playlists):
                    print(f"{i}.{p.nombre} ({len(p.canciones)} canciones)")
                idx = pedir_entero("Selecciona playlist para ver (o -1 para volver):", -1, len(biblio.playlists)-1)
                if idx == -1 or idx is None:
                    continue
                playlist = biblio.playlists[idx]
                print(f"\n--- {playlist.nombre} ---")
                if not playlist.canciones:
                    print("(vacía)")
                else:
                    for c in playlist.canciones:
                        print(f" {c.titulo} - {c.artista_principal.nombre} ({c.duracion_seg}s)")
            except IndexError:
                print("Índice de playlist fuera de rango")
            except Exception as e:
                print(f"Error al mostrar playlist: {e}")


        elif opcion == "4": #Fusionar playlists
            try:
                if len(biblio.playlists) < 2:
                    print("Necesitas al menos 2 playlists para fusionar")
                    continue
                print("\n--- Playlists disponibles ---")
                for i, p in enumerate(biblio.playlists):
                    print(f"{i}. {p.nombre} ({len(p.canciones)} canciones)")
                i1=pedir_entero("Índice Playlist 1: ",0,len(biblio.playlists)-1)
                if i1 is None:
                    continue
                i2=pedir_entero("Índice Playlist 2: ",0,len(biblio.playlists)-1)
                if i2 is None:
                    continue
                if i1 == i2:
                    print("Selecciona dos playlists diferentes")
                    continue

                fusion=biblio.playlists[i1]+biblio.playlists[i2]
                biblio.playlists.append(fusion)
                print(f" Fusión creada: '{fusion.nombre}' ({len(fusion.canciones)} canciones)")

            except (IndexError, ValueError) as e:
                print(f"Índice inválido: {e}")
            except Exception as e:
                print(f"Error al fusionar playlists: {e}")

        elif opcion == "5":
            continuar=False


def menu_usuarios(biblio):
    #Menú para crear usuarios (Gratis/Premium) y guardar playlists.
    continuar = True
    while continuar:
        print("\n" + "=" * 50)
        print("1. Gratis  2. Premium  3. Ver  4. Guardar playlist  5. Stats 6. Volver")
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

            print(f"\n--- Estadísticas de {usuario.nombre_usuario} ---")
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
        print("=" * 60)
        print("5. Playlist += Canción (Añadir rápido)")
        print("6. Ordenar Canciones por Duración (<,>)")
        print("7. Fusionar Playlist (Operador +)")
        print("8. Canción más larga de un álbum (usando >)")
        print("-" * 60)
        print("9. Volver")
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
            if not biblio.playlists or not biblio.canciones_solo:
                print("Necesitas al menos 1 playlist y 1 canción")
                continue
            print("\n--- Playlists disponibles ---")
            for i,p in enumerate(biblio.playlists):
                print(f"{i}. {p.nombre} ({len(p.canciones)} canciones")
            idx_p = pedir_entero("Playlist: ",0,len(biblio.playlists)-1)
            print("\n--- Canciones dispoibles ---")
            for i,c in enumerate(biblio.canciones_solo):
                print(f"{i}. {c.titulo}")
            idx_c = pedir_entero("Canción: ",0,len(biblio.canciones_solo)-1)

            biblio.playlists[idx_p] += biblio.canciones_solo[idx_c]
            print(f"'{biblio.canciones_solo[idx_c].titulo}' añadida con +=")

        elif opcion == "6":
            todas=biblio.canciones_solo + biblio.canciones_colab
            if not todas:
                print("No hay canciones registradas")
                continue
            print("\n1. Menor a mayor 2. Mayor a menor")
            orden=input("Opción:") == "2"
            print("\n--- Canciones ordenadas por duración (usando < y >) ---")
            for c in sorted(todas,reverse=orden):
                print(f" {c.duracion_seg}s - {c.titulo}")

        elif opcion == "7":
            if len(biblio.playlists) < 2:
                print("Necesitas al menos 2 playlists")
                continue
            print("\n--- Playlists disponibles ---")
            for i, p in enumerate(biblio.playlists):
                print(f"{i}. {p.nombre} ({len(p.canciones)} canciones)")
            i1=pedir_entero("Índice Playlist 1: ",0,len(biblio.playlist)-1)
            i2=pedir_entero("Índice Playlist 2: ",0,len(biblio.playlist)-1)
            if i1 == i2:
                print("Selecciona dos playlists diferentes")
                continue
            fusion = biblio.playlists[i1] + biblio.playlists[i2]
            biblio.playlists.append(fusion)
            print(f"Fusión creada: '{fusion.nombre}' ({len(fusion.canciones)} canciones)")

        elif opcion == "8":
            if not biblio.albumes:
                print(" No hay álbumes registrados")
                continue
            print("\n--- Álbumes disponibles ---")
            for i, alb in enumerate(biblio.albumes):
                print(f"{i}. {alb.titulo_album} - {alb.artista.nombre}")
            idx=pedir_entero("Selecciona álbum: ", 0, len(biblio.albumes)-1)

            try:
                mas_larga=biblio.albumes[idx].cancion_mas_larga()
                if mas_larga:
                    print(f"\n>>> Canción más larga; '{mas_larga.titulo}' ({mas_larga.duracion_seg}s)")
                else:
                    print("El álbum no tiene canciones")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "9":
            continuar = False
        else:
            print("Opción no válida")


def menu_adicionales():
    #Menú para probar clases adicionales.
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

    #Inicializamos directorios
    directorios=inicializar_directorios()

    biblio = BibliotecaMusical()
    biblio.cargar_binario(directorio=directorios['data/binarios'])
    BibliotecaMusical.guardar_log_actividad("Aplicación iniciada")

    continuar = True
    while continuar:
        print("\n" + "=" * 60)
        print("1. Artistas  2. Canciones  3. Álbumes  4. Playlists")
        print("5. Usuarios  6. Reproducir  7. Stats    8. Extra")
        print("9. SOBRECARGA MATEMÁTICA  0. Salir") # Nueva opción 9
        print("=" * 60)

        opcion = input("\nOpción: ")

        if opcion == "1":
            menu_artistas(biblio)
        elif opcion == "2":
            menu_canciones(biblio)
        elif opcion == "3":
            menu_albumes(biblio)
            # Nota: Implementar lógica de álbumes aquí o llamar a tu función
            pass
        elif opcion == "4":
            menu_playlists(biblio)
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
            biblio.guardar_binario(directorio=directorios['data/binarios'])
            biblio.guardar_datos()
            biblio.exportar_a_texto(directorio=directorios['data/texto'])
            BibliotecaMusical.guardar_log_actividad("Cierre correcto")
            continuar = False
            print("\n ¡Gracias!")
        else:
            print(" Opción no válida")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    main()