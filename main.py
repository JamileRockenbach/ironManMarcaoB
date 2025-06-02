import pygame
import random
from recursos.basicos import limparTela, aguaradar
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man do Marcão")
relogio = pygame.time.Clock()
branco = (255,255,255)
preto = (0,0,0)

iron = pygame.image.load("assets/iron.png")
fundoJogo = pygame.image.load("assets/fundoJogo.png")
missiel = pygame.image.load("assets/missile.png")
missielSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(missielSound)
velocidade_missiel = 3
posicaoXmissiel = 100
posicaoYmissiel = -250
posicaoXiron = 275
posicaoYiron = 400
movimentoXiron = 0
movimentoYiron = 0
velocidade = 5
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(-1)
pontos = 0
fonte = pygame.font.SysFont("comicsans",18)

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXiron = -velocidade
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXiron = velocidade
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYiron = -velocidade
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYiron = velocidade
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYIron = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYIron = 0

    posicaoXiron = posicaoXiron + movimentoXiron
    posicaoYiron = posicaoYiron + movimentoYiron
    if posicaoXiron < 0:
        posicaoXiron = 0
    elif posicaoXiron > 550:
        posicaoXiron = 550
    if posicaoYiron < 0:
        posicaoYiron = 0
    elif posicaoYiron > 473:
        posicaoYiron = 473

    posicaoYmissiel += velocidade_missiel
    if posicaoYmissiel > 600:
        posicaoYmissiel = -250
        pygame.mixer.Sound.play(missielSound)
        posicaoXmissiel = random.randint(0,800)
        velocidade_missiel += 1
        pontos += 1

    tela.fill(branco)
    tela.blit(fundoJogo, (0,0))
    tela.blit(iron, (posicaoXiron, posicaoYiron))
    tela.blit(missiel, (posicaoXmissiel, posicaoYmissiel))
    textoPontos = fonte.render(f'Pontos: {pontos}', True, branco)
    tela.blit(textoPontos,(10,10))


    pygame.display.update()
    relogio.tick(60)