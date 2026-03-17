from clase_Cancion import Cancion
from clase_Playlist import Playlist
from clase_Usuario import Usuario

from clase_Genero import Genero
from clase_Album import Album
from clase_Artista import Artista


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


from clase_Genero import Genero, ArtistaTrap
from clase_suscripcion import Suscripcion
from clase_anuncio import Anuncio
from clase_dispositivo import Dispositivo
from clase_podcast import Podcast

def main():
    print("PRUEBA DE LA LIBRERÍA MUSICAL")

    # Probar Clase Dispositivo (Encapsulamiento y Setters)
    pc = Dispositivo(nombre="PC Salón", tipo="Ordenador")
    print(pc)
    pc.subir_volumen(60) 
    pc.subir_volumen(10)  
    
    # Probar Clase Suscripcion (Método de Clase y Abstracción)
    sub = Suscripcion.crear_plan_estudiante()
    sub.aplicar_descuento(10) # Prueba del método abstracto implementado
    print(sub)

    # Probar Clase Genero y ArtistaTrap (Herencia Múltiple y Polimorfismo)
    trap = Genero("Trap", capacidad_maxima=2)
    bad_bunny = ArtistaTrap(
        nombre="Bad Bunny", 
        instrumento="Voz", 
        seguidores=45000000, 
        red_social="Instagram", 
        estilo="Latino"
    )
    trap.registrar_artista(bad_bunny)
    print(trap)

    # Probar Clase Podcast (MRO y Herencia Múltiple)
    mi_podcast = Podcast(titulo="Charlando Tranquilamente", anfitrion="Ibai", capitulos=15)
    mi_podcast.reproducir()
    mi_podcast.reproducir_capitulo(1)
    print(mi_podcast)

    # Probar Clase Anuncio (ABC y Estáticos)
    spoty_ad = Anuncio(patrocinador="Coca-Cola", duracion=20)
    print(spoty_ad)
    spoty_ad.reproducir()
    print(Anuncio.normativa_publicidad()) # Llamada a método estático

    print("\n--- ✅ PRUEBA FINALIZADA CON ÉXITO ---")
    print(f"Total artistas registrados en el sistema: {Genero.obtener_total_global()}")

if __name__ == "__main__":
    main()