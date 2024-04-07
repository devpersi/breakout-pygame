import pygame as pg

# Create game window
pg.init()
SCREEN_SIZE: tuple = 1280, 720 # '''width, height'''
SCREEN_BACKGROUND_COLOUR: tuple = 52, 78, 91
FPS: int = 60

screen : pg.surface.Surface = pg.display.set_mode(SCREEN_SIZE)

# Declare bricks 
BRICK_SIZE: int = 32, 13 # '''width, height'''
BRICK_COLOUR: tuple = 0, 0, 255 # Blue bricks
BRICK_HOME_SPAWN_LOCATION: tuple = ((SCREEN_SIZE[0] - BRICK_SIZE[0])*0.5, (SCREEN_SIZE[1] - BRICK_SIZE[1])*0.5) # Middle of the screen

# Create brick
brick : pg.rect.Rect = pg.Rect(BRICK_HOME_SPAWN_LOCATION, BRICK_SIZE)

# Declare paddles
PADDLE_SIZE: tuple = 180, 30 # '''width, height'''
RED_PADDLE_COLOUR: tuple = 255, 0, 0 # Red paddles
BLUE_PADDLE_COLOUR: tuple = 0, 0, 255 # Blue paddles
PADLE_SPEED: int = 5
PADDLE_HOME_SPAWN_LOCATION: tuple = ((SCREEN_SIZE[0] - PADDLE_SIZE[0])*0.5, SCREEN_SIZE[1]*0.95) # Middle bottom of the screen
FRIENDLY_FIRE: bool = True

# Create paddles
p1_paddle : pg.rect.Rect = pg.Rect(PADDLE_HOME_SPAWN_LOCATION, PADDLE_SIZE)
p2_paddle : pg.rect.Rect = pg.Rect(PADDLE_HOME_SPAWN_LOCATION, PADDLE_SIZE)

# Create game loop
clock : pg.time.Clock = pg.time.Clock()

while True:
    # Exit when game is closed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    # Clear the screen
    screen.fill(SCREEN_BACKGROUND_COLOUR)
    
    # Spawn brick
    pg.draw.rect(screen, BRICK_COLOUR, brick)
    
    # Spawn paddles
    pg.draw.rect(screen, RED_PADDLE_COLOUR, p1_paddle)
    pg.draw.rect(screen, BLUE_PADDLE_COLOUR, p2_paddle)

    # p1 controls
    keyboard_press = pg.key.get_pressed()
    
    paddles_not_currently_touching: bool = p1_paddle.right < p2_paddle.left and FRIENDLY_FIRE
    
    if keyboard_press[pg.K_a] and p1_paddle.left > 0:
        p1_paddle.move_ip(-PADLE_SPEED, 0) # PADLE_SPEED pixels to the left, 0 pixels to the bottom/top
    elif keyboard_press[pg.K_d] and p1_paddle.right < SCREEN_SIZE[0] and paddles_not_currently_touching:
        p1_paddle.move_ip(PADLE_SPEED, 0) # PADLE_SPEED pixels to the right, 0 pixels to the bottom/top
    #elif keyboard_press[pg.K_w]:
    #    red_paddle.move_ip(0, -1) # 0 pixels to the right/left, 1 pixel to the top
    #elif keyboard_press[pg.K_s]:
    #    red_paddle.move_ip(0, 1) # 0 pixel to the left/right, 1 pixel to the bottom
        
    coop = True
    if coop:
        # p2 controls
        keyboard_press = pg.key.get_pressed()
        if keyboard_press[pg.K_KP4] and p2_paddle.left > 0 and paddles_not_currently_touching:
            p2_paddle.move_ip(-PADLE_SPEED, 0) # PADLE_SPEED pixels, 0 pixels to the bottom/top
        elif keyboard_press[pg.K_KP6] and p2_paddle.right < SCREEN_SIZE[0]:
            p2_paddle.move_ip(PADLE_SPEED, 0) # PADLE_SPEED pixels, 0 pixels to the bottom/top
        #elif keyboard_press[pg.K_w]:
        #    red_paddle.move_ip(0, -1) # 0 pixels to the right/left, 1 pixel to the top
        #elif keyboard_press[pg.K_s]:
        #    red_paddle.move_ip(0, 1) # 0 pixel to the left/right, 1 pixel to the bottom
        

    pg.display.update()
    clock.tick(FPS)