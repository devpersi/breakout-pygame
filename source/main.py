import pygame as pg
import random

# Create game window
pg.init()
SCREEN_SIZE: tuple[int, int] = 1280, 720 # '''width, height'''
SCREEN_BACKGROUND_COLOUR: tuple[int, int, int] = 52, 78, 91
FPS: int = 60

screen : pg.surface.Surface = pg.display.set_mode(SCREEN_SIZE)

# Declare balls
BALL_RADIUS: int = 10
BALL_SIZE: int = int(BALL_RADIUS*2**0.5)
BALL_COLOUR : tuple[int,int,int] = 0, 0 , 0 # Black ball
BALL_SPEED: int = 4 # 4 pixels per frame
BALL_VELOCITY_X: int = 1
BALL_VELOCITY_Y: int = -1
BALL_HOME_SPAWN_LOCATION : tuple[int, int] = random.randint(2*BALL_SIZE, SCREEN_SIZE[0] - 2*BALL_SIZE), (SCREEN_SIZE[1] - BALL_SIZE)*0.5

# Create balls
ball = pg.Rect(BALL_HOME_SPAWN_LOCATION, (BALL_SIZE, BALL_SIZE))

# Declare bricks 
BRICK_COLUMNS: int = 10
BRICK_ROWS: int = 6
BRICK_ROWS_TIMES_COLUMNS: int = BRICK_COLUMNS * BRICK_ROWS
BRICK_SIZE: int = SCREEN_SIZE[0] // BRICK_COLUMNS, SCREEN_SIZE[1]*0.3 // BRICK_ROWS # '''width, height'''
BRICK_RED: tuple[int,int,int] = 242, 85, 96
BRICK_GREEN: tuple[int,int,int] = 86, 174, 87
BRICK_BLUE: tuple[int,int,int] = 69, 177, 232

# Create bricks
brick_list : tuple[pg.rect.Rect, int] = [pg.Rect(BRICK_SIZE[0] * w, BRICK_SIZE[1] * h, BRICK_SIZE[0], BRICK_SIZE[1]) 
                                    for h in range (BRICK_ROWS) for w in range(BRICK_COLUMNS)]

