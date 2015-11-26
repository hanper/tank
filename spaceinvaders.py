import pygame
from pygame.locals import *
import sys

class SpaceInvaders:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.enemySprites = {
            0:[pygame.image.load("assets/a1_0.png").convert(), pygame.image.load("assets/a1_1.png").convert()],
            1:[pygame.image.load("assets/a2_0.png").convert(), pygame.image.load("assets/a2_1.png").convert()],
            2:[pygame.image.load("assets/a3_0.png").convert(), pygame.image.load("assets/a3_1.png").convert()]
            }
        self.player = pygame.image.load("assets/shooter.png").convert()
        self.animationOn = 0
        self.direction = 1
        self.enemySpeed = 10
        self.lastEnemyMove = 0
        self.enemyX = 50
        self.enemyY = 50
        self.playerX = 400
        self.playerY = 550
        self.bullet = None
        self.enemies = []
        startX = 50
        startY = 50

    def enemyUpdate(self):
        if not self.lastEnemyMove:
            self.enemyX += self.enemySpeed * self.direction
            self.lastEnemyMove = 1
            if self.animationOn:
                self.animationOn -= 1
            else:
                self.animationOn += 1

            if self.enemyX >= 750 or self.enemyX <= 0:
                self.direction *= -1
                self.enemyY += self.enemySpeed * 2 
        else:
            self.lastEnemyMove -= 1

    def playerUpdate(self):
        key = pygame.key.get_pressed()
        if key[K_RIGHT] and self.playerX < 800 - self.player.get_width():
            self.playerX += 5
        elif key[K_LEFT] and self.playerX > 0:
            self.playerX -= 5
        if key[K_SPACE] and not self.bullet:
            self.bullet = pygame.Rect(self.playerX + self.player.get_width() / 2, self.playerY - 15, 5, 10)
            
    def bulletUpdate(self):
        if self.bullet:
            self.bullet.y -= 5
            if self.bullet.y < 0:
                self.bullet = None
        
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()

            self.screen.blit(pygame.transform.scale(self.enemy[self.animationOn], (35,35)), (self.enemyX, self.enemyY))
            self.screen.blit(self.player, (self.playerX, self.playerY))
            if self.bullet:
                pygame.draw.rect(self.screen, (52,255,0), self.bullet)
            self.bulletUpdate()
            self.enemyUpdate()
            self.playerUpdate()
            pygame.display.flip()

if __name__ == "__main__":
    SpaceInvaders().run()
