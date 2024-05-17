import pygame
import menu_settings

#button class

pygame.mixer.init()

button_sfx = pygame.mixer.Sound('audio/buttonSound.mp3')

class Button():
	def __init__(self, x, y, image, imageOn, scale = 1):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.imageOn = pygame.transform.scale(imageOn, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		on_button = self.rect.collidepoint(pygame.mouse.get_pos())

		action = False
		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if not menu_settings.mute_sfx: button_sfx.play()
					self.clicked = True
					action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		if self.clicked or on_button:
			# if self.clicked:
			surface.blit(self.imageOn, self.imageOn.get_rect(center=self.rect.center))
		else:
			surface.blit(self.image, self.image.get_rect(center=self.rect.center))

		return action