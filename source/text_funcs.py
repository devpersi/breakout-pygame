def text(screen, text, font, text_col, screen_width, screen_height):
	img = font.render(text, True, text_col)
	screen.blit(img, (screen_width / 2 - img.get_width() / 2, screen_height / (720 / 18)))

def text_current(screen, text, font, text_col, screen_width, screen_height):
	img = font.render(text, True, text_col)
	screen.blit(img, (screen_width - img.get_width() - screen_width / (1280 / 24), screen_height / (720 / 680)))
 
def text_score(screen, text, font, text_col, screen_width, screen_height):
	img = font.render(text, True, text_col)
	screen.blit(img, (img.get_width() - screen_width / (1280 / 24), screen_height / (720 / 680)))