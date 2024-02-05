# Proyecto Pygame Robot 8bit 
Este repositorio contiene un juego desarrollado en Python con la biblioteca Pygame, llamado "Robot Adventure". En este juego, controlarás a un robot que debe explorar un mapa lleno de obstáculos y desafíos.

## Características del Proyecto

*Vida del Jugador*:

- El jugador comienza la partida con 10 puntos de vida.
  
*Colisión con Muros*:

- El jugador no puede atravesar muros. Si choca con un muro, se le restará un punto de vida.

*Zona de Agua*:

- El jugador no puede atravesar una zona de agua sin un amuleto.
- Al entrar en el agua sin el amuleto, se restarán 3 puntos de vida por cada movimiento.

*Bombas*:

- El jugador puede encontrar bombas en el mapa.
- Puede utilizar las bombas para romper muros adyacentes.
- Las bombas explotarán en cadena si hay otra bomba en la posición adyacente.
- Las bombas no afectan al agua ni a los diamantes, pero hacen desaparecer el amuleto si no se ha recogido y está en una posición adyacente.

*Pociones de Curación*:

- A lo largo del mapa, el jugador puede encontrar pociones de curación.
- Las pociones aumentarán entre 5 puntos de vida.

## Estructura del Código

*Clase Game*:

- Inicia el juego, carga los recursos necesarios y gestiona la lógica del juego.
- Maneja la creación del mapa, la posición de los ítems y los eventos.
- Muestra la pantalla de introducción, la pantalla principal del juego y la pantalla de fin de partida.

*Clase Player*:

- Representa al personaje controlado por el jugador.
- Gestiona la salud, los diamantes recogidos, las bombas disponibles y si porta o no el amuleto.
  
*Clases Items*:

- Bomb, Potion, Diamond y Amulet, representan los diferentes elementos del juego.
- Cada item tiene un rol de utilidad para el jugador.
  
*Inicio del Juego:*

Al ejecutar el juego, se mostrará una pantalla de introducción.
Haz clic en el botón "PLAY" para comenzar el juego.

*Controles*:

- Utiliza las teclas de dirección para mover al robot.
- Presiona "Q" o "ESC" para mostrar un mensaje de confirmación de salida.
  
*Objetivos*:

- Recoge diamantes para aumentar tu puntuación.
- Utiliza bombas estratégicamente para abrir caminos.
- Encuentra y utiliza el traje acuático para atravesar zonas de agua.
  
*Fin del Juego*:

- El juego termina cuando el robot se queda sin vida.

*Requisitos del Sistema*:
Asegúrate de tener instalado Python y Pygame para ejecutar este juego. Puedes instalar Pygame utilizando el siguiente comando:

- pip install pygame
