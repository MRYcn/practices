#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py
try:
	import pygame
	import pygame.font
except:
	pass

class Scoreboard:
	def __init__(self,B_game):
		self.screen=B_game.screen
		self.rects={'miss':[],'current':[],'highest':[]}
		self.color=(30,30,30)
		self.red=(230,0,0)
		self.font=pygame.font.SysFont(None,20)
	def _update_sb(self,B_game):
		self.miss_y=50
		self.limit_life=B_game.stats.lives_limit
		stats=B_game.stats
		self.rects['miss']=[]
		for i in range(self.limit_life-stats.lives.left):
			miss_image=self.font.render('×',True,self.red,(230,230,230))
			miss_image_rect=miss_image.get_rect()
			miss_image_rect.centerx=25
			miss_image_rect.centery=self.miss_y
			comb=[miss_image,miss_image_rect]
			self.rects['miss'].append(comb)
			self.miss_y+=20
		for i in range(stats.lives.left):
			miss_image=self.font.render('×',True,self.color,(230,230,230))
			miss_image_rect=miss_image.get_rect()
			miss_image_rect.centerx=25
			miss_image_rect.centery=self.miss_y
			comb=[miss_image,miss_image_rect]
			self.rects['miss'].append(comb)
			self.miss_y+=20
		self.rects['current']=[]
		score_image=self.font.render(str(stats.score),True,self.color,(230,230,230))
		score_image_rect=score_image.get_rect()
		score_image_rect.centerx=600
		score_image_rect.centery=50
		comb=[score_image,score_image_rect]
		self.rects['current'].append(comb)
		self.rects['highest']=[]
		high_image=self.font.render(str(stats.highs[stats.level]),True,self.color,(230,230,230))
		high_image_rect=score_image.get_rect()
		high_image_rect.centerx=1150
		high_image_rect.centery=50
		comb=[high_image,high_image_rect]
		self.rects['highest'].append(comb)
	def blitme(self,B_game):
		self._update_sb(B_game)
		for sect in self.rects:
			for rect in sect:
				self.screen.blit(rect[0],rect[1])
