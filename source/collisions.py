#.\source\collisions.py
"""
Module: collisions

This module provides functions to handle collision detection and response in a game environment using Pygame.

Functions:
- collision(direction_x: int, direction_y: int, ball: pg.Rect, other: pg.Rect, threshold: int) -> tuple[int, int]:
  Detects collision between two rectangular objects and calculates the resulting direction of movement for a ball bouncing off the other object.
"""

import pygame as pg
from settings import COLLISION_THRESHOLD

def collision(direction_x: int, direction_y: int, ball: pg.Rect, other: pg.Rect, threshold: int) -> tuple[int, int]:
    """
    Detects collision between two rectangular objects and calculates the resulting direction of movement for a ball bouncing off the other object.

    Parameters:
    - direction_x (int): The x-direction of the ball's movement (-1 for left, 1 for right).
    - direction_y (int): The y-direction of the ball's movement (-1 for up, 1 for down).
    - ball (pygame.Rect): The rectangular bounding box representing the ball.
    - other (pygame.Rect): The rectangular bounding box representing the other object.
    - threshold (int): The threshold value used to determine if the collision is nearly equal along both axes.

    Returns:
    - tuple[int, int]: The updated direction of movement for the ball as a tuple containing the new x-direction and y-direction.
    """    
    # Calculate the overlap distances between the ball and the other object
    overlap_x = ball.right - other.left if direction_x > 0 else other.right - ball.left
    overlap_y = ball.bottom - other.top if direction_y > 0 else other.bottom - ball.top
    
    # Determine the axis of minimum overlap
    if abs(overlap_x - overlap_y) < COLLISION_THRESHOLD:
        # If overlaps are approximately equal, reverse both directions
        direction_x = -direction_x
        direction_y = -direction_y
    elif overlap_x > overlap_y:
        # If x-axis overlap is greater, reverse y-direction
        direction_y = -direction_y
    else:
        # If y-axis overlap is greater, reverse x-direction
        direction_x = -direction_x
        
    return direction_x, direction_y
    