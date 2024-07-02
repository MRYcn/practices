#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py
try:
	import pygame, datetime
except:
	pass

class Thread:
	def __init__(self,B_game):
		self.screen=B_game.screen
		self.boot=True
		self.start=590
		self.end=610
		self.width=20
		self.length_r=20
		self.color=(30,30,30)
	
	def blitme(self):
		if self.boot:
			_bootan()
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
				self.start-=self.length_r
				self.end+=self.length_r
				pygame.draw.line(self.screen,self.color,self.start,self.end,self.width)
				d1=d2
			if self.start<=60:
				break
	def reset(self):
		self.start=590
		self.end=610
		self.boot=True