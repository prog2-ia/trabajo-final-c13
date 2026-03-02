from proyecto_final import Cancion,Album,Artista,Playlist,Usuario

cancion1=Cancion('FULL ICE','YSY A',157,'Trap')
cancion2=Cancion('Callaita','Bad Bunny',190,'Reggaeton')
cancion3=Cancion('Moscow Mule','Bad Bunny',210,'Reggaeton')
cancion4=Cancion('Till I Collapse','Eminem',204,'Rap')
cancion5=Cancion('Uzbekistán','YSY A',185,'Trap')
cancion6=Cancion('Fan De Tus Batallas','YSY A',194,'House')
cancion7=Cancion('Como Tiene Que Ser','YSY A',198,'Trap')
cancion8=Cancion('Para Sacarmelo','YSY A',203,'Trap')

album1=Album('Un Verano Sin Ti','Bad Bunny',2022)
album2=Album('Saturación Pop','YSY A',2025)
album3=Album('Hecho A Mano','YSY A',2019)

artista1=Artista('Bad Bunny','Puerto Rico',29)
artista2=Artista('YSY A','Argentina',27)
artista3=Artista('Eminem','Estados Unidos',53)

playlist1=Playlist('Estudiar')
playlist2=Playlist('Días libres')

usuario1=Usuario('alex_11','Alejandro Navarro')
usuario2=Usuario('Valeriaa_29','Valeria Lake')

cancion1.repros()
cancion2.repros()
cancion1.repros()
cancion3.repros()
cancion1.repros()
cancion4.repros()
cancion4.repros()
cancion5.repros()
cancion6.repros()
cancion2.repros()
cancion7.repros()
cancion7.repros()
cancion7.repros()
cancion8.repros()

cancion7.numero_reproducciones()

album1.agrega_cancion(cancion2)
album1.agrega_cancion(cancion3)
album2.agrega_cancion(cancion5)
album2.agrega_cancion(cancion6)
album3.agrega_cancion(cancion1)
album3.agrega_cancion(cancion7)
album3.agrega_cancion(cancion8)

album1.numero_canciones_album()
album2.numero_canciones_album()
album3.numero_canciones_album()

album2.reproducir_album()
album2.reproducir_album()
album2.reproducir_album()
album3.reproducir_album()
album3.reproducir_album()
album1.reproducir_album()

artista1.agregar_album(album1)
artista2.agregar_album(album2)
artista2.agregar_album(album3)
artista3.agregar_canciones(cancion4)
artista1.numero_albumes()
artista1.total_canciones()
artista2.numero_albumes()
artista2.total_canciones()
artista3.numero_albumes()
artista3.total_canciones()

playlist1.agregar_cancion(cancion1)
playlist1.agregar_cancion(cancion4)
playlist1.agregar_cancion(cancion5)
playlist1.agregar_cancion(cancion6)
playlist1.agregar_cancion(cancion7)
playlist1.agregar_cancion(cancion8)
playlist2.agregar_cancion(cancion2)
playlist2.agregar_cancion(cancion3)
playlist2.agregar_cancion(cancion5)
playlist2.agregar_cancion(cancion6)

playlist1.contar_canciones()
playlist1.mostrar_canciones()
playlist2.contar_canciones()
playlist2.mostrar_canciones()

usuario1.guardar_playlist(playlist1)
usuario2.guardar_playlist(playlist1)
usuario2.guardar_playlist(playlist2)
usuario1.cantidad_playlists()
usuario2.cantidad_playlists()

print(album2)
print(artista1)
print(playlist1)


#prueba de la clase GÉNERO 
print("\n" + "="*40)
print("TEST DE LA CLASE GENERO (Lógica de Capacidad)")
print("="*40)

# 1. Creamos un Género con capacidad para 2 canciones 
# Esto cumple con definir atributos por el usuario
mi_genero = Genero("Trap", "Ritmos urbanos de Argentina", capacidad_maxima=2)

# 2. Intentamos añadir canciones
# Añadir la primera gasta 1 de capacidad
mi_genero.añadir_cancion_a_genero(cancion1) 

# Añadir la segunda deja el espacio a 0
mi_genero.añadir_cancion_a_genero(cancion5) 

# 3. Probamos el límite de capacidad 
# Intentamos añadir una tercera canción: debe saltar el mensaje de ERROR
print("\nIntentando añadir una tercera canción sin espacio...")
mi_genero.añadir_cancion_a_genero(cancion7)

# 4. Ampliar capacidad
print("\nAmpliando capacidad del género...")
mi_genero.ampliar_capacidad(3)

# 5. Ahora sí podemos añadir las canciones restantes
mi_genero.añadir_cancion_a_genero(cancion7)
mi_genero.añadir_cancion_a_genero(cancion8)

# 6. Comprobar el Atributo de Clase (Total global de canciones)
# Esto muestra cuántas canciones se han registrado en el sistema
print("\n" + "-"*30)
Genero.obtener_total_sistema()
print("-"*30)