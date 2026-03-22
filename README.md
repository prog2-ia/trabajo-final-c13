[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)
# 🎵 Spotify Clon - Biblioteca Musical
Este proyecto fue desarrollado por Alejandro Navarro y Carla Carreras para la asignatura Programación II de la Universidad de Alicante, curso 2025-2026, bajo la supervisión del profesor Miguel Ángel Teruel Martínez en la parte de teoría y del profesor Matías Díaz Tornero en la parte de prácticas. El código fuente completo está disponible en el repositorio de GitHub del equipo, junto con este archivo de documentación y el archivo de requisitos del proyecto. Cabe aclarar que existen carpetas con archivos de clases que no hemos usado en la ejecución del proyecto por falta de tiempo pero pensamos añadirlas antes de la entrega del trabajo al final del cuatrimestre.
## Propósito del Proyecto

Este proyecto es una simulación de una plataforma de streaming musical similar a Spotify, desarrollada como trabajo final de la asignatura Programación II. El objetivo principal es demostrar la aplicación práctica de los conceptos de Programación Orientada a Objetos aprendidos durante el curso, incluyendo herencia, polimorfismo, encapsulamiento, clases abstractas y herencia múltiple con mixins.

El sistema permite a los usuarios gestionar una biblioteca musical completa, donde pueden registrar artistas (tanto solistas como bandas), crear canciones (individuales o colaboraciones), organizar álbumes y playlists, y gestionar diferentes tipos de cuentas de usuario con funcionalidades diferenciadas. Además, el proyecto integra funcionalidades adicionales como gestión de dispositivos de reproducción, sistema de suscripciones, podcasts, anuncios y géneros musicales.

Desarrollado por: Alejandro Navarro y Carla Carreras

---

## Instalación

Para ejecutar este proyecto necesitarás tener instalado Python 3.8 o una versión superior en tu ordenador. No es necesario instalar ningún paquete externo, ya que el proyecto utiliza exclusivamente la biblioteca estándar de Python, principalmente los módulos abc para clases abstractas y datetime para manejo de fechas.

Los pasos para poner en marcha el proyecto son sencillos. Primero, descarga o clona el repositorio en tu ordenador usando el comando git clone seguido de la URL del repositorio. Una vez tengas todos los archivos en tu máquina, abre una terminal o consola de comandos y navega hasta la carpeta del proyecto donde se encuentra el archivo ejecucion_proyecto_final.py.

Si lo deseas, puedes crear un entorno virtual para aislar las dependencias del proyecto, aunque al no requerir paquetes externos este paso es completamente opcional. Para ello, ejecuta el comando python -m venv venv y activa el entorno con venv\Scripts\activate en Windows o source venv/bin/activate en Linux y Mac. El archivo requirements.txt está incluido por convención y para cumplir con los estándares de proyectos Python, pero no es necesario ejecutar pip install ya que no hay dependencias externas que instalar.

---

## Uso del Programa

Para iniciar la aplicación, simplemente ejecuta el comando python ejecucion_proyecto_final.py desde la terminal ubicada en la carpeta del proyecto. Al arrancar, se mostrará un menú principal con ocho opciones numeradas que te permitirán navegar por todas las funcionalidades del sistema de manera intuitiva.

El flujo de trabajo recomendado comienza registrando al menos un artista en la opción 1, ya que este dato es requerido para poder crear canciones posteriormente. En esta sección puedes elegir entre registrar un artista solista, introduciendo nombre, país, edad y año de debut, o una banda, donde además se especifica el número de miembros y el año de formación. Una vez tengas artistas registrados, puedes proceder a crear canciones en la opción 2, donde podrás elegir entre canciones solo de un artista o colaboraciones entre múltiples artistas.

Las opciones 3 y 4 te permiten organizar ese contenido en álbumes y playlists respectivamente. En la sección de álbumes puedes crear nuevos discos y añadirles canciones, mientras que en playlists puedes crear listas de reproducción personalizadas y añadirles las canciones que desees reproducir juntas. La opción 5 es para crear usuarios, donde podrás elegir entre cuenta Gratis con calidad estándar y 6 saltos máximos, o cuenta Premium con calidad Hi-Fi, saltos ilimitados y descuento del 20% en suscripciones.

La opción 6 es la reproducción de playlists, donde podrás seleccionar un usuario y una playlist para escuchar las canciones en orden, con la posibilidad de saltar pistas según el tipo de cuenta. Durante la reproducción, el programa te mostrará cada canción una por una, permitiéndote elegir entre escucharla completa o saltarla a la siguiente. La opción 7 muestra estadísticas globales del sistema, incluyendo el total de artistas, canciones, álbumes, playlists, usuarios y reproducciones acumuladas.

La opción 8 permite probar clases adicionales que complementan el sistema. En esta sección puedes gestionar dispositivos de reproducción ajustando el volumen y verificando compatibilidad, crear suscripciones con diferentes planes y descuentos, registrar podcasts con sus capítulos, configurar anuncios patrocinados, y gestionar géneros musicales con sus artistas asociados. Cada una de estas funcionalidades demuestra conceptos avanzados de POO como herencia múltiple, mixins, métodos estáticos y de clase.

---

## Ejemplos de Uso

