#coding=utf-8
#author=MRY
#releasedtime=

from random import randint

def main():
    sq=[None for i in range(9)]
    input('回车以开始：')
    user=bool(randint(0,1))
    if user:
        print('User先行')
        out(sq)
        while True:
            try:
                user_append=int(input('请输入落棋位：'))
               	if 1<=user_append<=9:
                   	user=False
                   	break
                else:
                    print('输入不规范,',end='')
            except:
                print('输入不规范,',end='')
        sq[user_append-1]=0
    else:
        print('Bot先行')
        #sq=mind(sq)
        user=True
        out(sq)
    while True:
        if user:
            while True:
                try:
                    user_append=int(input('请输入落棋位:'))
                    if user_append<1 or user_append>9:
                        print('输入不规范,',end='')
                    elif sq[user_append-1]!=None:
                        print('棋位已落子,',end='')
                    else:
                        sq[user_append-1]=0
                        break
                except:
                    print('输入不规范,',end='')
            sq[user_append-1]=0
            result=iswin(sq)
            if result==1 or result==2 or result==0:
                break
            user=False
        if not user:
            
            #sq=mind(sq)
            
            result=iswin(sq)
            if result==1 or result==2 or result==0:
                break
            user=True
    if result==1:
        out(sq)
        print('你输了！')
        return
    elif result==0:
        out(sq)
        print('你赢了！')
        return
    elif result==2:
        out(sq)
        print('平局')
        return

def out(sq):
    '''输出局势'''
    it=0
    for va in sq:
        if it%3==0 and it!=0:
            print('')
        if va==0:
            print('○',end='')
        if va==1:
            print('╳',end='')
        if va==None:
            print('__',end='')
        it+=1
    return

def mind(sq):
    return

def helpset():
	print('九宫格棋。与人机下棋，您为○，人机为╳，优先连成一条线的获胜。九宫格中数字从左到右、从上到下依次递增，从1–9。')
    
def iswin(sq):
    '''判断局势'''
    print('sq:',sq)
    rs=False
    ran=0
    for st in [0,3,6]:
        if sq[st]==sq[st+1]==sq[st+2]==0 or sq[st]==sq[st+1]==sq[st+2]==1:
            rs=True
            rt=(sq[st],sq[st+1],sq[st+2])
            break
    if not rs:
        if sq[2]==sq[4]==sq[6]:
            rs=True
            rt=(sq[2],sq[4],sq[6])
    if not rs:
        for st in [0,1,2]:
            if sq[st]==sq[st+3]==sq[st+6]:
                rs=True
                rt=(sq[st],sq[st+3],sq[st+6])
                break
    if not rs:
        if sq[0]==sq[4]==sq[8]:
            rs=True
            rt=(sq[0],sq[4],sq[8])
    if not rs:
        #print('判断平局')
        return None
    if rt[0]==0:
        #print('判断赢')
        return 0
    elif rt[0]==1:
        #print('判断输')
        return 1
    elif None in sq:
        #print('判断无')
        return None
    else:
        #print('判断平')
        return 2


def level_judge(user_position,bot_position,target_position):
    return
    
if __name__=='__main__':
    ans='y'
    while True:
        if ans=='y' or ans=='Y':
            main()
        ans=input('是否再来？(y/n);显示帮助信息(h):')
        if ans=='y' or ans=='Y':
            continue
        elif ans=='n' or ans=='N':
            print('谢谢使用！')
            break
        elif ans=='h' or ans=='H':
            helpset()
        else:
            print('输入不规范,',end='')
        
