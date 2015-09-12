import pygame
import time
import random
import math

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
top_radius = 10
bottom_radius = 30
turret_wall = 0
turret_head_length = 40
turret_head_thickness = 5

#TURRET
def turret(center_x, center_y, lead_x, lead_y, enemy_b_p_x, enemy_b_p_y):
    end_x = (turret_head_length) * ((lead_x - center_x) / math.sqrt(math.pow(lead_x - center_x, 2) + math.pow(lead_y - center_y, 2))) + center_x
    end_y = (turret_head_length) * ((lead_y - center_y) / math.sqrt(math.pow(lead_x - center_x, 2) + math.pow(lead_y - center_y, 2))) + center_y
    pygame.draw.circle(display, green, (center_x, center_y), bottom_radius, turret_wall)
    turret_head(center_x, center_y, end_x, end_y)
    pygame.draw.circle(display, blue, (center_x, center_y), top_radius, turret_wall)
    bullet(enemy_b_p_x, enemy_b_p_y)
#TURRET_HEAD
def turret_head(center_x, center_y, end_x, end_y):
    pygame.draw.line(display, black, (center_x, center_y), (end_x, end_y), turret_head_thickness)
#TANK
def tank(lead_x, lead_y, tank_width, tank_height, head_position_x, head_position_y):
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
#TURRET&BULLET collision detector
def isTurretHit(center_x, center_y, bullet_x, bullet_y):
    turret_hit = False
    if bullet_x >= center_x - bottom_radius and bullet_x <= center_x + bottom_radius:
        if bullet_y >= center_y - bottom_radius and bullet_y <= center_y + bottom_radius:
            turret_hit = True
    elif bullet_x + block_size >= center_x - bottom_radius and bullet_x + block_size <= center_x + bottom_radius:
        if bullet_y + block_size >= center_y - bottom_radius and bullet_y + block_size <= center_y + bottom_radius:
            turret_hit = True
    return turret_hit
#TANK&BULLET collision detector
def isTankHit(lead_x, lead_y, bullet_x, bullet_y):
    tank_hit = False
    if bullet_x >= lead_x and lead_x <= lead_x + tank_width:
        if bullet_y >= lead_y and bullet_y <= lead_y + tank_height:
            tank_hit = True
    elif bullet_x + block_size >= lead_x and bullet_x + block_size <= lead_x + tank_width:
        if bullet_y + block_size >= lead_y and bullet_y + block_size <= lead_y + tank_height:
            tank_hit = True
    return tank_hit
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

    enemy_bullet_x = 0
    enemy_bullet_y = 0
    enemy_b_p_x = -10
    enemy_b_p_y = -10

    enemy_x = round( random.randrange(0, window_width - tank_width) / 10.0 ) * 10.0
    enemy_y = round( random.randrange(0, window_height - tank_height) / 10.0 ) * 10.0

    center_x = random.randrange(turret_head_length, window_width - turret_head_length)
    center_y = random.randrange(turret_head_length, window_height - turret_head_length)
##    enemy_x_change = round( random.randrange(-10, 10) / 10.0 ) * 10.0
##    enemy_y_change = round( random.randrange(-10, 10) / 10.0 ) * 10.0

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
                enemy_b_p_x = (turret_head_length) * ((lead_x - center_x) / math.sqrt(math.pow(lead_x - center_x, 2) + math.pow(lead_y - center_y, 2))) + center_x
                enemy_b_p_y = (turret_head_length) * ((lead_y - center_y) / math.sqrt(math.pow(lead_x - center_x, 2) + math.pow(lead_y - center_y, 2))) + center_y
                if center_x < lead_x and center_y < lead_y:
                    enemy_bullet_x = bullet_speed
                    enemy_bullet_y = bullet_speed / (enemy_b_p_x - center_x) * ( enemy_b_p_y - center_y)
                elif center_x < lead_x and center_y > lead_y:
                    enemy_bullet_x = bullet_speed
                    enemy_bullet_y = -bullet_speed / (enemy_b_p_x - center_x) * ( -enemy_b_p_y + center_y)
                elif center_x > lead_x and center_y < lead_y:
                    enemy_bullet_x = -bullet_speed
                    enemy_bullet_y = bullet_speed / (-enemy_b_p_x + center_x) * ( enemy_b_p_y - center_y)
                elif center_x > lead_x and center_y > lead_y:
                    enemy_bullet_x = -bullet_speed
                    enemy_bullet_y = -bullet_speed / (-enemy_b_p_x + center_x) * ( -enemy_b_p_y + center_y)

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
##        enemy_x += enemy_x_change
##        enemy_y += enemy_y_change
        bullet_position_x += bullet_x_change
        bullet_position_y += bullet_y_change

        enemy_b_p_x += enemy_bullet_x
        enemy_b_p_y += enemy_bullet_y
        
        display.fill(white)
        bullet(bullet_position_x, bullet_position_y)
        tank(lead_x, lead_y, tank_width, tank_height, head_position_x, head_position_y)
        #enemy(enemy_x, enemy_y)
        turret(center_x, center_y, lead_x, lead_y, enemy_b_p_x, enemy_b_p_y)
        turret_state = isTurretHit(center_x, center_y, bullet_position_x, bullet_position_y)
        tank_state = isTankHit(lead_x, lead_y, enemy_b_p_x, enemy_b_p_y)
        
        if turret_state:
            center_x = random.randrange(0, window_width - turret_head_length)
            center_y = random.randrange(0, window_height - turret_head_length)
            turret(center_x, center_y, lead_x, lead_y, enemy_b_p_x, enemy_b_p_y)
        if tank_state:
            gameOver = True
            
##        enemy_state = isHit(enemy_x, enemy_y, bullet_position_x, bullet_position_y)
##
##        if enemy_state:
##            enemy_x = round( random.randrange(0, window_width - tank_width) / 10.0 ) * 10.0
##            enemy_y = round( random.randrange(0, window_height - tank_height) / 10.0 ) * 10.0
##            enemy(enemy_x, enemy_y)

        #print(enemy_state)
        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

#START game
gameLoop()
