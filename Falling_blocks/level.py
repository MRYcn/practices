#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py
try:
	import pygame
	from pygame.sprite import Sprite
except:
	pass

class Level(Sprite):
	def __init__(self,B_game,n):
		super().__init__()
		self.screen=B_game.screen
		self.settings=B_game.settings
		self.color=self.settings.level_color
		self.bg_color=self.settings.bg_color
		if n!=0:
			self.font=pygame.font.SysFont(None,48)
			self.level_str=str(n)
			self.level_img=self.font.render(self.level_str,True,self.color,self.bg_color)
			self.rect=self.level_img.get_rect()
			self.font_scale=24/60
			self.size=48
		else:
			font=pygame.font.SysFont(None,60)
			level_str='级别'
			self.level_img=font.render(level_str,True,(30,30,30),self.bg_color)
			self.rect=self.level_img.get_rect()
	
	def blitme(self):
		self.screen.blit(self.level_img,self.rect)
	
	def change_color(self):
		self.level_img=self.font.render(self.level_str,True,(30,30,30),self.bg_color)
	
	def change_size(self):
		self.size-=self.font_scale
		self.font=pygame.font.SysFont(None,int(self.size))
		self.change_color()
