#coding=utf-8
#author=MRY
#releasedtime=

#assists for: block_game.py

class Settings:
	def __init__(self):
		self.screen_size=(1200,700)
		self.bg_color=(230,230,230)
		self.level_color=(30,30,30)
		self.block_rect=[(100,100),(100,50),(75,25),(50,25),(20,20)]
		self.speeds=[10,15,20,25,30]
		self.lives_limits=[3,3,3,2,2]
		self.waits=[(10,30),(5,15),(5,10),(3,10),(2,7)]
		self.sing_scores=[10,15,20,25,30]
	def dynamic_set(self,level):
		self.speed=self.speeds[level-1]
		self.lives_limit=self.lives_limits[level-1]
		self.sing_score=self.sing_scores[level-1]
		self.wait=self.waits[level-1]
