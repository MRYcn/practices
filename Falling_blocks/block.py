#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py
try:
	import pygame
	from pygame.sprite import Sprite
except:
	pass

class Block(Sprite):
	def __init__(self,B_game,chcolor=False):
		super().__init__()
		self.screen=B_game.screen
		self.settings=B_game.settings
		self.stats=B_game.stats
		self.status=B_game.status
		if not self.status:
			self.x=self.y=50
			self.color=(230,30,0)
			if chcolor:
				self.color=(0,135,0)
		else:
			recttuple=self.settings.block_rect[self.stats.level-1]
			self.x,self.y=recttuple[0],recttuple[1]
		self.rect=pygame.Rect(0,0,self.x,self.y)
	def blitme(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
