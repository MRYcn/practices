#coding=utf-8
#author=MRY
#releasedtime=

#assist for: block_game.py

class Stats:
	def __init__(self,B_game):
		self.settings=B_game.settings
		rfile=open('user_info','r').readlines()
		if rfile[5][0]!='0':
			self.level=int(rfile[5][0])
		else:
			self.level=0
		self.highs=[None]
		for high in rfile[:5]:
			self.highs.append(int(high[:-2]))
		rfile.close()
		self.score=0
		self.lives_left=0
		self.lives_limit=0
		self.wait=0.0
		self.thread=B_game.thread
	def check_high_score(self,B_game):
		if self.highs[self.level]!=None and self.highs[self.level]<self.score:
			self.highs[self.level]=self.score
	def update(self,hit):
		if hit:
			self.score+=self.settings.sing_score
		else:
			self.lives_left-=1
	def reset(self):
		self.lives_limit=self.lives_left=self, settings.lives_limits[self.level-1]
		self.score=0
		self.wait=randint(self.settings.wait[0],self.settings.wait[1])/10
		self.thread.reset()
