import pygame
import sys

pygame.init()

largura = 1280
altura = 720
screen = pygame.display.set_mode((largura,altura))
clock = pygame.time.Clock()
running = True


icone = pygame.image.load("istockphoto-928418862-612x612.jpg")
pygame.display.set_icon(icone)




left = 10
top = 10
width = 50
height = 50


velocidade = 5
left_ = 100
top_ = 100
width_ = 50
geight_ = 50
posicao_retangulo_azul = ((left_,top_,width_,geight_))

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    posicao_retangulo_vermelho = ((left,top,width,height))

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        posicao_retangulo_vermelho = (left,top - velocidade,width,height)
    if teclas[pygame.K_s]:
        posicao_retangulo_vermelho = (left,top + velocidade,width,height)
    if teclas[pygame.K_a]:
        posicao_retangulo_vermelho = (left - velocidade,top,width,height)
    if teclas[pygame.K_d]:
        posicao_retangulo_vermelho = (left + velocidade,top,width,height)








    retangulo_vermelho = pygame.draw.rect(screen,(255,0,0),posicao_retangulo_vermelho)
    retangulo_azul = pygame.draw.rect(screen,(0,0,255),posicao_retangulo_azul)


    pygame.display.flip()
    clock.tick(60)





pygame.quit()
