import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

RESOLUCAO = (800,600)
FPS = 60

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

pontas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

cores = (
    (1,0,0),
    (1,1,0),
    (0,0,1),
    (0,1,1),
    (1,1,1),
    (0,1,1),
    (1,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

superfices = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cubo():
    glBegin(GL_QUADS)
    for surperfice in superfices:
        x = 0
        for vertice in surperfice:
            x+=1
            glColor3fv(cores[x])
            glVertex3fv(verticies[vertice])
    glEnd()

    glBegin(GL_LINES)
    for ponta in pontas:
        for vertice in ponta:
            glVertex3fv(verticies[vertice])
    glEnd()

def main():
    pygame.init()
    tela = RESOLUCAO
    pygame.display.set_mode(tela, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Cubo')
    clock = pygame.time.Clock()
    crashed = False

    gluPerspective(45, (tela[0]/tela[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        glRotatef(1, 2, 8, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cubo()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    quit()
    
if __name__ == '__main__':
    main()
