import pygame
import time
import random

pygame.init()
#########START of DEFAULT VALUES##########
#Message
GAME_NAME = "Super Tanks"
GAME_WELCOME = "Welcome to Super Tanks"
GAME_MENU = "Press C to continue or Q to quit"
GAME_OBJECTIVE = "Destroy your enemy"
GAME_RULE = "Just dont die"
GAME_OVER = "You Lost"
GAME_PAUSE = "Are you tired?"

#Font
small_font = pygame.font.SysFont("timesroman", 16)
medium_font = pygame.font.SysFont("timesroman", 25)
large_font = pygame.font.SysFont("timesroman", 48)

#Color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Game window
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(GAME_NAME)

clock = pygame.time.Clock()

#Image
#game_icon = pygame.image.load("game_icon.png")
#pygame.display.set_icon(icon)

#########END of DEFAULT VALUES##########
#########START of FUNCTIONS##########
#Scoring system
def score(score):
    text = small_font.render("Score: " + str(score), True, black)
    game_display.blit(text, [0,0])

#Text & Message manager
def textObjects(text, color, size = "small"):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    if size == "medium":
        text_surface = medium_font.render(text, True, color)
    if size == "large":
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()

def messageToScreen(msg, color, y_displace = 0, size = "small"):
    text_surf, text_rect = textObjects(msg, color, size)
    text_rect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    game_display.blit(text_surf, text_rect)

#Test EVENT_HANDLER
def eventHandler():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

#Game pause
def pause():
    paused = True
    messageToScreen(GAME_PAUSE, black, -100, "medium")
    messageToScreen(GAME_MENU, black, 100, "small")
    pygame.display.update()

    while paused:
        eventHandler()
    
        clock.tick(5)

#Game intro with menu
def gameIntro():
    intro = True

    while intro:
        eventHandler()

        game_display.fill(white)
        messageToScreen(GAME_WELCOME, green, -150, "large")
        messageToScreen(GAME_OBJECTIVE, green, -50, "small")
        messageToScreen(GAME_RULE, green, 50, "small")
        messageToScreen(GAME_MENU, green, 150, "medium")
        pygame.display.update()

        clock.tick(15)

gameIntro()

#MAIN game function
def gameLoop():
    game_exit = False
    game_over = False
    FPS = 15

    while not game_exit:
        if game_over == True:
            messageToScreen(GAME_OVER, red, -50, "large")
            messageToScreen(GAE_MENU, black, 100, "medium")
            pygame.display.update()
            while game_over == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_exit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            game_exit = True
                            game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_p:
                    pause()

        game_display.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
