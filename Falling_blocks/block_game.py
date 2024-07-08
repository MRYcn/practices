#coding=utf-8
#author=MRY
#releasedtime=
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
                                self.screen=pygame.display.set_mode((700,500))
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
                                                                                                                sleep(3)
                                                                                                                break
                                                                                                n+=1
                                                else:
                                                                if event.type==pygame.MOUSEBUTTONDOWN:
                                                                                mouse_pos=pygame.mouse.get_pos()
                                                                                for block in self.g_blocks.copy():
                                                                                                if block.rect.collidepoint(mouse_pos):
                                                                                                                if block.rect.midtopy<=550<=block.rect.midbottomy:
                                                                                                                                self.stats.update(True)
                                                                                                                else:
                                                                                                                                self.stats.update(False)
                                                                                                                self.g_blocks.remove(block)
                                                                                                if block.rect.midbottomy>=700:
                                                                                                                self.stats.update(False)
                                                                                                                self.g_block.remove(block)
                                                                if self.stats.lives_left<=0:
                                                                                self.status=False
                                                                                self.high_checked=False
                                                                                self.g_blocks.empty()
                                                                                self._create_block()
                                                                                self._score_ending()
                def _create_intro(self):
                                intro_str='接方块游戏。选择难度级别后，当方块在判定线上时点击方\n块，则得分，否则失去一条生命。游戏会记录您的最高分。\n作者：MRY 联系：yrk2021***.com\n 版本：1.0.0'
                                intro_bg_color=self.settings.bg_color
                                intro_color=(30,30,30)
                                font=pygame.font.SysFont(None,30)
                                self.intro_image=font.render(intro_str,True,intro_color,intro_bg_color)
                                self.intro_image_rect=self.intro_image.get_rect()
                                self.intro_image_rect.centerx=600
                                self.intro_image_rect.centery=450

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
                                new_high.rect.centerx=50
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
                                                                                new_block.rect.midtopx=x
                                                                                new_block.rect.midtopy=50
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
                                y_r=(70-y)/60
                                while x<1170 and y>70:
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
                                s=48
                                s_r=0.2
                                score_color=(30,30,30)
                                score_bg_color=self.settings.bg_color
                                while y<=350:
                                                y+=y_r
                                                s+=s_r
                                                st=int(s)
                                                font=pygame.font.SysFont(None,st)
                                                score_image=font.render(str(self.score),True,score_color,score_bg_color)
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
                                                self.screen.blit(self.intro_image,self.intro_image_rect)
                                else:
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
                                                wfilet.append(str(self.stats.highs[high_level]))
                                                wfilet.append('\n')
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
