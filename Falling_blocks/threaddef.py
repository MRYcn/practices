#coding=utf-8
#author=MRY
#releasedtime=2024.7.9

#assist for: block_game.py
try:
	import pygame, datetime
except:
	pass

class Thread:
	def __init__(self,B_game):
		self.screen=B_game.screen
		self.bg_color=B_game.settings.bg_color
		self.boot=True
		self.start=(590,550)
		self.end=(610,550)
		self.width=8
		self.length_r=20
		self.color=(30,30,30)
	
	def blitme(self):
		if self.boot:
			self._bootan()
		else:
			pygame.draw.line(self.screen,self.color,self.start,self.end,self.width)
	def _bootan(self):
		self.boot=False
		d1=datetime.datetime.now()
		while True:
			d2=datetime.datetime.now()
			d=d2-d1
			dm=d.microseconds/1000
			if dm>=20:
				self.start=(self.start[0]-self.length_r,self.start[1])
				self.end=(self.end[0]+self.length_r,self.end[1])
				self.screen.fill(self.bg_color)
				pygame.draw.line(self.screen,self.color,self.start,self.end,self.width)
				pygame.display.flip()
				d1=d2
			if self.start[0]<=60:
				break
	def reset(self):
		self.start=(590,550)
		self.end=(610,550)
		self.boot=True
