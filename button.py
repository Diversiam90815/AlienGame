import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Button")
main_font = pygame.font.SysFont('cambria', 50)


#class Button:

#    def __init__(self, ai_game, msg):
#        self.screen = ai_game.screen
#        self.screen_rect = self.screen.get_rect()
#        self.width, self.height = 200, 50
#        self.button_color = (0, 255, 0)
#        self.text_color = (255, 255, 255)
#        self.font = pygame.font.SysFont(None, 48)
#        self.rect = pygame.Rect(0, 0, self.width, self.height)
#        self.rect.center = self.screen_rect.center
#        self._prep_msg(msg)

#    def _prep_msg(self,msg):
#        """Turn msg into a rendered image and center it on the button."""
#        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
#        self.msg_image_rect = self.msg_image.get_rect()
#        self.msg_image_rect.center = self.rect.center

#    def draw_button(self):
#        """Draws a button."""
#        self.screen.fill(self.button_color,self.rect)
#        self.screen.blit(self.msg_image, self.msg_image_rect)



class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)