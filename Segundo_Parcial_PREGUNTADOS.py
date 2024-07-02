import pygame   
from pygame.locals import *
from datos import lista
from biblioteca_preguntados import *

''' Desafío:
A. Analizar detenidamente el set de datos (puede agregarle más preguntas si así
lo desea).

B. Crear una pantalla de inicio, con 3 (tres) botones, “Jugar”, “Ver Puntajes”,
“Salir”, la misma deberá tener alguna imagen cubriendo completamente el
fondo y tener un sonido de fondo. Al apretar el botón jugar se iniciará el juego.
Opcional: Agregar un botón para activar/desactivar el sonido de fondo.

C. Crear 2 botones uno con la etiqueta “Pregunta”, otro con la etiqueta “Reiniciar”

D. Imprimir el Puntaje: 000 donde se va a ir acumulando el puntaje de las
respuestas correctas. Cada respuesta correcta suma 10 puntos.

E. Al hacer clic en el botón “Pregunta” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic en este botón pasa a la siguiente
pregunta.

F. Al hacer clic en una de las tres palabras que representa una de las tres
opciones, si es correcta, debe sumar el puntaje, reproducir un sonido de
respuesta correcta y dejar de mostrar las otras opciones.

G. Solo tiene 2 intentos para acertar la respuesta correcta y sumar puntos, si
agotó ambos intentos, deja de mostrar las opciones y no suma puntos. Al
elegir una respuesta incorrecta se reproducirá un sonido indicando el error y
se ocultará esa opción, obligando al usuario a elegir una de las dos restantes.

H. Al hacer clic en el botón “Reiniciar” debe mostrar las preguntas comenzando
por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el puntaje.

I. Una vez terminado el juego se deberá pedirle el nombre al usuario, guardar
ese nombre con su puntaje en un archivo, y volver a la pantalla de inicio.

J. Al ingresar a la pantalla “Ver Puntajes”, se deberá mostrar los 3 (tres) mejores
puntajes ordenados de mayor a menor, junto con sus nombres de usuario
correspondientes. Debe haber un botón para volver al menú principal.

NOTAS:
- Tienen total libertad para utilizar los sonidos, imágenes, y animaciones
(opcional) alusivas, donde corresponda.
- El formato del archivo que se debe crear para guardar los puntajes
debe ser TXT, CSV o JSON.
- Se deben definir y utilizar funciones, y las mismas deben estar
documentadas e importadas desde otro archivo (biblioteca).
'''

pygame.init()

' Pantalla '
config_pantalla = [1600, 900]
pygame.display.set_caption("PREGUNTADOVICH")
screen = pygame.display.set_mode(config_pantalla)

' Imagenes '

imagen_fondo = pygame.image.load('ProyectoGAME/background.png')
imagen_fondo = pygame.transform.scale(imagen_fondo, (1600, 900))
logo = pygame.image.load('ProyectoGAME/logito.png')
logo = pygame.transform.scale(logo, (200, 200))
titulo = pygame.image.load('ProyectoGAME/PREGUNTADOUSH.png')
titulo = pygame.transform.scale(titulo, (780, 120))
sound_on = pygame.image.load('ProyectoGAME/soundon.png')
sound_on = pygame.transform.scale(sound_on, (100, 100))
sound_off = pygame.image.load('ProyectoGAME/soundoff.png')
sound_off = pygame.transform.scale(sound_off, (100, 100))
boton_jugar_text = pygame.image.load('ProyectoGAME/BOTON JUGAR.png')
boton_jugar_text = pygame.transform.scale(boton_jugar_text, (200, 75))
boton_puntaje = pygame.image.load('ProyectoGAME/PUNTAJE.png')
boton_puntaje = pygame.transform.scale(boton_puntaje, (250, 75))
boton_salir = pygame.image.load('ProyectoGAME/SALIR.png')
boton_salir = pygame.transform.scale(boton_salir, (210, 65))
fondo_jugar = pygame.image.load('ProyectoGAME/preguntados_fondo_jugar.jpg')
fondo_jugar = pygame.transform.scale(fondo_jugar, (1600, 900))
fondo_ranking = pygame.image.load('ProyectoGAME/fondo_ranking.jpg')
fondo_ranking = pygame.transform.scale(fondo_ranking, (1600, 900))


