#coding=utf-8
#author=MRY
#releasedtime=2024.7.9
try:
	import pygame,pygame.font,sys,random,datetime,os
except:
	pass
from time import sleep
from level import Level
from block import Block
from threaddef import Thread
from scoreboard import Scoreboard as Sb
from stats import Stats
from settings import Settings
from high_level import High_level as HL

class Block_game:
		def __init__(self):
				self.settings=Settings()
				if not os.path.exists('user_info'):
						cfile=open("user_info",'w')
						cfile.write('0\n0\n0\n0\n0\n1\n \n')
						cfile.close()
				try:
						if open('user_info','r').readlines()[-1]=='dev\n':
								self.dev=True
						else:
								self.dev=False
				except:
						self.dev=False
				self.stats=Stats(self)
				pygame.init()
				self.screen=pygame.display.set_mode((1200,700))
				pygame.display.set_caption('Falling Blocks')
				self.status=False
				self.thread=Thread(self)
				self.stats.thread=self.thread
				self.c_blocks=pygame.sprite.Group()
				self.g_blocks=pygame.sprite.Group()
				self.levels=pygame.sprite.Group()
				self.high_levels=pygame.sprite.Group()
				self.sb=Sb(self)
				self.clock=pygame.time.Clock()
				self._create_block()
				self._create_levels()
				self._create_intro()
				self._create_high_levels()
				self.high_checked=True
				self.bl_d1=None
