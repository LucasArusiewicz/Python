import pygame

RESOLUCAO = (800,600)
FPS = 60

def main():
    pygame.init()
    tela = pygame.display.set_mode(RESOLUCAO)
    pygame.display.set_caption('PyGame')
    clock = pygame.time.Clock()
    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True


        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main();
