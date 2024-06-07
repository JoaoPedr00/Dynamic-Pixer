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



posicao_bola = pygame.Vector2(largura // 2, altura // 2)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                posicao_bola.y -= velocidade * 2

    screen.fill("blue")


    chao = pygame.draw.rect(screen,(0,255,0), (0,600,1280,120))

    pygame.draw.circle(screen,(255,255,255), (560,200),30)
    pygame.draw.circle(screen,(255,255,255), (1100,250),30)
    pygame.draw.circle(screen,(255,255,255), (300,200),30)
    pygame.draw.circle(screen,(255,255,255), (800,205),30)
    pygame.draw.circle(screen,(255,255,255), (150,220),30)
    pygame.draw.circle(screen,(255,255,255), (950,210),30)
    pygame.draw.circle(screen,(255,255,255), (560,200),30)
    pygame.draw.circle(screen,(255,255,255), (400,200),30)


    
    raio_bola = 50
    velocidade = 5




                       



    teclas = pygame.key.get_pressed()
    '''if teclas[pygame.K_w]:
        posicao_bola.y -= velocidade'''
    if teclas[pygame.K_s]:
        posicao_bola.y += velocidade
    if teclas[pygame.K_a] and posicao_bola.x > 0:
        posicao_bola.x -= velocidade
    if teclas[pygame.K_d]and posicao_bola.x < 1280:
        posicao_bola.x += velocidade


    pygame.draw.circle(screen,(255,0,0), (posicao_bola),(raio_bola))

   

   

    pygame.display.flip()

    clock.tick(144)



pygame.quit

