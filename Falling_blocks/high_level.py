#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py
try:
	import pygame, pygame.font
	from pygame.sprite import Sprite
except:
	pass

class High_level(Sprite):
	def __init__(self,B_game,level):
		self.settings.B_game.settings
		self.screen=B_game.screen
		self.stats=B_game.stats
		if level>=1:
			self.font=pygame.font.SysFont(None,40)
		else:
			self.font=pygame.font.SysFont(None,60)
		self.color=(30,30,30)
		self.bg_color=self.settings.bg_color
		if level>=1:
			self.high_str=str(self.stats.highs[level])
			self.img=self.font.render(self.high_str,True,self.color,self.bg_color)
			self.rect=self.img.get_rect()
		else:
			self.level_str='最高纪录：'
			self.img=self.font.render(self.level_str,True,self.color,self.bg_color)
			self.rect=self.img.get_rect()
	def blitme(self):
		self.screen.blit(self.img,self.rect)