#                               self.stats.ch_last(self)

		def run_game(self):
				while True:
						self._check_events()
						if not self.status and not self.high_checked:
								self.stats.check_high_score(self)
								self._create_high_levels()
								self.high_checked=True
						else:
								self._create_block()
								self._update_block()
						self._update_screen()
						self.clock.tick(60)
		def _check_events(self):
				for event in pygame.event.get():
						if event.type==pygame.QUIT:
								self._quitdef()
						if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
								self._quitdef()
						if not self.status:
								if event.type==pygame.MOUSEBUTTONDOWN:
										mouse_pos=pygame.mouse.get_pos()
										n=1
										for block in self.c_blocks:
												if block.rect.collidepoint(mouse_pos):
														self.status=True
														self.stats.level=self._update_level(n)
														self.settings.dynamic_set(n)
														self.stats.reset()
														sleep(1)
														break
												n+=1
						else:
								if event.type==pygame.MOUSEBUTTONDOWN:
										mouse_pos=pygame.mouse.get_pos()
										for block in self.g_blocks.copy():
												if block.rect.collidepoint(mouse_pos):
														if block.rect.midtop[1]<=550<=block.rect.midbottom[1]:
																self.stats.update(True)
														else:
																self.stats.update(False)
																print('-1')
														self.g_blocks.remove(block)
														continue
								for block in self.g_blocks.copy():
										if block.rect.midbottom[1]>=700:
												self.stats.update(False)
												self.g_blocks.remove(block)
												print('-1')
								if self.stats.lives_left<=0:
										self.status=False
										self.high_checked=False
										self.g_blocks.empty()
										self._create_block()
										self._create_levels()
										self._score_ending()
		def _create_intro(self):
				intro_str=('接方块游戏。选择难度级别后，当方块在判定线上时点击方','块，则得分，否则失去一条生命。游戏会记录您的最高分。','作者：MRY 联系：yrk2021***.com''版本：1.0.0')
				intro_bg_color=self.settings.bg_color
				intro_color=(30,30,30)
				font=pygame.font.SysFont('FangSong',30)
				self.intro_images=[]
				x=600
				y=459
				for i in range(3):
						intro_image=font.render(intro_str[i],True,intro_color,intro_bg_color)
						intro_image_rect=intro_image.get_rect()
						intro_image_rect.centerx=x
						intro_image_rect.centery=y
						y+=32
						self.intro_images.append([intro_image,intro_image_rect])

		def _create_levels(self):
				self.levels.empty()
				x,y=200,350
				for i in range(1,6):
						new_level=Level(self,i)
						new_level.rect.centerx=x
						new_level.rect.centery=y
						x+=200
						self.levels.add(new_level)
				new_level=Level(self,0)
				new_level.rect.centerx=600
				new_level.rect.centery=200
				self.levels.add(new_level)

		def _create_high_levels(self):
				x,y=200,280
				self.high_levels.empty()
				for i in range(1,6):
						new_high=HL(self,i)
						new_high.rect.centerx=x
						new_high.rect.centery=y
						x+=200
						self.high_levels.add(new_high)
				new_high=HL(self,0)
				new_high.rect.centerx=100
				new_high.rect.centery=280
				self.high_levels.add(new_high)
				x,y=200,280

		def _create_block(self):
				if self.status:
						if self.bl_d1:
								d2=datetime.datetime.now()
								d=d2-self.bl_d1
								if d.seconds>=self.stats.wait:
										x=random.randint(50,1150)
										new_block=Block(self)
										new_block.rect.centerx=x
										new_block.rect.centery=50
										self.g_blocks.add(new_block)
										self.bl_d1=d2
						else:
								self.bl_d1=datetime.datetime.now()
				else:
						x,y=200,350
						self.c_blocks.empty()
						for i in range(5):
								new_block=Block(self,self.stats.level==i+1)
								new_block.rect.centerx=x
								new_block.rect.centery=y
								self.c_blocks.add(new_block)
								x+=200

		def _update_level(self,n):
				level=self.levels.sprites()[n-1]
				level.change_color()
				x=level.rect.centerx
				y=level.rect.centery
				x_r=(1170-x)/60
				y_r=(75-y)/60
				while x<1170 and y>75:
						x+=x_r
						y+=y_r
						level.rect.centerx=x
						level.rect.centery=y
						level.change_size()
						self.screen.fill((230,230,230))
						level.blitme()
						pygame.display.flip()
				self.display_level=level
				return n
		def _update_block(self):
				for block in self.g_blocks:
						block.rect.y+=self.settings.speed

		def _score_ending(self):
				x=600
				y=50
				y_r=5
				s=48
				s_r=0.2
				score_color=(30,30,30)
				score_bg_color=self.settings.bg_color
				while y<=350:
						y+=y_r
						s+=s_r
						st=int(s)
						font=pygame.font.SysFont(None,st)
						score_image=font.render(str(self.stats.score),True,score_color,score_bg_color)
						score_image_rect=score_image.get_rect()
						score_image_rect.centerx=x
						score_image_rect.centery=y
						self.screen.fill(self.settings.bg_color)
						self.screen.blit(score_image,score_image_rect)
						pygame.display.flip()
				sleep(1)

		def _update_screen(self):
				self.screen.fill(self.settings.bg_color)
				if not self.status:
						for high in self.high_levels.sprites():
								high.blitme()
						for block in self.c_blocks.sprites():
								block.blitme()
						for level in self.levels.sprites():
								level.blitme()
						for intro in self.intro_images:
								self.screen.blit(intro[0],intro[1])
				else:
#                                               print(self.stats.lives_left)
						self.display_level.blitme()
						self.sb.blitme(self)
						self.thread.blitme()
						for block in self.g_blocks.sprites():
							block.blitme()
				pygame.display.flip()

		def _quitdef(self):
				wfile=open('user_info','w')
				wfilet=[]
				for high_level in range(5):
						wfilet.append(str(self.stats.highs[high_level+1]))
						wfilet.append('\n')
				wfilet.append(str(self.stats.level)+'\n')
				if self.dev:
						wfilet.append('dev')
				else:
						wfilet.append('')
				wfilet.append('\n')
				for i in wfilet:
						wfile.write(i)
				wfile.close()
				pygame.quit()
				sys.exit()


if __name__=='__main__':
		print('本游戏使用python开发，可能会有性能问题，敬请谅解。\n正在初始化…')
		B_game=Block_game()
		B_game.run_game()
else:
		print('请直接在控制台运行！')
#
