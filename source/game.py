#.\source\game.py
"""
This script is a simple game using Pygame. It simulates a brick-breaking game where the player controls one or two paddles to bounce balls into bricks to destroy them. The script initializes the game environment, including creating balls, bricks, and paddles, and defines the main gameplay loop.

Controls:
- Player 1 (Single Player or Cooperative mode):
  - A: Move paddle left
  - D: Move paddle right

- Player 2 (Cooperative mode only):
  - NumPad 4: Move paddle left
  - NumPad 6: Move paddle right
"""

import pygame as pg
import random
import settings
import breakoutMenu
from game_over import game_over
from text_funcs import text_current
from inits import red_paddle_img, orange_paddle_img, red_brick_img, green_brick_img, blue_brick_img, ball_img, p2p_font_current
from collisions import collision

def loop(screen : pg.Surface) -> None:
    """Main gameplay loop"""    
    clock = pg.time.Clock()

    # Create balls
    ball_direction_x = [random.uniform(-2, -1) for i in range(settings.ball_count)]
    ball_direction_y = [random.uniform(1, 2) for i in range(settings.ball_count)]
    balls = [pg.Rect(settings.BALL_HOME_SPAWN_LOCATION, (settings.BALL_SIZE, settings.BALL_SIZE)) for i in range(settings.ball_count)]

    # Create bricks
    brick_list = [pg.Rect(settings.BRICK_SIZE[0] * w, settings.BRICK_SIZE[1] * h, settings.BRICK_SIZE[0], settings.BRICK_SIZE[1]) 
                                        for h in range (settings.BRICK_ROWS) for w in range(settings.BRICK_COLUMNS)]

    # Filter bricks by colour
    red_brick_list = list(brick_list[:settings.BRICK_ROWS_TIMES_COLUMNS // 3])
    green_brick_list = list(brick_list[settings.BRICK_ROWS_TIMES_COLUMNS // 3:settings.BRICK_ROWS_TIMES_COLUMNS // 3 * 2])
    blue_brick_list = list(brick_list[settings.BRICK_ROWS_TIMES_COLUMNS // 3 * 2:])

    # Create paddles
    p1_paddle = pg.Rect(settings.PADDLE_HOME_SPAWN_LOCATION, settings.PADDLE_SIZE)
    if settings.COOP:
        p2_paddle = pg.Rect(settings.PADDLE_HOME_SPAWN_LOCATION, settings.PADDLE_SIZE)

    while True:
        # Exit when game is closed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                
                
        # Clear the screen
        screen.fill(settings.SCREEN_BACKGROUND_COLOUR)
        
        text_current(screen, "Lives: " + str(settings.lives), p2p_font_current, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        
        # Spawn ball
        for ball in balls:
            screen.blit(ball_img, ball)

        # Spawn brick
        [screen.blit(red_brick_img, brick) for brick in red_brick_list]
        [screen.blit(green_brick_img, brick) for brick in green_brick_list]
        [screen.blit(blue_brick_img, brick) for brick in blue_brick_list]
        
        # Spawn paddles
        screen.blit(red_paddle_img, p1_paddle)
        
        if settings.COOP:
            screen.blit(orange_paddle_img, p2_paddle)
        
        for i,ball in enumerate(balls):
            # Move the ball
            ball.x += settings.BALL_SPEED * ball_direction_x[i]
            ball.y += settings.BALL_SPEED * ball_direction_y[i]
            
            # Reset when hitting the bottom
            if ball.centery > settings.SCREEN_HEIGHT - settings.BALL_RADIUS:
                if settings.lives > 0:
                    settings.lives -= 1
                else:
                    game_over(screen)
                    
                ball.x = random.randint(2*settings.BALL_SIZE, settings.SCREEN_WIDTH - 2*settings.BALL_SIZE)
                ball.y = settings.BALL_HOME_SPAWN_LOCATION[1]
                ball_direction_x[i] = random.choice([random.uniform(1, 2), random.uniform(-2, -1)])
                ball_direction_y[i] = random.choice([random.uniform(1, 2), random.uniform(-2, -1)])
            
            # Reflect the ball when it reaches a side wall
            if ball.centerx < settings.BALL_RADIUS or ball.centerx > settings.SCREEN_WIDTH - settings.BALL_RADIUS:
                ball_direction_x[i] = -ball_direction_x[i]
            
            # same for the top
            if ball.centery < settings.BALL_RADIUS:
                ball_direction_y[i] = -ball_direction_y[i]
                
            # same for paddle collision
            if ball.colliderect(p1_paddle) and ball_direction_y[i] > 0:
                ball_direction_x[i], ball_direction_y[i] = collision(ball_direction_x[i], ball_direction_y[i], ball, p1_paddle, settings.COLLISION_THRESHOLD)
                
            if settings.COOP:
                if ball.colliderect(p2_paddle) and ball_direction_y[i] > 0:
                    ball_direction_x[i], ball_direction_y[i] = collision(ball_direction_x[i], ball_direction_y[i], ball, p2_paddle, settings.COLLISION_THRESHOLD)

            # same for brick collision
            brick_index = ball.collidelist(blue_brick_list)
            if brick_index != -1:
                brick = blue_brick_list.pop(brick_index)
                ball_direction_x[i], ball_direction_y[i] = collision(ball_direction_x[i], ball_direction_y[i], ball, brick, settings.COLLISION_THRESHOLD)
            
            brick_index = ball.collidelist(green_brick_list)
            if brick_index != -1:
                brick = green_brick_list.pop(brick_index)
                ball_direction_x[i], ball_direction_y[i] = collision(ball_direction_x[i], ball_direction_y[i], ball, brick, settings.COLLISION_THRESHOLD)
            
            brick_index = ball.collidelist(red_brick_list)
            if brick_index != -1:
                brick = red_brick_list.pop(brick_index)
                ball_direction_x[i], ball_direction_y[i] = collision(ball_direction_x[i], ball_direction_y[i], ball, brick, settings.COLLISION_THRESHOLD)
        
        # respawn bricks if they are all broken
        if not (red_brick_list or green_brick_list or blue_brick_list):
            red_brick_list = list(brick_list[:settings.BRICK_ROWS_TIMES_COLUMNS // 3])
            green_brick_list = list(brick_list[settings.BRICK_ROWS_TIMES_COLUMNS // 3:settings.BRICK_ROWS_TIMES_COLUMNS // 3 * 2])
            blue_brick_list = list(brick_list[settings.BRICK_ROWS_TIMES_COLUMNS // 3 * 2:])
        
        # p1 controls
        keyboard_press = pg.key.get_pressed()
        
        paddles_not_currently_touching: bool = p1_paddle.right < p2_paddle.left and settings.FRIENDLY_FIRE if settings.COOP else True
        
        if keyboard_press[pg.K_a] and p1_paddle.left > 0:
            p1_paddle.move_ip(-settings.PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the left, 0 pixels to the bottom/top
        elif keyboard_press[pg.K_d] and p1_paddle.right < settings.SCREEN_WIDTH and paddles_not_currently_touching:
            p1_paddle.move_ip(settings.PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the right, 0 pixels to the bottom/top
            
        if settings.COOP:
            # p2 controls
            keyboard_press = pg.key.get_pressed()
            if keyboard_press[pg.K_KP4] and p2_paddle.left > 0 and paddles_not_currently_touching:
                p2_paddle.move_ip(-settings.PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the left, 0 pixels to the bottom/top
            elif keyboard_press[pg.K_KP6] and p2_paddle.right < settings.SCREEN_WIDTH:
                p2_paddle.move_ip(settings.PADDLE_SPEED, 0) # PADDLE_SPEED pixels to the right, 0 pixels to the bottom/top
        
        if keyboard_press[pg.K_ESCAPE]:
            breakoutMenu.loop(screen)
        
        pg.display.update()
        clock.tick(settings.FPS)