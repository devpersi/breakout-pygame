import pygame as pg

def collision(direction_x: int, direction_y: int, ball: pg.Rect, other: pg.Rect, threshold: int) -> tuple[int, int]:
    if direction_x > 0:
        delta_x = ball.right - other.left
    else:
        delta_x = other.right - ball.left
    if direction_y > 0:
        delta_y = ball.bottom - other.top
    else:
        delta_y = other.bottom - ball.top
        
    if abs(delta_x - delta_y) < threshold:
        direction_x = -direction_x
        direction_y = -direction_y
    elif delta_x > delta_y:
        direction_y = -direction_y
    else:
        direction_x = -direction_x
    return direction_x, direction_y
    