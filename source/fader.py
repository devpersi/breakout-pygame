import pygame as pg

def fade(screen, image, fade_duration):
    fade_frames = fade_duration * 60
    fade_speed = max(1, 255 / fade_frames) # Ensure the step is at least 1
    
    # Create a copy of the image to modify its alpha value
    faded_image = image.copy()

    # Fade in
    for alpha in range(0, 256, int(fade_speed)):
        faded_image.set_alpha(alpha)
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(faded_image, (0, 0))  # Draw the faded image onto the screen
        pg.display.flip()  # Update the display
        pg.time.Clock().tick(60)  # Cap the frame rate at 60 FPS

    # Ensure the image is fully opaque
    faded_image.set_alpha(255)

    # Fade out
    for alpha in range(255, -1, -int(fade_speed)):
        faded_image.set_alpha(alpha)
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(faded_image, (0, 0))  # Draw the faded image onto the screen
        pg.display.flip()  # Update the display
        pg.time.Clock().tick(60)  # Cap the frame rate at 60 FPS

