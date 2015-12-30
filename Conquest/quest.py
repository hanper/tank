import pygame

pygame.init()

blue = (0,0,255)
screen = pygame.display.set_mode((1000,400))

class Quest(object):
    def __init__(self):
        self.pos = []
        self.color = blue

    def main(self):
        while True:
            self.pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()


            
            
            screen.fill((255,255,0))
            pygame.display.update()
            
            print(self.pos)

if __name__ == "__main__":
    Quest().main()
