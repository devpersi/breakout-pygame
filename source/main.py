from pygame import init, display
import game
from settings import SCREEN_SIZE

# Create game window
init()
sc = display.set_mode(SCREEN_SIZE)
# Create game loop
game.loop(sc)