import pygame
import random
import cor as cores

RESOLUCAO = (1600,900)
FPS = 600
TAMANHO = 13
PORCENTAGEM = 0.8

def main():
    pygame.init()
    tela = pygame.display.set_mode(RESOLUCAO)
    pygame.display.set_caption('10PRINT')
    clock = pygame.time.Clock()
    crashed = False
    x = 0
    y = 0
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        if(random.random() < PORCENTAGEM):
            pygame.draw.line(tela, cores.randCorBonita(), (x + TAMANHO,y), (x,y + TAMANHO))
        else:
            pygame.draw.line(tela, cores.randCorBonita(), (x,y), (x + TAMANHO,y  + TAMANHO))

        x += TAMANHO

        if(x > RESOLUCAO[0]):
            x = 0
            y += TAMANHO
        if (y > RESOLUCAO[1]):
            y = 0
            tela.fill([0, 0, 0])

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main();
