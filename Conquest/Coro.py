import pygame
from pygame.locals import *
import sys
import random

class Coro():
    def __init__(self):
        self.display = pygame.display.set_mode((400,600))
        self.state = ['idle',
                      'run',
                      'jump',
                      'fall',
                      'slide',
                      'faint',
                      'dizzy']
        self.coro_direction = ['left', 'right']
        self.sprites = []

    def updateModel(self, state, direction):
        frame = 0   #number of frame in folder.
        coro_state = state
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
            if direction == 'left':
                directed_img = pygame.transform.flip(temp_img, 1, 0)
            else:
                directed_img = temp_img
            self.sprites.append(pygame.transform.scale(directed_img, (48,48)))

    def main(self):
        clock = pygame.time.Clock()
        test_state = 0
        test_x = 10
        test_y = 50
        direction = ''

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        test_state += 1
                        test_x += 30
                        test_y += 50
                        self.sprites = []
                    if event.key == K_LEFT:
                        direction = self.coro_direction[0]
                        test_state = 1
                        test_x += -10
                        self.sprites = []
                    if event.key == K_RIGHT:
                        direction = self.coro_direction[1]
                        test_state = 1
                        test_x += 10
                        self.sprites = []
                if event.type == KEYUP:
                    test_state = 0
                    self.sprites = []

            self.display.fill((0,0,0))

            for i in range(0, len(self.sprites)):
                self.display.blit(self.sprites[i], (test_x, test_y))
                pygame.time.delay(120)
                pygame.display.flip()

            pygame.display.update()

            if test_state > 6:
                test_state = 0
            self.updateModel(self.state[test_state], direction)

if __name__ == "__main__":
    Coro().main()

        
