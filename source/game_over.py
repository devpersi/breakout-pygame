import pygame as pg
import settings
import breakoutMenu
import text_funcs
from menu_settings import fade_time
from inits import p2p_font_current
from fader import fade

def game_over(screen):
    splash = pg.image.load("images/game/game_over.png")
    splash = pg.transform.scale(splash, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    text_funcs.text_current(screen, "Score: " + str(0), p2p_font_current, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    fade(screen, splash, fade_time)
    breakoutMenu.loop(screen)