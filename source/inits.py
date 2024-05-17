import pygame
from button import Button

pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

p2p_font = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", int(SCREEN_WIDTH / (1280 / 38)))
p2p_font_current = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", int(SCREEN_WIDTH / (1280 / 20)))

# menu images
BG_SMALL = pygame.image.load("images/bg.png")
BG_MEDIUM = pygame.image.load("images/bg.png")
BG_LARGE = pygame.image.load("images/bg.png")

TITLE_SMALL = pygame.image.load('images/title.png')
TITLE_MEDIUM = pygame.image.load('images/title.png')
TITLE_LARGE = pygame.image.load('images/title.png')

BG_BLUR_SMALL = pygame.image.load("images/bg_blur.png")
BG_BLUR_MEDIUM = pygame.image.load("images/bg_blur.png")
BG_BLUR_LARGE = pygame.image.load("images/bg_blur.png")

play_solo_img = pygame.image.load('images/mainMenu/play_solo.png')
play_coop_img = pygame.image.load('images/mainMenu/play_coop.png')
options_img = pygame.image.load('images/mainMenu/options.png')
exit_img = pygame.image.load('images/mainMenu/exit.png')

play_solo_img_highlighted = pygame.image.load('images/mainMenu/play_solo_highlighted.png')
play_coop_img_highlighted = pygame.image.load('images/mainMenu/play_coop_highlighted.png')
options_img_highlighted = pygame.image.load('images/mainMenu/options_highlighted.png')
exit_img_highlighted = pygame.image.load('images/mainMenu/exit_highlighted.png')

video_img = pygame.image.load('images/options/video.png')
audio_img = pygame.image.load('images/options/audio.png')
mode_img = pygame.image.load('images/options/mode.png')

video_img_highlighted = pygame.image.load('images/options/video_highlighted.png')
audio_img_highlighted = pygame.image.load('images/options/audio_highlighted.png')
mode_img_highlighted = pygame.image.load('images/options/mode_highlighted.png')

small_img = pygame.image.load('images/video/800x450.png')
medium_img = pygame.image.load('images/video/1024x576.png')
large_img = pygame.image.load('images/video/1280x720.png')

small_img_highlighted = pygame.image.load('images/video/800x450_highlighted.png')
medium_img_highlighted = pygame.image.load('images/video/1024x576_highlighted.png')
large_img_highlighted = pygame.image.load('images/video/1280x720_highlighted.png')

music_img = pygame.image.load('images/audio/music.png')
music_muted_img = pygame.image.load('images/audio/music_muted.png')

sound_img = pygame.image.load('images/audio/sound.png')
sound_muted_img = pygame.image.load('images/audio/sound_muted.png')

music_img_highlighted = pygame.image.load('images/audio/music_highlighted.png')
sound_img_highlighted = pygame.image.load('images/audio/sound_highlighted.png')

music_muted_img_highlighted = pygame.image.load('images/audio/music_muted_highlighted.png')
sound_muted_img_highlighted = pygame.image.load('images/audio/sound_muted_highlighted.png')

keyboard_img = pygame.image.load('images/modes/keyboard_mode.png')
keyboard_img_highlighted = pygame.image.load('images/modes/keyboard_mode_highlighted.png')
mouse_img = pygame.image.load('images/modes/mouse_mode.png')
mouse_img_highlighted = pygame.image.load('images/modes/mouse_mode_highlighted.png')

back_img = pygame.image.load('images/back.png')
back_img_highlighted = pygame.image.load('images/back_highlighted.png')

# game images
red_paddle_img = pygame.image.load('images/game/red_paddle.png')
orange_paddle_img = pygame.image.load('images/game/orange_paddle.png')

red_brick_img = pygame.image.load('images/game/red_brick.png')
green_brick_img = pygame.image.load('images/game/green_brick.png')
blue_brick_img = pygame.image.load('images/game/blue_brick.png')

ball_img = pygame.image.load('images/game/ball.png')

