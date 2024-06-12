import pygame
import sys

pygame.init()

largura = 1280
altura = 720
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
running = True

icone = pygame.image.load("istockphoto-928418862-612x612.jpg")
pygame.display.set_icon(icone)

posicao_bola = pygame.Vector2(largura // 2, altura // 2)
velocidade_bola = pygame.Vector2(0, 0)
gravidade = 0.5
raio_bola = 50
velocidade = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocidade_bola.y = -10  # Aplicar impulso para cima

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_s] and posicao_bola.y + raio_bola < altura:
        posicao_bola.y += velocidade
    if teclas[pygame.K_a] and posicao_bola.x - raio_bola > 0:
        posicao_bola.x -= velocidade
    if teclas[pygame.K_d] and posicao_bola.x + raio_bola < largura:
        posicao_bola.x += velocidade

    #  gravidade
    velocidade_bola.y += gravidade
    posicao_bola += velocidade_bola

    # colisão com o chão
    if posicao_bola.y + raio_bola >= 600:
        posicao_bola.y = 600 - raio_bola
        velocidade_bola.y = 0

    # limitar a bola dentro da tela
    if posicao_bola.x - raio_bola < 0:
        posicao_bola.x = raio_bola
    if posicao_bola.x + raio_bola > largura:
        posicao_bola.x = largura - raio_bola

    # preencher o fundo com uma cor
    screen.fill("blue")

    # desenhar elementos na tela
    pygame.draw.rect(screen, (0, 255, 0), (0, 600, 1280, 120))
    pygame.draw.circle(screen, (255, 255, 255), (560, 200), 30)
    pygame.draw.circle(screen, (255, 255, 255), (1100, 250), 30)
    pygame.draw.circle(screen, (255, 255, 255), (300, 200), 30)
    pygame.draw.circle(screen, (255, 255, 255), (800, 205), 30)
    pygame.draw.circle(screen, (255, 255, 255), (150, 220), 30)
    pygame.draw.circle(screen, (255, 255, 255), (950, 210), 30)
    pygame.draw.circle(screen, (255, 255, 255), (560, 200), 30)
    pygame.draw.circle(screen, (255, 255, 255), (400, 200), 30)

    # desenhar bola
    pygame.draw.circle(screen, (255, 0, 0), posicao_bola, raio_bola)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
