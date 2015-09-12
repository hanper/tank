import pygame
import time
import random

pygame.init()
#MESSAGE
LOST = "You lost"
GAME_NAME = "TANK"
GAME_OVER = "GAME OVER, Press Q to quit or R to replay"

#COLOR values
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#DEFAULT values
window_width = 800
window_height = 600
font = pygame.font.SysFont(None, 25)

#DISPLAY settings
display = pygame.display.set_mode( (window_width, window_height) )
pygame.display.set_caption(GAME_NAME)
pygame.display.update()

#TIMER
clock = pygame.time.Clock()
fps = 30

#COORDINATE values
tank_width = 30
tank_height = 30
head_width = 10
head_height = 10
speed = 10
block_size = 10

#TANK
def tank(lead_x, lead_y, tank_width, tank_height, head_position_x, head_position_y, head_width, head_height):
    pygame.draw.rect(display, red, [lead_x, lead_y, tank_width, tank_height])
    pygame.draw.rect(display, blue, [lead_x + head_position_x, lead_y + head_position_y, head_width, head_height])
#BULLET
def bullet(start_x, start_y):
    pygame.draw.rect(display, black, [start_x, start_y, block_size, block_size])
#ENEMY
def enemy(enemy_x, enemy_y):
    pygame.draw.rect(display, green, [enemy_x, enemy_y, tank_width, tank_height])
#COLLISION detector
def isHit(enemy_x, enemy_y, bullet_x, bullet_y):
    enemy_hit = False
    if bullet_x >= enemy_x and bullet_x <= enemy_x + tank_width and bullet_y >= enemy_y and bullet_y <= enemy_y + tank_height:
        enemy_hit = True
    return enemy_hit
    
#SCREEN text 
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [window_width / 2, window_height / 2])

#GAME loop
def gameLoop():
    #EXIT value
    gameExit = False
    gameOver = False

    #COORDINATE values
    lead_x = window_width / 2
    lead_y = window_height / 2
    lead_x_change = 0
    lead_y_change = 0
    head_position_x = 10
    head_position_y = -10
    head_direction = 0 #/0-right, 1-top, 2-left, 3-right/

    bullet_position_x = -10
    bullet_position_y = -10
    bullet_x_change = 0
    bullet_y_change = 0
    bullet_speed = 10

    enemy_x = round( random.randrange(0, window_width - tank_width) / 10.0 ) * 10.0
    enemy_y = round( random.randrange(0, window_height - tank_height) / 10.0 ) * 10.0

##    enemy_x_change = round( random.randrange(-10, 10) / 10.0 ) * 10.0
##    enemy_y_change = round( random.randrange(-10, 10) / 10.0 ) * 10.0
    
    #SNAKE list
    snakeList = []
    snakeLength = 1
    
    while not gameExit:
        while gameOver == True:
            display.fill(white)
            message_to_screen(GAME_OVER, red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        gameLoop()
                    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -speed
                    head_position_x = -10
                    head_position_y = 10
                    head_direction = 2
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = speed
                    head_position_x = tank_width
                    head_position_y = 10
                    head_direction = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -speed
                    head_position_x = 10
                    head_position_y = -10
                    head_direction = 1
                elif event.key == pygame.K_DOWN:
                    lead_y_change = speed
                    head_position_x = 10
                    head_position_y = tank_height
                    head_direction = 3
                elif event.key == pygame.K_SPACE:
                    bullet_position_x = lead_x + lead_x_change + head_position_x
                    bullet_position_y = lead_y + lead_y_change + head_position_y
                    bullet_x_change = 0
                    bullet_y_change = 0
                    if head_direction == 0:
                        bullet_x_change = bullet_speed
                    elif head_direction == 1:
                        bullet_y_change = -bullet_speed
                    elif head_direction == 2:
                        bullet_x_change = -bullet_speed
                    elif head_direction == 3:
                        bullet_y_change = bullet_speed
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0

        if lead_x >= window_width - (tank_width + head_width) or lead_x < 0 + (tank_width) or lead_y >= window_height - (tank_height + head_height) or lead_y < 0 + (tank_height):
                
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        enemy_x += enemy_x_change
        enemy_y += enemy_y_change
        bullet_position_x += bullet_x_change
        bullet_position_y += bullet_y_change

        display.fill(white)
        bullet(bullet_position_x, bullet_position_y)
        tank(lead_x, lead_y, tank_width, tank_height, head_position_x, head_position_y, head_width, head_height)
        enemy(enemy_x, enemy_y)
        enemy_state = isHit(enemy_x, enemy_y, bullet_position_x, bullet_position_y)

        if enemy_state:
            enemy_x = round( random.randrange(0, window_width - tank_width) / 10.0 ) * 10.0
            enemy_y = round( random.randrange(0, window_height - tank_height) / 10.0 ) * 10.0
            enemy(enemy_x, enemy_y)

        #print(enemy_state)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

#START game
gameLoop()