def scale_menu(screen_width, screen_height):
    global BG_SMALL, BG_MEDIUM, BG_LARGE, TITLE_SMALL, TITLE_MEDIUM, TITLE_LARGE, BG_BLUR_SMALL, BG_BLUR_MEDIUM, BG_BLUR_LARGE, p2p_font, p2p_font_current, play_solo_button, play_coop_button, options_button, exit_button, video_button, audio_button, mode_button, small_button, medium_button, large_button, music_button, sound_button, music_muted_button, sound_muted_button, keyboard_mode_button, mouse_mode_button, back_button
    
    scale = screen_width / 1280

    BG_SMALL = pygame.transform.scale(BG_SMALL, (800, 450))
    BG_MEDIUM = pygame.transform.scale(BG_MEDIUM, (1024, 576))
    BG_LARGE = pygame.transform.scale(BG_LARGE, (1280, 720))

    TITLE_SMALL = pygame.transform.scale(TITLE_SMALL, (481, 74))
    TITLE_MEDIUM = pygame.transform.scale(TITLE_MEDIUM, (615, 94))
    TITLE_LARGE = pygame.transform.scale(TITLE_LARGE, (770, 118))

    BG_BLUR_SMALL = pygame.transform.scale(BG_BLUR_SMALL, (800, 450))
    BG_BLUR_MEDIUM = pygame.transform.scale(BG_BLUR_MEDIUM, (1024, 576))
    BG_BLUR_LARGE = pygame.transform.scale(BG_BLUR_LARGE, (1280, 720))

    p2p_font = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", int(screen_width / (1280 / 38)))
    p2p_font_current = pygame.font.Font("fonts/PressStart2P-vaV7.ttf", int(screen_width / (1280 / 20)))

    # mainMenuButtons
    play_solo_button = Button(screen_width / (1280 / 390), screen_height / (720 / 204), play_solo_img, play_solo_img_highlighted, scale)
    play_coop_button = Button(screen_width / (1280 / 390), screen_height / (720 / 318), play_coop_img, play_coop_img_highlighted, scale)
    options_button = Button(screen_width / (1280 / 390), screen_height/ (720 / 432), options_img, options_img_highlighted, scale)
    exit_button = Button(screen_width / (1280 / 655), screen_height/ (720 / 432), exit_img, exit_img_highlighted, scale)

    # optionsMenuButtons
    video_button = Button(screen_width / (1280 / 522), screen_height / (720 / 204), video_img, video_img_highlighted, scale)
    audio_button = Button(screen_width / (1280 / 522), screen_height / (720 / 318), audio_img, audio_img_highlighted, scale)
    mode_button = Button(screen_width / (1280 / 522), screen_height / (720 / 432), mode_img, mode_img_highlighted, scale)

    # videoMenuButtons
    small_button = Button(screen_width / (1280 / 522), screen_height / (720 / 204), small_img, small_img_highlighted, scale)
    medium_button = Button(screen_width / (1280 / 522), screen_height / (720 / 318), medium_img, medium_img_highlighted, scale)
    large_button = Button(screen_width / (1280 / 522), screen_height / (720 / 432), large_img, large_img_highlighted, scale)

    # audioMenuButtons
    music_button = Button(screen_width / (1280 / 541), screen_height/ 2 - music_img.get_height() / 2, music_img, music_img_highlighted, scale)
    sound_button = Button(screen_width / (1280 / 655), screen_height/ 2 - sound_img.get_height() / 2, sound_img, sound_img_highlighted, scale)
    music_muted_button = Button(screen_width / (1280 / 541), screen_height/ 2 - music_img.get_height() / 2, music_muted_img, music_muted_img_highlighted, scale)
    sound_muted_button = Button(screen_width / (1280 / 655), screen_height/ 2 - sound_img.get_height() / 2, sound_muted_img, sound_muted_img_highlighted, scale)

    # modeMenuButtons
    keyboard_mode_button = Button(screen_width / (1280 / 522), screen_height / (720 / 261), keyboard_img, keyboard_img_highlighted, scale)
    mouse_mode_button = Button(screen_width / (1280 / 522), screen_height / (720 / 375), mouse_img, mouse_img_highlighted, scale)

    back_button = Button(screen_width / (1280 / 18), screen_height / (720 / 18), back_img, back_img_highlighted, scale)
    