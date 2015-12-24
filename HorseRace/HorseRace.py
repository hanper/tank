import pygame
from pygame.locals import *
import random

class HorseRace:
    def __init__(self):
        self.display = pygame.display.set_mode((800,600))
        self.background = pygame.image.load("images/background.png").convert()
        self.bones = [pygame.image.load("images/horse.png").convert_alpha(),
                      pygame.image.load("images/cattle.png").convert_alpha(),
                      pygame.image.load("images/sheep.png").convert_alpha(),
                      pygame.image.load("images/goat.png").convert_alpha(),
                      pygame.image.load("images/camel.png").convert_alpha()]
        self.position = 0
        self.player = []

    def menu(self):
        pass

    def updateRace(self):
        pass

    def updateRoll(self):
        pass

    def main(self):
        pass

if __name__ == "__main__":
    HorseRace().main()
