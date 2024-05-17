#.\source\settings.py
"""
Settings module for the game.

This module contains various settings used throughout the game, including settings for the screen, ball, bricks, and paddle.

Attributes:
    SCREEN_WIDTH (int): Width size of the game screen in pixels.
    SCREEN_HEIGHT(int): Height size of the game screen in pixels.
    SCREEN_SIZE (tuple[int, int]): The size of the game screen in pixels, specified as (width, height).
    SCREEN_BACKGROUND_COLOUR (tuple[int, int, int]): The RGB colour tuple representing the background colour of the screen.
    FPS (int): The frames per second at which the game runs.
    
    COLLISION_THRESHOLD (int): The threshold for collision detection between objects in the game.
    
    BALL_RADIUS (int): The radius of the ball in pixels.
    BALL_SIZE (int): The diameter of the ball calculated from its radius.
    BALL_COLOUR (tuple[int, int, int]): The RGB colour tuple representing the colour of the ball.
    BALL_SPEED (int): The speed of the ball in pixels per frame.
    BALL_HOME_SPAWN_LOCATION (tuple[int, int]): The initial spawn location of the ball on the screen, specified as (x, y) coordinates.
    ball_count (int): The number of balls
    
    BRICK_COLUMNS (int): The number of columns of bricks in the game.
    BRICK_ROWS (int): The number of rows of bricks in the game.
    BRICK_ROWS_TIMES_COLUMNS (int): The total number of bricks in the game grid.
    BRICK_SIZE (tuple): The size of each brick in pixels, specified as (width, height).
    BRICK_RED (tuple[int, int, int]): The RGB colour tuple representing the colour of red bricks.
    BRICK_GREEN (tuple[int, int, int]): The RGB colour tuple representing the colour of green bricks.
    BRICK_BLUE (tuple[int, int, int]): The RGB colour tuple representing the colour of blue bricks.
    
    COOP (bool): A flag indicating whether cooperative mode is enabled.
    FRIENDLY_FIRE (bool): A flag indicating whether paddles blocking each other is enabled.
    
    PADDLE_SIZE (tuple): The size of the paddle in pixels, specified as (width, height).
    RED_PADDLE_COLOUR (tuple[int, int, int]): The RGB colour tuple representing the colour of red paddles.
    BLUE_PADDLE_COLOUR (tuple[int, int, int]): The RGB colour tuple representing the colour of blue paddles.
    PADDLE_SPEED (int): The speed of the paddle in pixels per frame.
    PADDLE_HOME_SPAWN_LOCATION (tuple[int, int]): The initial spawn location of the paddle on the screen, specified as (x, y) coordinates.
"""

import random

# General settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_BACKGROUND_COLOUR = 52, 78, 91
FPS = 60

# Ball settings
COLLISION_THRESHOLD = 5
BALL_RADIUS = 10
BALL_SIZE = int(BALL_RADIUS*2**0.5)
BALL_COLOUR = 0, 0, 0 # Black ball
BALL_SPEED = 2 # 2 pixels per frame
BALL_HOME_SPAWN_LOCATION = random.randint(2*BALL_SIZE, SCREEN_WIDTH - 2*BALL_SIZE), (SCREEN_HEIGHT - BALL_SIZE)*0.5
ball_count = 5

# Brick settings
BRICK_COLUMNS = 10
BRICK_ROWS = 6
BRICK_ROWS_TIMES_COLUMNS = BRICK_COLUMNS * BRICK_ROWS
BRICK_SIZE = SCREEN_WIDTH // BRICK_COLUMNS, SCREEN_HEIGHT*0.3 // BRICK_ROWS # '''width, height'''
BRICK_RED = 242, 85, 96
BRICK_GREEN = 86, 174, 87
BRICK_BLUE = 69, 177, 232

# Paddle settings
COOP = True
FRIENDLY_FIRE = True

PADDLE_SIZE = 180, 30 # '''width, height'''
RED_PADDLE_COLOUR = 255, 0, 0 # Red paddles
BLUE_PADDLE_COLOUR = 0, 0, 255 # Blue paddles
PADDLE_SPEED = 5
PADDLE_HOME_SPAWN_LOCATION = ((SCREEN_WIDTH - PADDLE_SIZE[0])*0.5, SCREEN_HEIGHT*0.95) # Middle bottom of the screen

lives = 3