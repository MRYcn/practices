import pygame,random,sys
#score=0
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption('collect fu')
screen.fill((0,0,0))
#background=pygame.image.load('bg.jpg')

def main():
    score=0
    while True:
        #screen.blit(back,[0,0])
        showscore(score)
        x=random. randint(50, 700)
        y=random. randint(50, 700)
        showfu(x,y)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousex,mousey=pygame.mouse.get_pos()
                    if mousex in range(x,x+60) and mousey in range(y,y+70):
                        score+=5
                        break
        pygame.time.delay(800)

def showfu(x,y):
    w=random.randint(1,2)
    gift=pygame.image.load(f'fu{str(w)}.png')
    screen.blit(gift,[x,y])

def showscore(score):
    textfont=pygame.font.SysFont('Arial',30)
    t=textfont.render('score:'+str(score),True, (255,0,0))
    screen.blit(t,[50,50])
