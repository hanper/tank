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
GAME_OPTIONS = "OPTIONS"
GAME_INSTRUCTION = "Use arrows to move and spacebar to shoot"

BUTTON_TYPE_PLAY = "play"
BUTTON_TYPE_OPTIONS = "options"
BUTTON_TYPE_QUIT = "quit"

#Font
small_font = pygame.font.SysFont("timesroman", 16)
medium_font = pygame.font.SysFont("timesroman", 25)
large_font = pygame.font.SysFont("timesroman", 48)

#Color
white = (255,255,255)
black = (0,0,0)
red = (200,20,20)
light_red = (255,0,0)
green = (20,200,20)
light_green = (0,255,0)
blue = (20,20,200)
light_blue = (0,0,255)
yellow = (200,200,20)
light_yellow = (255,255,0)

#Game window
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(GAME_NAME)

#Game object defaults
tank_width = 50
tank_height = 20
tank_speed = 5

turret_width = 5
wheel_width = 5

barrier_width = 50

clock = pygame.time.Clock()

#Image
#game_icon = pygame.image.load("game_icon.png")
#pygame.display.set_icon(icon)

#########END of DEFAULT VALUES##########
#########START of FUNCTIONS##########
#Barrier
def barrier(location_x, height):
    pygame.draw.rect(game_display, green, [location_x, display_height - height, barrier_width, height])

#Shooting
def fireShell(xy, tank_x, tank_y, turret_position):
    fire = True

    starting_coordinate = list(xy)

    while fire:
        quitListener()

        print(starting_coordinate[0], starting_coordinate[1])
        pygame.draw.circle(game_display, red, starting_coordinate, 5)

        starting_coordinate[0] -= (10 - turret_position) * 2
        starting_coordinate[1] += int((((starting_coordinate[0] - xy[0]) * 0.01) ** 2) - (turret_position + turret_position / (10 - turret_position)))

        if starting_coordinate[1] > display_height:
            fire = False

        pygame.display.update()
        clock.tick(100)

#Tank drawer
def tank(x, y, turret_position):
    x = int(x)
    y = int(y)

    possible_turrets = [(x-25, y-5),
                        (x-23, y-7),
                        (x-21, y-9),
                        (x-19, y-11),
                        (x-17, y-13),
                        (x-15, y-15)]

    pygame.draw.circle(game_display, black, (x,y), int(tank_height / 2))
    pygame.draw.rect(game_display, black, (x - (tank_width / 2), y, tank_width, tank_height))

    pygame.draw.line(game_display, black, (x,y), possible_turrets[turret_position], turret_width)

    #for turret in range(6):
    #   pygame.draw.line(game_display, black, (x,y), possible_turrets[turret], turret_width)

    start_x = 20
    for wheel_number in range(9):
        pygame.draw.circle(game_display, black, (x - start_x, y + 20), wheel_width)
        start_x -= 5

    return possible_turrets[turret_position]
    
#Button text
def textToButton(text, color, button_x, button_y, button_width, button_height, size = "medium"):
    text_surf, text_rect = textObjects(text, color, size)
    text_rect.center = (button_x + (button_width / 2), button_y + (button_height / 2))
    game_display.blit(text_surf, text_rect)

#Button generate
def button(text, x, y, width, height, inactive_color, active_color, action):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(game_display, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == BUTTON_TYPE_PLAY:
                gameLoop()
            elif action == BUTTON_TYPE_OPTIONS:
                gameOptions()
            elif action == BUTTON_TYPE_QUIT:
                pygame.quit()
                quit()      
    else:
        pygame.draw.rect(game_display, inactive_color, (x, y, width, height))

    textToButton(text, black, x, y, width, height)

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
def quitListener():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

#Game menu
def gameMenu():
    button("Play", 150, 400, 100, 50, green, light_green, action = BUTTON_TYPE_PLAY)
    button("Options", 350, 400, 100, 50, yellow, light_yellow, action = BUTTON_TYPE_OPTIONS)
    button("Quit", 550, 400, 100, 50, red, light_red, action = BUTTON_TYPE_QUIT)

#Game options
def gameOptions():
    game_options = True

    while game_options:
        quitListener()

        game_display.fill(white)
        messageToScreen(GAME_OPTIONS, green, -150, "large")
        messageToScreen(GAME_INSTRUCTION, green, -50, "small")
        messageToScreen("P to Pause", green, 50, "small")        

        gameMenu()

        pygame.display.update()
        clock.tick(15)        

#Game intro with menu
def gameIntro():
    intro = True

    while intro:
        eventHandler()

        game_display.fill(white)
        messageToScreen(GAME_WELCOME, green, -150, "large")
        messageToScreen(GAME_OBJECTIVE, green, -50, "small")
        messageToScreen(GAME_RULE, green, 50, "small")

        gameMenu()
        
        pygame.display.update()
        clock.tick(15)

#MAIN game function
def gameLoop():
    game_exit = False
    game_over = False
    FPS = 15
    
    tank_x = display_width * 0.9
    tank_y = display_height * 0.9
    tank_move = 0
    turret_position = 0
    turret_change = 0
    
    barrier_x = (display_width / 2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    barrier_height = random.randrange(0.1 * display_height, 0.6 * display_height)
    
    while not game_exit:
        game_display.fill(white)
        gun = tank(tank_x, tank_y, turret_position)
        
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
                    tank_move = -tank_speed
                elif event.key == pygame.K_RIGHT:
                    tank_move = tank_speed
                elif event.key == pygame.K_UP:
                    turret_change = 1
                elif event.key == pygame.K_DOWN:
                    turret_change = -1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    fireShell(gun, tank_x, tank_y, turret_position)
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   tank_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    turret_change = 0
                
        tank_x += tank_move
        turret_position += turret_change

        if turret_position > 5:
            turret_position = 5
        elif turret_position < 0:
            turret_position = 0

        if tank_x - (tank_width / 2)< barrier_x + barrier_width:
            tank_x += 5
        elif tank_x + (tank_width / 2) > display_width:
            tank_x -= 5
                    
        barrier(barrier_x, barrier_height)
        
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

#########END of FUNCTIONS##########
#Start game.
gameIntro()
