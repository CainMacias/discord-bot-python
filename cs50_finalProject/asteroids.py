import pygame
import math
import random

# Inicializar pygame
pygame.init()

# Configuración de ventana
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("CS50 Asteroids")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Clase de la nave
class Nave:
    def __init__(self):
        self.x = ANCHO / 2
        self.y = ALTO / 2
        self.angulo = 0
        self.velocidad = 0
        self.triangulo = [(0, -15), (10, 10), (-10, 10)]

    def dibujar(self):
        puntos_rotados = []
        for x, y in self.triangulo:
            xr = x * math.cos(math.radians(self.angulo)) - y * math.sin(math.radians(self.angulo))
            yr = x * math.sin(math.radians(self.angulo)) + y * math.cos(math.radians(self.angulo))
            puntos_rotados.append((self.x + xr, self.y + yr))
        pygame.draw.polygon(VENTANA, BLANCO, puntos_rotados, 1)

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.angulo += 5
        if teclas[pygame.K_RIGHT]:
            self.angulo -= 5
        if teclas[pygame.K_UP]:
            self.velocidad += 0.3
        else:
            self.velocidad *= 0.98  # freno suave
        self.x += self.velocidad * math.sin(math.radians(-self.angulo))
        self.y += self.velocidad * math.cos(math.radians(-self.angulo))
        self.x %= ANCHO
        self.y %= ALTO

# Clase de los proyectiles
class Bala:
    def __init__(self, x, y, angulo):
        self.x = x
        self.y = y
        self.angulo = angulo
        self.velocidad = 10

    def mover(self):
        self.x += self.velocidad * math.sin(math.radians(-self.angulo))
        self.y += self.velocidad * math.cos(math.radians(-self.angulo))
        self.x %= ANCHO
        self.y %= ALTO

    def dibujar(self):
        pygame.draw.circle(VENTANA, BLANCO, (int(self.x), int(self.y)), 2)

# Bucle principal
def main():
    reloj = pygame.time.Clock()
    nave = Nave()
    balas = []

    corriendo = True
    while corriendo:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                balas.append(Bala(nave.x, nave.y, nave.angulo))

        nave.mover()

        VENTANA.fill(NEGRO)
        nave.dibujar()

        for bala in balas:
            bala.mover()
            bala.dibujar()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
