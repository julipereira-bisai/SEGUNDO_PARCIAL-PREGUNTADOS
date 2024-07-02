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

# alto = 700
# ancho = 500
#                                  [x   ,   y]
screen = pygame.display.set_mode(config_pantalla) #Se crea una ventana

ubicacion_rectangulo = [225, 225]
tamanio_rectangulo = [50, 50]
ubicacion_circulo = [250, 250]

#rectangulo = [ubicacion_rectangulo, tamanio_rectangulo]
contador_tiempo = 0
color_rectangulo = (29, 107, 224)
color_circulo = (224, 29, 224)

# Imagenes
gif_start = pygame.image.load("START (3).gif") # 512x512
gif_start = pygame.transform.scale(gif_start, (500, 500))
# Textos
font = pygame.font.SysFont("Arial Narrow", 50)
text = font.render("Puntaje:", True, (0, 255, 0))
puntaje = "50"
txt_puntaje = font.render(puntaje, True, (0, 255, 0))

running = True
while running:
    pressed_keys = pygame.key.get_pressed()
    
   # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
           running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}")
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse up: {event.pos}")

        # if event.type == tick:
            # if True in pressed_keys:
                #if pressed_keys[K_d]:
                    #ubicacion_circulo[0] += 1
                    #if ubicacion_circulo[0] > config_pantalla[0] + 75:
                        #ubicacion_circulo[0] = 0 - 75
                #if pressed_keys[K_a]:
                    #ubicacion_circulo[0] -= 1
                    #if ubicacion_circulo[0] < 0 - 75:
                        #ubicacion_circulo[0] = config_pantalla[0] + 75
                #if pressed_keys[K_w]:
                    #ubicacion_circulo[1] -= 1
                #if pressed_keys[K_s]:
                    #ubicacion_circulo[1] += 1
            
            #contador_tiempo += 1
            #print(f"Ya pasaron {contador_tiempo} segundo")

            #ubicacion_rectangulo[0] += 1
            #if ubicacion_rectangulo[0] > config_pantalla[0]:
                #ubicacion_rectangulo[0] = 0 - tamanio_rectangulo[0]
            #if ubicacion_rectangulo[0] > 0:
                #ubicacion_rectangulo[0] -= 1
                # ubicacion_rect[X] 

            #if contador_tiempo == 100:
                #color_circulo = (random.randint(0, 255), 0, random.randint(0, 255))
                #contador_tiempo = 0
                #print(pressed_keys)
        
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_KP_ENTER:
                
        #     #print("Se apreto alguna tecla")
        #     if event.key == pygame.K_w:
        #         print("Apretaste la W!")
        #     if event.key == pygame.K_s:
        #         print("Apretaste la S!")
        #     if event.key == pygame.K_d:
        #         ubicacion_circulo[0] += 20
        #     if event.key == pygame.K_a:
        #         print("Apretaste la A!")


    #     RGB   Red, Green, Blue -> 0 al 255
    screen.fill((0, 0, 0))# Se pinta el fondo de la ventana
    
    screen.blit(gif_start, (0, 50))

    # Se dibuja un círculo azul en el centro
    #                donde se dibuja, color, ubicacion, radio
    # pygame.draw.circle(screen, color_circulo, ubicacion_circulo, 75)
    #                donde se dibuja, color, (ubicacion, tamaño)
    # pygame.draw.rect(screen, color_rectangulo, (ubicacion_rectangulo, tamanio_rectangulo), border_radius=15)
    #pygame.draw.line(screen, (7, 135, 26), (500, 0), (0, 500), 70)

    pygame.display.flip() # Muestra los cambios en  la pantalla

pygame.quit() # Fin