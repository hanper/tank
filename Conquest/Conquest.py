import pygame
from pygame.locals import *
import sys
import random

class Conquest():
    def __init__(self, lvl = 1):
        self.display = pygame.display.set_mode((640,545))
        self.background = []
        self.lvl = lvl
        self.speed = 20
        self.gravity = 25

        self.coro = []
        self.coro_x = 20
        self.coro_x_change = 0
        self.coro_default_y = 428
        self.coro_y = self.coro_default_y
        self.coro_y_change = 0
        self.coro_jump = 50
        self.coro_direction = 'right'     #0-left, 1-right, 2-up
        self.coro_states = ['idle',
                            'run',
                            'jump',
                            'fall',
                            'slide',
                            'faint',
                            'dizzy']

        for i in range (0,13):
            self.background.append(pygame.image.load("assets/frame_" + str(i) + ".png").convert_alpha())
        self.stage = pygame.image.load("assets/stage.png").convert_alpha()

        for j in range(1,3):
            temp_img = pygame.image.load("assets/coro/"
                                         + "idle"
                                         + "/frame-"
                                         + str(j)
                                         + ".png").convert_alpha()
            self.coro.append(pygame.transform.scale(temp_img, (48,48)))

    def coroUpdate(self, coro_state):
        frame = 0   #number of frame in folder.
        if coro_state == 'idle':
            frame = 2
        elif coro_state == 'run':
            frame = 4
        elif coro_state == 'jump':
            frame = 1
        elif coro_state == 'fall':
            frame = 1
        elif coro_state == 'slide':
            frame = 1
        elif coro_state == 'faint':
            frame = 3
        elif coro_state == 'dizzy':
            frame = 2

        for j in range(1, frame + 1):
            temp_img = pygame.image.load("assets/coro/"
                                         + coro_state
                                         + "/frame-"
                                         + str(j)
                                         + ".png").convert_alpha()
            if self.coro_direction == 'left':
                directed_img = pygame.transform.flip(temp_img, 1, 0)
            else:
                directed_img = temp_img
            self.coro.append(pygame.transform.scale(directed_img, (48,48)))

        #for i in range(0, len(self.background)):
        #    self.display.blit(self.coroUpdate[state] ,(self.coro_x,self.coro_y))
                    
    def main(self):
        clock = pygame.time.Clock()
        state = 0
        #self.coro(self.coro_direction)
        coro = self.coro[state]
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.coro_x_change = self.speed
                        self.coro_drection = 'right'
                    if event.key == pygame.K_LEFT:
                        self.coro_x_change = -self.speed
                        self.coro_direction = 'left'
                    if event.key == pygame.K_UP:
                        self.coro_y = self.coro_y - self.coro_jump
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.coro_x_change = 0
                if event.key == pygame.K_UP:
                    self.coro_y = self.coro_y + self.gravity
                    if self.coro_y > self.coro_default_y:
                        self.coro_y = self.coro_default_y
                    else:
                        self.coro_y = self.coro_y + self.gravity
                    
            self.coro_x += self.coro_x_change
            #self.coro_y += self.coro_y_change
            for i in range(0, len(self.background)):
                self.display.blit(self.background[i], (0,0))
                self.display.blit(self.stage, (0,475))

                self.display.blit(coro ,(self.coro_x,self.coro_y))
                pygame.time.delay(20)
                pygame.display.flip()

            state += 1
            if state > len(self.coro) - 1:
                state = 0
            coro = self.coro[state]

            self.coroUpdate('idle')
            pygame.display.update()

        
if __name__ == "__main__":
    Conquest().main()
