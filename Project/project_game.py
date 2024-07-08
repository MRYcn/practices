#coding=utf-8
#author=QQ群824091869
#releasedtime=

import pygame
import pygame.font
import sys

class Pro_game:
	def __init__(self):
		pygame.init()
		#self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.screen=pygame.display.set_mode((500,500))
		self.screen_width=self.screen.get_rect().width
		self.screen_height=self.screen.get_rect().height
		pygame.display.set_caption('Project')
	
	def run_game(self):
		while True:
			self._check_event()
			
			self._update_screen()
	
	def _check_event(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				if self.quitdef():
					pygame.quit()
					sys.exit()
			if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
								if self.quitdef():
										pygame.quit()
										sys.exit()
	
	def _update_screen(self):
		self.screen.fill((0,0,0))
		pygame.display.flip()

	def quitdef(self):
		return True

game=Pro_game()
game.run_game()
