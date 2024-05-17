from pygame import init, display, mixer
import breakoutMenu
from settings import SCREEN_SIZE

# Create game window
init()
display.set_caption('Breakout Game')
sc = display.set_mode(SCREEN_SIZE)
mixer.music.load('audio/music1.mp3')
mixer.music.play(-1)

# Create game loop
breakoutMenu.loop(sc)