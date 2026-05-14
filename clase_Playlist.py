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

    def __repr__(self):
        return f"Playlist(nombre='{self.nombre}', canciones={len(self.canciones)})"

    def __len__(self):
        return len(self.canciones)

    def __contains__(self,cancion):
        return cancion in self.canciones

    def __getitem__(self,indice):
        #Permite:p playlist[indice] con manejo de IndexError
        try:
            return self.canciones[indice]
        except IndexError:
            from excepciones import RecursoNoEncontradoError
            raise RecursoNoEncontradoError("canción en índice", indice)

    def __add__(self,otra):
        #Playlist + Playlist -> nueva playlist combinada
        from excepciones import RecursoNoEncontradoError
        if not isinstance(otra, Playlist):
            from excepciones import ValorInvalidoError
            raise ValorInvalidoError("playlist",type(otra).__name__,"debe ser un objeto Playlist")

        nueva = Playlist(f"{self.nombre} + {otra.nombre}")
        nueva.canciones = self.canciones.copy() + otra.canciones.copy()
        return nueva

    def __iadd__(self,cancion):
        from canciones.clase_Cancion import Cancion
        from excepciones import CancionDuplicadaError

        if not isinstance(cancion, Cancion):
            from excepciones import ValorInvalidoError
            raise ValorInvalidoError("canción",type(cancion).__name__,"debe ser un objeto Cancion")

        #Verificar duplicados
        for existente in self.canciones:
            if existente.titulo.lower() == cancion.titulo.lower():
                raise CancionDuplicadaError(cancion.titulo,f"la playlist '{self.nombre}'")

        self.canciones.append(cancion)
        return self

        #Evitamos duplicados con un bucle simple
        for existente in self.canciones:
            if existente.titulo.lower()==cancion.titulo.lower():
                return self #Ya existe,salimos

        self.canciones.append(cancion)
        return self #Obligatorio para que += funcione


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

        while continuar and indice < len(self):
            cancion = self[indice]
            print(f"\n--- {indice + 1}/{len(self)}: {cancion.titulo} ---")

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

        if indice >= len(self):
            print("\n Playlist completada")