' Botones '
boton_jugar = pygame.Rect(700, 300, 200, 75)
hitbox_puntaje = pygame.Rect(670, 450, 250, 75)
hitbox_salir = pygame.Rect(685, 600, 200, 65)
boton_mute = pygame.Rect(30, 0, 100, 100)
cambiar_pregunta_hitbox = pygame.Rect(700, 100, 800, 100)
respuesta_a = pygame.Rect(300, 700, 300, 75)
respuesta_b = pygame.Rect(750, 700, 300, 75)
respuesta_c = pygame.Rect(1200, 700, 300, 75)
boton_reiniciar = pygame.Rect(100, 300, 300, 75)

' Textos '
font = pygame.font.SysFont("Arial Narrow", 50)
font2 = pygame.font.SysFont("Arial Narrow", 100)
text = font.render("Cambiar pregunta", True, (255, 255, 255))
puntaje = 0
txt_puntaje = font.render(f"Puntaje: {str(puntaje)}", False, (255, 255, 255))
mi_texto = ""
cambiar_pregunta_txt = font.render("Cambiar pregunta", True, (255, 255, 255))
pedido_nombre = font2.render("INGRESE SU NOMBRE:", True, (255, 255, 255))




' Sonidos '
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
musica_menu = pygame.mixer.Sound('ProyectoGAME/musica menu.mp3')
musica_menu.set_volume(0.3)
musica_jugar = pygame.mixer.Sound('ProyectoGAME/musica_jugar.mp3')
musica_jugar.set_volume(0.3)
sonido_correcto = pygame.mixer.Sound('ProyectoGAME/Sonido_correcto.mp3')
sonido_correcto.set_volume(0.5)
sonido_incorrecto = pygame.mixer.Sound('ProyectoGAME/sonido_incorrecto.mp3')
sonido_incorrecto.set_volume(0.5)
musica_ranking = pygame.mixer.Sound('ProyectoGAME/musica_ranking.mp3')
musica_ranking.set_volume(0.5)

' Variables '

mostrar_score = False
# ' Se crea una variable para cargar los datos del scoreboard.json '
scoreboard = scoreboard_carga_datos()
nombre_registrado = ""
contador_puntaje = 0
vidas = 2
indice_pregunta = 0
ver_puntaje = False
musica_jugar_on = False
musica_menu_on = True
musica_ranking_on = False
esta_jugando = False
musica_on = False
running = True

# ' Bucle del juego '
while running:
#  ' Eventos del juego '
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
           running = False

#        ' Evento por dónde se hace click '
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ver_puntaje == False:
                if esta_jugando == False:
                    if hitbox_puntaje.collidepoint(event.pos):
                        ver_puntaje = True
                    if hitbox_salir.collidepoint(event.pos):
                        running = False
                    if boton_jugar.collidepoint(event.pos):
                        esta_jugando = True

                    if boton_mute.collidepoint(event.pos):
                        if musica_menu_on == True:
                            mute = screen.blit(sound_on, (30, 0))
                            musica_menu_on = False
                            musica_menu.play(-1)
                        else: 
                            mute = screen.blit(sound_off, (30, 0))
                            musica_menu_on = True
                            musica_menu.stop()
                else: 
                    respuesta_jugador = ""
                    if respuesta_a.collidepoint(event.pos):
                        respuesta_jugador = 'a'
                    if respuesta_b.collidepoint(event.pos):
                        respuesta_jugador = 'b'
                    if respuesta_c.collidepoint(event.pos):
                        respuesta_jugador = 'c'
                    
                    if respuesta_jugador != "":
                        if respuesta_jugador == lista[indice_pregunta]['correcta']:
                            sonido_correcto.play(0)
                            puntaje += 10
                            indice_pregunta += 1
                        else: 
                            vidas -= 1
                            sonido_incorrecto.play(0)
                    if boton_reiniciar.collidepoint(event.pos):
                        indice_pregunta += 1
                        puntaje = 0

#        ' Evento para registrar teclas y escribir / Registrar el nombre con ENTER / Borrar último caracter con BACKSPACE '
        if event.type == pygame.TEXTINPUT:
            nombre_registrado_x_tecla = event.text
            nombre_registrado += nombre_registrado_x_tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # ' Se crea la función para borrar el último caracter ingresado en nombre_registrado utilizando el BACKSPACE '
                nombre_registrado = borrar_ultimo_caracter(nombre_registrado) 
            if event.key == pygame.K_RETURN:
                mostrar_score = True
                datos_x_jugador = {"nombre": nombre_registrado, "puntaje": puntaje}     
                print(scoreboard)
                scoreboard['top_mejores'].append(datos_x_jugador)     
                # ' Se utiliza la función para guardar los datos a la variable del scoreboard, la cuál tiene .json ' 
                scoreboard_guardar_datos(scoreboard)

