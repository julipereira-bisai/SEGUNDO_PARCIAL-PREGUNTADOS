import pygame
import random
from pygame.locals import *



pygame.init() #Se inicializa pygame

config_pantalla = [500, 500]
pygame.display.set_caption("Mi super juego")

# Tiempos
tick = pygame.USEREVENT + 0
# 1000 milisegundos = 1 segundo
pygame.time.set_timer(tick, 10)

# Eje X -> Ancho de la pantalla
# Eje Y -> Alto de la pantalla
#                                  [x   ,   y]
screen = pygame.display.set_mode(config_pantalla) #Se crea una ventana

#rectangulo = [ubicacion_rectangulo, tamanio_rectangulo]
ubicacion_rectangulo = [225, 225]
tamanio_rectangulo = [50, 50]

#mi_rectangulo = pygame.Rect(225, 225, 50, 50)


#                    x     y 
ubicacion_circulo = [250, 250]
radio_circulo = 75
color_rectangulo = (29, 107, 224)
color_circulo = (224, 29, 224)
contador_tiempo = 0

red = 0
green = 0
blue = 0


# Imagenes
imagen_joystick = pygame.image.load("Programacion_I/Clase_15/joystick.png") # 512x512
imagen_joystick = pygame.transform.scale(imagen_joystick, (500, 500))



imagen_personaje = pygame.image.load("Programacion_I/Clase_15/personaje.jpg")
rect_personaje = imagen_personaje.get_rect()
rect_personaje.x = 225 
rect_personaje.y = 425
rect_personaje.w = 50 # Ancho del rectangulo del personaje
rect_personaje.h = 50 # Alto del rectangulo del personaje



imagen_roca = pygame.image.load("Programacion_I/Clase_15/roca.jpg")
rect_roca = imagen_roca.get_rect()
rect_roca.x = 450
rect_roca.y = 450



# Textos
font = pygame.font.SysFont("Arial Narrow", 50)
text = font.render("Puntaje:", True, (0, 255, 0))
puntaje = "0"
txt_puntaje = font.render(puntaje, False, (0, 255, 0))
mi_texto = ""


# Sonidos
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)


sonido_click = pygame.mixer.Sound("Programacion_I/Clase_15/test_sound.mp3")
sonido_click.set_volume(0.4)
#sonido_click.play()
#sonido_click.stop()


esta_jugando = False

running = True
while running: # Loop principal del juego
    pressed_keys = pygame.key.get_pressed()
    
   # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
           running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(f"Mouse down: {event.pos}")
            #print(rect_personaje.w)
            sonido_click.play()
            esta_jugando = True
            if rect_personaje.collidepoint(event.pos):
                print("Click sobre el personaje")

        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse up: {event.pos}")
            
        if event.type == pygame.KEYDOWN:
            mi_texto += event.unicode
            #print(mi_texto)

        if event.type == tick:
            if True in pressed_keys:
                if pressed_keys[K_d]:
                    rect_personaje.x += 1
                    #ubicacion_circulo[0] += 1
                    #if ubicacion_circulo[0] > config_pantalla[0] + radio_circulo:
                        #ubicacion_circulo[0] = 0 - radio_circulo
                if pressed_keys[K_a]:
                    rect_personaje.x -= 1
                    #ubicacion_circulo[0] -= 1
                    #if ubicacion_circulo[0] < 0 - radio_circulo:
                        #ubicacion_circulo[0] = config_pantalla[0] + radio_circulo
                if pressed_keys[K_w]:
                    rect_personaje.y -= 1

                    #ubicacion_circulo[1] -= 1
                if pressed_keys[K_s]:
                    rect_personaje.y += 1
                    #ubicacion_circulo[1] += 1
            
            contador_tiempo += 1
            #print(f"Ya pasaron {contador_tiempo} segundo")

            ubicacion_rectangulo[0] += 1
            if ubicacion_rectangulo[0] > config_pantalla[0]:
                ubicacion_rectangulo[0] = 0 - tamanio_rectangulo[0]
            #if ubicacion_rectangulo[0] > 0:
                #ubicacion_rectangulo[0] -= 1
                # ubicacion_rect[X] 

            if contador_tiempo == 100:
                color_circulo = (random.randint(0, 255), 0, random.randint(0, 255))
                contador_tiempo = 0

                # puntaje creciente
                puntaje = int(puntaje) + 1
                txt_puntaje = font.render(str(puntaje), False, (0, 255, 0))
                #print(pressed_keys)

            # if contador_tiempo == 5:
            #     contador_tiempo = 0
            #     red += 3
            #     green += 1
            #     blue += 2
            #     color_circulo = (red, green, blue)
        # if event.type == pygame.KEYDOWN:
        #     #print("Se apreto alguna tecla")
        #     if event.key == pygame.K_w:
        #         print("Apretaste la W!")
        #     if event.key == pygame.K_s:
        #         print("Apretaste la S!")
        #     if event.key == pygame.K_d:
        #         ubicacion_circulo[0] += 20
        #     if event.key == pygame.K_a:
        #         print("Apretaste la A!")

    if rect_personaje.colliderect(rect_roca):
        print("COLISIONO PERSONAJE!!!!")

    #     RGB   Red, Green, Blue -> 0 al 255
    screen.fill((199, 144, 16))# Se pinta el fondo de la ventana
    
    if esta_jugando == True:
        screen.blit(imagen_roca, rect_roca)
        #screen.blit(imagen_personaje, (225, 425))
        screen.blit(imagen_personaje, rect_personaje)
        screen.blit(imagen_joystick, (0, 0))
        screen.blit(text, (130, 50))
        screen.blit(txt_puntaje, (330, 50))

        # Se dibuja un círculo azul en el centro
        #                  donde se dibuja, color, ubicacion, radio
        pygame.draw.circle(screen, color_circulo, ubicacion_circulo, radio_circulo)
        #                donde se dibuja, color, (ubicacion, tamaño), bordes_redondeados es opcional
        pygame.draw.rect(screen, color_rectangulo, (ubicacion_rectangulo, tamanio_rectangulo), width=3, border_radius=10)
        #pygame.draw.rect(screen, color_rectangulo, mi_rectangulo)
        #pygame.draw.line(screen, (7, 135, 26), (500, 0), (0, 500), 70)



    pygame.display.flip() # Muestra los cambios en la pantalla

pygame.quit() # Fin