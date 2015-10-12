import pygame
import time
import random

pygame.init()
#MESSAGES
GAME_WELCOME = "Welcome to SNAKE MONSTER"
GAME_OBJECTIVE = "Eat all, get long"
GAME_RULE = "Dont die, dont retreat"
GAME_MENU = "Press C to continue, Q to quit"
GAME_OVER = "Your life is useless, try again!!!"
GAME_PAUSE = "Game is paused"

#Colors
white = (255,255, 255)
black = (0, 0, 0)
red = (255,0 , 0)
green = (0, 155, 0)

#Default values
display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SNAKE MONSTER")

game_icon = pygame.image.load("snake_head_30.png")
pygame.display.set_icon(game_icon)

snake_head = pygame.image.load("snake_head_20.png")
apple_img = pygame.image.load("apple.png")

clock = pygame.time.Clock()

apple_thickness = 30
block_size = 20
FPS = 15

direction = "right"

small_font = pygame.font.SysFont("comicsansms", 16)
medium_font = pygame.font.SysFont("timesroman", 32)
large_font = pygame.font.SysFont("arial", 64)

#Scoring system
def score(score):
    text = small_font.render("Score: " + str(score), True, black)
    game_display.blit(text, [0, 0])

#Generate random position for an apple
def randAppleGen():
    apple_x = random.randrange(0, display_width - apple_thickness)
    apple_y = random.randrange(0, display_height - apple_thickness)

    return apple_x, apple_y

#Pause game progress
def pause():
    paused = True

    messageToScreen(GAME_PAUSE, black, -100, "medium")
    messageToScreen(GAME_MENU, black, 100)
    pygame.display.update()
    
    while paused:
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
        #game_display.fill(white)
        clock.tick(5)

#Game introduction
def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(white)
        messageToScreen(GAME_WELCOME, green, -100, "large")
        messageToScreen(GAME_OBJECTIVE, black, -25, "medium")
        messageToScreen(GAME_RULE, black, 100, "small")
        messageToScreen(GAME_MENU, black, 150, "small")
        pygame.display.update()
        clock.tick(FPS)

    gameLoop()

#Snake manager
def snake(block_size, snake_list):
    if direction == "right":
        head = pygame.transform.rotate(snake_head, 270)
    if direction == "left":
        head = pygame.transform.rotate(snake_head, 90)
    if direction == "up":
        head = snake_head
    if direction == "down":
        head = pygame.transform.rotate(snake_head, 180)

    game_display.blit(head, (snake_list[-1][0], snake_list[-1][1]))                      
    for XnY in snake_list[:-1]:
        pygame.draw.rect(game_display, green, [XnY[0], XnY[1], block_size, block_size])

#Text renderer
def textObjects(text, color, size):
    if size == "small":
        text_surface = small_font.render(text, True, color)
    elif size == "medium":
        text_surface = medium_font.render(text, True, color)
    elif size == "large":
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()

#Message display
def messageToScreen(msg, color, y_displace = 0, size = "small"):
    text_surf, text_rect = textObjects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    game_display.blit(text_surf, text_rect)
    
#Main game loop
def gameLoop():
    global direction

    direction = "right"
    game_exit = False
    game_over = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    apple_x, apple_y = randAppleGen()

    while not game_exit:
        if game_over == True:
            messageToScreen(GAME_OVER, red, -50, "large")
            messageToScreen(GAME_MENU, black, 50, "medium")
            pygame.display.update()
        while game_over == True:
            #game_display.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_over = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)
        game_display.blit(apple_img, (apple_x, apple_y))

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        snake(block_size, snake_list)
        score((snake_length - 1) * 10)
        pygame.display.update()

        if lead_x > apple_x and lead_x < apple_x + apple_thickness or lead_x + block_size > apple_x and lead_x + block_size < apple_x + apple_thickness:
            if lead_y > apple_y and lead_y < apple_y + apple_thickness:
                apple_x, apple_y = randAppleGen()
                snake_length += 1
            elif lead_y + block_size > apple_y and lead_y + block_size < apple_y + apple_thickness:
                apple_x, apple_y = randAppleGen()
                snake_length += 1
            
        clock.tick(FPS)

    pygame.quit()
    quit()

gameIntro()