#    ' MENU '                       
    if esta_jugando == False:
        screen.blit(sound_off, (0, 0))
        screen.blit(sound_on, (0, 0))
        screen.blit(imagen_fondo, (0, 0))
        screen.blit(logo, (300, 50))
        screen.blit(titulo, (500, 100))
        screen.blit(boton_jugar_text, (700, 300))
        screen.blit(boton_puntaje, (670, 450))
        screen.blit(boton_salir, (700, 600))

        if musica_menu_on == True:
            screen.blit(sound_on, (30, 0))
        elif musica_menu_on == False: 
            screen.blit(sound_off, (30, 0))

        if musica_on == False:
            musica_menu.play(-1)
            screen.blit(sound_on, (30, 0))
            musica_on = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(sound_off, (30, 0))
            musica_menu.stop()

#   ' PANTALLA AL JUGAR '
    elif esta_jugando == True:
        musica_menu.stop()
        if musica_jugar_on == False:
            musica_jugar.play(-1)
            musica_jugar_on = True
        txt_puntaje = font.render(f"Puntaje: {str(puntaje)}", False, (255, 255, 255))
        screen.blit(fondo_jugar, (0, 0))
        pygame.draw.rect(screen, (52, 63, 180), [700, 100, 800, 100])
        pygame.draw.rect(screen, (52, 63, 180), [300, 700, 300, 75])
        pygame.draw.rect(screen, (52, 63, 180), [750, 700, 300, 75])
        pygame.draw.rect(screen, (52, 63, 180), [1200, 700, 300, 75])
        pygame.draw.rect(screen, (52, 63, 180), [50, 300, 500, 100])
        pygame.draw.rect(screen, (52, 63, 180), [50, 100, 500, 75])

        
        if indice_pregunta >= 0 and indice_pregunta < len(lista):
            screen.blit(font.render(lista[indice_pregunta]['pregunta'], False, (255, 255, 255)), (730, 150))
            screen.blit(font.render(f"A-{lista[indice_pregunta]['a']}", False, (255, 255, 255)), (310, 710))
            screen.blit(font.render(f"B-{lista[indice_pregunta]['b']}", False, (255, 255, 255)), (760, 710))
            screen.blit(font.render(f"C-{lista[indice_pregunta]['c']}", False, (255, 255, 255)), (1210, 710))
        #screen.blit(cambiar_pregunta_txt(50, 300))
        screen.blit(text, (150, 330))
        screen.blit(txt_puntaje, (200, 120))


    
    if indice_pregunta == len(lista) or vidas == 0:
        ver_puntaje = True
        screen.blit(fondo_ranking, (0, 0))
        pygame.draw.rect(screen, (52, 63, 180), [400, 750, 750, 100], border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), [400, 750, 750, 100], width=3, border_radius=10)
        musica_jugar.stop()
        if musica_ranking_on == False:
            musica_ranking.play(-1)
            musica_ranking_on = True

    if ver_puntaje == True:
        if mostrar_score == True:
            screen.blit(fondo_ranking, (0, 0))
        screen.blit(fondo_ranking, (0, 0))
        musica_jugar.stop()
        if musica_ranking_on == False:
            musica_ranking.play(-1)
            musica_ranking_on = True

        if mostrar_score == True:
            acumulador_y = 0
            pygame.draw.rect(screen, (255, 197, 36), [350, 90, 1050, 100], border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), [350, 90 + 150, 1050, 100], width=3, border_radius=10)
            pygame.draw.rect(screen, (171, 171, 171), [350, 90 + 150, 1050, 100], border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), [350, 90 + 150, 1050, 100], width=3, border_radius=10)
            pygame.draw.rect(screen, (171, 83, 0), [350, 90 + 300, 1050, 100], border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), [350, 90 + 300, 1050, 100], width=3, border_radius=10)
            for dato_jugador in scoreboard["top_mejores"]:
                # ' Se crea una función para realizar el Bubble Sort, y ordenar los puntajes de mayor a menor '
                bubble_sort_puntaje(scoreboard['top_mejores'])
                dato_jugador_render = font2.render(f"{acumulador_y + 1} - {dato_jugador['nombre']:5}: {dato_jugador['puntaje']}", True, (255, 255, 255))
                if acumulador_y < 3:
                    screen.blit(dato_jugador_render, (500, 100 + (acumulador_y * 150)))
                acumulador_y += 1
        else:
            screen.blit(pedido_nombre, (400, 200))
            nombre_registrado_render = font2.render(nombre_registrado, True, (255, 255, 255))
            screen.blit(nombre_registrado_render, (450, 760))
        

    pygame.display.flip()

pygame.quit()
