import pygame as pg
from sys import exit
import inits
import menu_settings
import settings
from fader import fade
from text_funcs import text, text_current
import game


def loop(screen):
	inits.scale_menu(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    
	splash = pg.image.load("images/splash.png")
	splash = pg.transform.scale(splash, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
	fade(screen, splash, menu_settings.fade_time)

	while True:
		if menu_settings.menu_state == "main":
			screen.blit(inits.BG_LARGE, (0, 0)) if menu_settings.size == "large" else screen.blit(inits.BG_MEDIUM, (0, 0)) if menu_settings.size == "medium" else screen.blit(inits.BG_SMALL, (0, 0))
			if menu_settings.size == "large":
				screen.blit(inits.TITLE_LARGE, (settings.SCREEN_WIDTH / 2 - inits.TITLE_LARGE.get_width() / 2 + settings.SCREEN_WIDTH / 256, settings.SCREEN_HEIGHT / (720 / 204) / 2 - inits.TITLE_LARGE.get_height() / 2 + settings.SCREEN_HEIGHT / 90))
			elif menu_settings.size == "medium":
				screen.blit(inits.TITLE_MEDIUM, (settings.SCREEN_WIDTH / 2 - inits.TITLE_MEDIUM.get_width() / 2 + settings.SCREEN_WIDTH / 256, settings.SCREEN_HEIGHT / (720 / 204) / 2 - inits.TITLE_MEDIUM.get_height() / 2 + settings.SCREEN_HEIGHT / 90))
			else:
				screen.blit(inits.TITLE_SMALL, (settings.SCREEN_WIDTH / 2 - inits.TITLE_SMALL.get_width() / 2 + settings.SCREEN_WIDTH / 256, settings.SCREEN_HEIGHT / (720 / 204) / 2 - inits.TITLE_SMALL.get_height() / 2 + settings.SCREEN_HEIGHT / 90))
			if inits.play_solo_button.draw(screen):
				settings.COOP = False
				game.loop(screen)
				print('PLAY SOLO')
			if inits.play_coop_button.draw(screen):
				settings.COOP = True
				game.loop(screen)
				print('PLAY CO-OP')
			if inits.options_button.draw(screen):
				menu_settings.menu_state = "options"
			if inits.exit_button.draw(screen):
				pg.quit()
				exit()
		else:
			screen.blit(inits.BG_BLUR_LARGE, (0, 0)) if menu_settings.size == "large" else screen.blit(inits.BG_BLUR_MEDIUM, (0, 0)) if menu_settings.size == "medium" else screen.blit(inits.BG_BLUR_SMALL, (0, 0))
	
		if menu_settings.menu_state == "options":
			text(screen, "OPTIONS", inits.p2p_font, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
			if inits.back_button.draw(screen):
				menu_settings.menu_state = "main"
			if inits.video_button.draw(screen):
				menu_settings.menu_state = "video"
			if inits.audio_button.draw(screen):
				menu_settings.menu_state = "audio"
			if inits.mode_button.draw(screen):
				menu_settings.menu_state = "mode"

		if menu_settings.menu_state == "video":
			text(screen, "VIDEO", inits.p2p_font, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
			text_current(screen, f"Current: {settings.SCREEN_WIDTH} x {settings.SCREEN_HEIGHT}", inits.p2p_font_current, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

			if inits.back_button.draw(screen):
				menu_settings.menu_state = "options"

			if inits.small_button.draw(screen):
				menu_settings.size = "small"
				settings.SCREEN_WIDTH = 800
				settings.SCREEN_HEIGHT = 450
				screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
				inits.scale_menu(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

			if inits.medium_button.draw(screen):
				menu_settings.size = "medium"
				settings.SCREEN_WIDTH = 1024
				settings.SCREEN_HEIGHT = 576
				screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
				inits.scale_menu(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

			if inits.large_button.draw(screen):
				menu_settings.size = "large"
				settings.SCREEN_WIDTH = 1280
				settings.SCREEN_HEIGHT = 720
				screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
				inits.scale_menu(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

		if menu_settings.menu_state == "audio":
			text(screen, "AUDIO", inits.p2p_font, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
			if inits.back_button.draw(screen):
				menu_settings.menu_state = "options"
			if not menu_settings.mute_music:
				if inits.music_button.draw(screen):
					print("Music Muted")
					pg.mixer.music.set_volume(0)
					menu_settings.mute_music = True
			else:
				if inits.music_muted_button.draw(screen):
					print("Music Unmuted")
					pg.mixer.music.set_volume(0.5)
					menu_settings.mute_music = False
			if not menu_settings.mute_sfx:
				if inits.sound_button.draw(screen):
					print("Sound Muted")
					menu_settings.mute_sfx = True
			else:
				if inits.sound_muted_button.draw(screen):
					print("Sound Unmuted")
					menu_settings.mute_sfx = False

		if menu_settings.menu_state == "mode":
			text(screen, "MODE", inits.p2p_font, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
			if inits.back_button.draw(screen):
				menu_settings.menu_state = "options"
			if inits.keyboard_mode_button.draw(screen):
				menu_settings.input_mode = "Keyboard"
			if inits.mouse_mode_button.draw(screen):
				menu_settings.input_mode = "Mouse"
			text_current(screen, f"Current: {menu_settings.input_mode}", inits.p2p_font_current, (255, 255, 255), settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()

		pg.display.update()