import random
import pygame
from math import pi as PI
from math import cos as COS
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class GDA():
    AMPLITUDE = 4
    SEED = 0

    def __init__(self, seed=0):

        if (seed == 0):
            seed = random.randint(0, 100000000)

        self.SEED = seed

    def GDDT(self, x=int, z=int):
        total = self.GetInterpolateNoise(x / 4, z / 4) * self.AMPLITUDE
        total += self.GetInterpolateNoise(x / 2, z / 2) * self.AMPLITUDE / 3
        total += self.GetInterpolateNoise(x, z) * self.AMPLITUDE / 9

        return total

    def Interpola(self,a=float, b=float, alpha=float):
        theta = alpha * PI;
        f = (1- COS(theta)) * 0.5
        return a * (1 - f) + b * f

    def GetInterpolateNoise(self, x=float, z=float):

        intX = int(x)
        intZ = int(z)

        fracX = float(x - intX)
        fracZ = float(z - intZ)

        v1 = self.GetSmoothNoise(intX, intZ)
        v2 = self.GetSmoothNoise(intX + 1, intZ)
        v3 = self.GetSmoothNoise(intX, intZ + 1)
        v4 = self.GetSmoothNoise(intX + 1, intZ)

        i1 = self.Interpola(v1, v2, fracX)
        i2 = self.Interpola(v3, v4, fracX)

        return self.Interpola(i1, i2, fracZ)

    def GetNoise(self, x=int, z=int):
        random.seed = x * 235324 + z * 32423 + self.SEED
        return random.random() * 2 - 1

    def GetSmoothNoise(self, x=int, z=int):

        pontas = (
            self.GetNoise(x - 1, z - 1) +
            self.GetNoise(x + 1, z - 1) +
            self.GetNoise(x - 1, z + 1) +
            self.GetNoise(x + 1, z + 1)) / 16

        lados = (
            self.GetNoise(x - 1, z) +
            self.GetNoise(x + 1, z) +
            self.GetNoise(x, z - 1) +
            self.GetNoise(x, z + 1)) / 8

        centro = self.GetNoise(x, z) / 4

        return pontas + lados + centro

RESOLUCAO = (1200,720)
FPS = 60
SIZE = 10
gda = GDA()
vertices = []
pontas = []
superfices = []

for i in range(SIZE):
    for j in range(SIZE):
        vertices.append((i, (gda.GDDT(i,j)), j))

for i in range(SIZE):
    for j in range(SIZE):
        atual = (i*SIZE)+j
        naFrente = atual + 1
        cima = ((i + 1)*SIZE)+j
        l = False
        c = False

        if(naFrente < SIZE*(i+1)):
            pontas.append((atual, naFrente))
            l = True

        if (cima < SIZE*SIZE):
            pontas.append((atual, cima))
            c = True

        if(l and c):
            pontas.append((cima, naFrente))
            superfices.append((atual, naFrente, cima))
            superfices.append((cima, cima+1, naFrente))


vertices = tuple(vertices)
pontas = tuple(pontas)
superfices = tuple(superfices)

print("SEED: ", end='')
print(gda.SEED)
print("-=-=- Vertices -=-=-")
print(vertices)
print("-=-=- Pontas -=-=-")
print(pontas)
print("-=-=- Superfices -=-=-")
print(superfices)
print("countV: {}".format(len(vertices)))
print("countP: {}".format(len(pontas)))
print("countS: {}".format(len(superfices)))

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

def Terreno():

    glBegin(GL_LINES)
    for ponta in pontas:
        for vertex in ponta:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_TRIANGLES)
    for surperfice in superfices:
        x = 0
        for vertice in surperfice:
            x += 1
            glColor3fv(cores[x])
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (RESOLUCAO)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Terreno')
    clock = pygame.time.Clock()
    crashed = False

    gluPerspective(80, (display[0]/display[1]), 0.8, 50.0)
    glTranslatef(-5, -5, -10)

    for x in range(15):
        glRotatef(1, 1, 0, 0)
    for x in range(90):
        glRotatef(1, 0, 1, 0)

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Terreno()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
