# CLASE: Playlist | IMPORT TARDÍO: Evita importación circular con Usuario

class Playlist:
    #Contenedor de canciones. Gestiona reproducción interactiva.

    def __init__(self, nombre):
        #Inicializa playlist con nombre y lista vacía de canciones.
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        #Añade una canción a la playlist.
        self.canciones.append(cancion)

    def contar_canciones(self):
        #Muestra y retorna la cantidad de canciones en la playlist.
        print(f"Playlist '{self.nombre}': {len(self.canciones)} canciones")
        return len(self.canciones)

    def mostrar_canciones(self):
        #Muestra las canciones de la playlist.
        if not self.canciones:
            print(f"Playlist '{self.nombre}' vacía")
        else:
            print(f"--- {self.nombre} ---")
            for c in self.canciones:
                print(f"{c.titulo} - {c.artista_principal.nombre}")

    def __str__(self):
        #Representación en texto de la playlist.
        return f"Playlist '{self.nombre}' ({len(self.canciones)} canciones)"

    def reproducir(self, usuario):

        #Reproducción interactiva (escuchar/saltar/salir).

        #IMPORT TARDÍO (dentro del método): Evita circular import.
        #Usuario importa Playlist y Playlist importa Usuario , eso nos da un error circular.
        #Solución: Importar UsuarioGratis solo cuando se llama al método.

        from usuarios.clase_UsuarioGratis import UsuarioGratis

        if not self.canciones:
            print(f" Playlist '{self.nombre}' vacía")
            return

        print(f"\n REPRODUCIENDO: {self.nombre}")
        print(f" Usuario: {usuario.nombre_usuario}")

        continuar = True
        indice = 0

        while continuar and indice < len(self.canciones):
            cancion = self.canciones[indice]
            print(f"\n--- {indice + 1}/{len(self.canciones)}: {cancion.titulo} ---")

            # Muestra saltos disponibles (Ilimitados para Premium)
            if usuario.saltos_maximos == float('inf'):
                print(f"Saltos: Ilimitados")
            else:
                disponibles = usuario.saltos_maximos - usuario.saltos_actuales
                print(f"Saltos: {disponibles}")

            print("1. Escuchar  2. Saltar  3. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                usuario.escuchar_cancion(cancion)  # Cuenta como reproducción
                indice += 1
            elif opcion == "2":
                if usuario.avanzar_cancion(cancion, self):  # Gasta salto
                    indice += 1
                elif isinstance(usuario, UsuarioGratis):
                    # Gratis puede ver anuncio para recargar
                    if input("¿Ver anuncio? (s/n): ") == "s":
                        usuario.ver_anuncio()
                        usuario.recargar_saltos(2)
                        indice += 1
                    else:
                        continuar = False
                else:
                    continuar = False
            elif opcion == "3":
                continuar = False
            else:
                print(" Opción no válida")

        if indice >= len(self.canciones):
            print("\n Playlist completada")