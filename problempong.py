import pygame, sys, random
from pygame.locals import *

pygame.init()

gamename = pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
FPS = 60

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((800, 800))
screen.fill(black)

line = pygame.draw.line(screen, white, (400, 800), (400, 0), 5)


class Player(object):
    def __init__(self, screen):
        pady = 350
        padx = 40
        padh = 100
        padw = 35
        dist = 5
        self.pady = pady
        self.padx = padx
        self.padh = padh
        self.padw = padw
        self.dist = dist
        self.screen = screen

    def draw(self):
        playerpaddle = pygame.rect.Rect((self.padx, self.pady, self.padw, self.padh))
        pygame.draw.rect(self.screen, white, playerpaddle)

    def controlkeys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_s]:
            self.pady += self.dist
        elif key[pygame.K_w]:
            self.pady -= self.dist


pygame.display.update()

player = Player(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player.controlkeys()
    player.draw()
    pygame.display.update()
    clock.tick(FPS)