# Filter bricks by colour
red_brick_list = list(brick_list[:BRICK_ROWS_TIMES_COLUMNS // 3])
green_brick_list = list(brick_list[BRICK_ROWS_TIMES_COLUMNS // 3:BRICK_ROWS_TIMES_COLUMNS // 3 * 2])
blue_brick_list = list(brick_list[BRICK_ROWS_TIMES_COLUMNS // 3 * 2:])

# Declare paddles
PADDLE_SIZE: tuple[int,int] = 180, 30 # '''width, height'''
RED_PADDLE_COLOUR: tuple[int,int,int] = 255, 0, 0 # Red paddles
BLUE_PADDLE_COLOUR: tuple[int,int,int] = 0, 0, 255 # Blue paddles
PADDLE_SPEED: int = 5
PADDLE_HOME_SPAWN_LOCATION: tuple[int,int] = ((SCREEN_SIZE[0] - PADDLE_SIZE[0])*0.5, SCREEN_SIZE[1]*0.95) # Middle bottom of the screen
FRIENDLY_FIRE: bool = True

# Create paddles
COOP: bool = False
p1_paddle : pg.rect.Rect = pg.Rect(PADDLE_HOME_SPAWN_LOCATION, PADDLE_SIZE)
if COOP:
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
    
    # Spawn ball
    pg.draw.circle(screen, BALL_COLOUR, ball.center, BALL_RADIUS)
    # Move the ball
    ball.x += BALL_SPEED * BALL_VELOCITY_X
    ball.y += BALL_SPEED * BALL_VELOCITY_Y
    
    # Reset when hitting the bottom
    if ball.centery > SCREEN_SIZE[1] - BALL_RADIUS:
        ball.x = random.randint(2*BALL_SIZE, SCREEN_SIZE[0] - 2*BALL_SIZE)
        ball.y = BALL_HOME_SPAWN_LOCATION[1]
        BALL_VELOCITY_X = random.choice([1, -1])
        BALL_VELOCITY_Y = random.choice([1, -1])
        
    # Reflect the ball when it reaches a side wall
    if ball.centerx < BALL_RADIUS or ball.centerx > SCREEN_SIZE[0] - BALL_RADIUS:
        BALL_VELOCITY_X = -BALL_VELOCITY_X
    
    # same for the top
    if ball.centery < BALL_RADIUS:
        BALL_VELOCITY_Y = -BALL_VELOCITY_Y
        
    # same for paddle collision
    if ball.colliderect(p1_paddle) and BALL_VELOCITY_Y > 0:
        BALL_VELOCITY_Y = -BALL_VELOCITY_Y
        
    if COOP:
        if ball.colliderect(p2_paddle) and BALL_VELOCITY_Y > 0:
            BALL_VELOCITY_Y = -BALL_VELOCITY_Y

    
    # same for brick collision
    for brick in blue_brick_list:
        if ball.colliderect(brick):
            if ball.bottom - BALL_SPEED * BALL_VELOCITY_Y < brick.top or ball.top - BALL_SPEED * BALL_VELOCITY_Y > brick.bottom:
                BALL_VELOCITY_Y = -BALL_VELOCITY_Y
                blue_brick_list.remove(brick)
                break
            if ball.right - BALL_SPEED * BALL_VELOCITY_X < brick.left or ball.left - BALL_SPEED * BALL_VELOCITY_X > brick.right:
                BALL_VELOCITY_X = -BALL_VELOCITY_X
                blue_brick_list.remove(brick)
                break
            
    for brick in green_brick_list:
        if ball.colliderect(brick):
            if ball.bottom - BALL_SPEED * BALL_VELOCITY_Y < brick.top or ball.top - BALL_SPEED * BALL_VELOCITY_Y > brick.bottom:
                BALL_VELOCITY_Y = -BALL_VELOCITY_Y
                green_brick_list.remove(brick)
                break
            if ball.right - BALL_SPEED * BALL_VELOCITY_X < brick.left or ball.left - BALL_SPEED * BALL_VELOCITY_X > brick.right:
                BALL_VELOCITY_X = -BALL_VELOCITY_X
                green_brick_list.remove(brick)
                break
    
    for brick in red_brick_list:
        if ball.colliderect(brick):
            if ball.bottom - BALL_SPEED * BALL_VELOCITY_Y < brick.top or ball.top - BALL_SPEED * BALL_VELOCITY_Y > brick.bottom:
                BALL_VELOCITY_Y = -BALL_VELOCITY_Y
                red_brick_list.remove(brick)
                break
            if ball.right - BALL_SPEED * BALL_VELOCITY_X < brick.left or ball.left - BALL_SPEED * BALL_VELOCITY_X > brick.right:
                BALL_VELOCITY_X = -BALL_VELOCITY_X
                red_brick_list.remove(brick)
                break
    
    # Spawn brick
    [pg.draw.rect(screen, BRICK_RED, brick) for brick in red_brick_list]
    [pg.draw.rect(screen, BRICK_GREEN, brick) for brick in green_brick_list]
    [pg.draw.rect(screen, BRICK_BLUE, brick) for brick in blue_brick_list]
    
    # Spawn paddles
    pg.draw.rect(screen, RED_PADDLE_COLOUR, p1_paddle)
    
    if COOP:
        pg.draw.rect(screen, BLUE_PADDLE_COLOUR, p2_paddle)

    # p1 controls
    keyboard_press = pg.key.get_pressed()
    
    paddles_not_currently_touching: bool = p1_paddle.right < p2_paddle.left and FRIENDLY_FIRE if COOP else True
    
    if keyboard_press[pg.K_a] and p1_paddle.left > 0:
        p1_paddle.move_ip(-PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the left, 0 pixels to the bottom/top
    elif keyboard_press[pg.K_d] and p1_paddle.right < SCREEN_SIZE[0] and paddles_not_currently_touching:
        p1_paddle.move_ip(PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the right, 0 pixels to the bottom/top
    #elif keyboard_press[pg.K_w]:
    #    red_paddle.move_ip(0, -1) # 0 pixels to the right/left, 1 pixel to the top
    #elif keyboard_press[pg.K_s]:
    #    red_paddle.move_ip(0, 1) # 0 pixel to the left/right, 1 pixel to the bottom
        
    if COOP:
        # p2 controls
        keyboard_press = pg.key.get_pressed()
        if keyboard_press[pg.K_KP4] and p2_paddle.left > 0 and paddles_not_currently_touching:
            p2_paddle.move_ip(-PADDLE_SPEED, 0) # PADDLE_SPEED pixels, 0 pixels to the bottom/top
        elif keyboard_press[pg.K_KP6] and p2_paddle.right < SCREEN_SIZE[0]:
            p2_paddle.move_ip(PADDLE_SPEED, 0) # PADDLE_SPEED pixels, 0 pixels to the bottom/top
        #elif keyboard_press[pg.K_w]:
        #    red_paddle.move_ip(0, -1) # 0 pixels to the right/left, 1 pixel to the top
        #elif keyboard_press[pg.K_s]:
        #    red_paddle.move_ip(0, 1) # 0 pixel to the left/right, 1 pixel to the bottom
        

    pg.display.update()
    clock.tick(FPS)