import random

# General settings
SCREEN_SIZE = 1280, 720 # '''width, height'''
SCREEN_BACKGROUND_COLOUR = 52, 78, 91
FPS = 60

# Ball settings
COLLISION_THRESHOLD = 5
BALL_RADIUS = 10
BALL_SIZE = int(BALL_RADIUS*2**0.5)
BALL_COLOUR = 0, 0 , 0 # Black ball
BALL_SPEED = 4 # 4 pixels per frame
BALL_HOME_SPAWN_LOCATION = random.randint(2*BALL_SIZE, SCREEN_SIZE[0] - 2*BALL_SIZE), (SCREEN_SIZE[1] - BALL_SIZE)*0.5

# Brick settings
BRICK_COLUMNS = 10
BRICK_ROWS = 6
BRICK_ROWS_TIMES_COLUMNS = BRICK_COLUMNS * BRICK_ROWS
BRICK_SIZE = SCREEN_SIZE[0] // BRICK_COLUMNS, SCREEN_SIZE[1]*0.3 // BRICK_ROWS # '''width, height'''
BRICK_RED = 242, 85, 96
BRICK_GREEN = 86, 174, 87
BRICK_BLUE = 69, 177, 232

# Paddle settings
PADDLE_SIZE = 180, 30 # '''width, height'''
RED_PADDLE_COLOUR = 255, 0, 0 # Red paddles
BLUE_PADDLE_COLOUR = 0, 0, 255 # Blue paddles
PADDLE_SPEED = 5
PADDLE_HOME_SPAWN_LOCATION = ((SCREEN_SIZE[0] - PADDLE_SIZE[0])*0.5, SCREEN_SIZE[1]*0.95) # Middle bottom of the screen
FRIENDLY_FIRE = True
COOP = False