A continuación se muestra un ejemplo típico de interacción con el programa para que puedas familiarizarte con su funcionamiento. Al iniciar el programa por primera vez, selecciona la opción 1 para registrar un artista. El programa te preguntará si deseas registrar un solista o una banda. Para un solista, introduce el nombre artístico, país de origen, edad actual y año de debut profesional. Por ejemplo, puedes registrar a Bad Bunny de Puerto Rico con 29 años de edad y debut en 2016. El programa confirmará el registro mostrando un mensaje de éxito.

Luego ve a la opción 2 para crear una canción. Selecciona el artista que acabas de registrar de la lista desplegable, introduce el título de la canción, la duración en segundos y el género musical. El programa confirmará el registro mostrando el nombre de la canción y el artista principal. Si deseas crear una colaboración, selecciona la opción de colaboración, elige el artista principal y luego podrás seleccionar múltiples artistas secundarios de la lista hasta que indiques que has terminado.

Para crear una playlist, ve a la opción 4, dale un nombre como Fiesta Latina o Música para Estudiar, y luego añade las canciones que desees. Puedes añadir tantas canciones como quieras antes de volver al menú principal. Cada vez que añadas una canción, el programa te pedirá que selecciones la playlist y la canción de listas desplegables que muestran las opciones disponibles.

Finalmente, en la opción 6 podrás reproducir esa playlist. Selecciona un usuario previamente creado y la playlist que deseas escuchar. El programa te mostrará cada canción una por una, permitiéndote elegir entre escucharla completa, lo que incrementará el contador de reproducciones, o saltarla, lo que consumirá uno de tus saltos disponibles. Si el usuario es Gratis, tendrás un límite de 6 saltos por sesión. Si es Premium, los saltos son ilimitados y verás el mensaje Saltos: Ilimitados en pantalla.

En la opción 8 puedes probar las clases adicionales. Por ejemplo, en Dispositivo puedes crear un nuevo dispositivo como Altavoz Bluetooth y ajustar el volumen entre 0 y 100. En Suscripción puedes crear planes especiales como el plan Estudiante con descuento, y aplicar descuentos adicionales al precio base. En Podcast puedes registrar nuevos programas con su anfitrión y número de capítulos, y reproducir el podcast. En Anuncio puedes configurar publicidad patrocinada con duración máxima de 30 segundos para cuentas estándar.

---

## Estructura de Archivos

El proyecto está organizado en múltiples carpetas con archivos Python. Cada carpeta contiene las clases correspondientes a cada función del sistema. Para las funciones de tipo Playlist y Album, hemos dejado el archivo individual(sin meter en ninguna carpeta), al igual que hemos hecho con el fichero de ejecución. Las clases principales incluyen Artista como clase base abstracta, con ArtistaSolista y ArtistaBanda como subclases que implementan los métodos abstractos tipo y anyos_carrera. De manera similar, Cancion es la clase base abstracta para CancionSolo y CancionColaboracion, cada una con su propia implementación de info y get_numero_artista.

La clase Usuario sirve como base para UsuarioGratis y UsuarioPremium, siendo esta última un ejemplo de herencia múltiple que combina Usuario con los mixins BeneficiosPremium y Notificaciones para añadir funcionalidad sin duplicar código. Las clases adicionales incluyen Dispositivo para gestión de hardware de reproducción, Suscripcion para planes de pago, Podcast para contenido hablado, Anuncio para publicidad, y Genero con ArtistaTrap para demostrar herencia múltiple compleja.

El archivo ejecucion_proyecto_final.py contiene el menú interactivo principal y coordina todas las clases del sistema mediante la clase BibliotecaMusical, que encapsula todas las colecciones de objetos evitando el uso de variables globales. Los archivos requirements.txt y README.md completan la documentación del proyecto para facilitar su instalación y uso por otros desarrolladores.

---

## Conceptos de Programación Orientada a Objetos

Este proyecto implementa los principales conceptos de POO vistos en clase de manera integral y coherente. El encapsulamiento se demuestra mediante el uso sistemático de atributos privados con doble guión bajo en todas las clases, obligando a usar properties con getters y setters para su acceso y modificación, lo que permite validar datos antes de asignarlos y proteger la integridad del estado interno de los objetos.

La herencia está presente en toda la jerarquía de clases, desde Artista hasta sus subclases específicas ArtistaSolista y ArtistaBanda, y desde Cancion hasta CancionSolo y CancionColaboracion. Cada subclase extiende la funcionalidad de su clase padre añadiendo atributos y métodos específicos mientras reutiliza el código común. El polimorfismo se evidencia en métodos como tipo e info, que tienen implementaciones diferentes según la clase concreta, permitiendo que el mismo código funcione con diferentes tipos de objetos.

Las clases abstractas Artista y Cancion definen métodos abstractos con el decorador @abstractmethod que deben ser implementados obligatoriamente por sus subclases, garantizando que todas las clases hijas tengan una interfaz común. La herencia múltiple se muestra en UsuarioPremium, que combina funcionalidad de tres clases diferentes mediante mixins, y en ArtistaTrap, que hereda simultáneamente de Musico e Influencer. Los mixins BeneficiosPremium y Notificaciones demuestran cómo añadir funcionalidad compartida sin crear jerarquías de herencia profundas.

El proyecto también incluye métodos de clase con @classmethod para acceder a variables de clase como los contadores globales, métodos estáticos con @staticmethod para funciones utilitarias que no necesitan acceso a la instancia, y el uso correcto de super con kwargs para asegurar la inicialización cooperativa en jerarquías de herencia múltiple complejas.
