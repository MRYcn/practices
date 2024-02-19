#-*-coding:utf-8;-*-
#author:MRY
#releasedtime:2024.2.18

import datetime,os,random,time,hashlib
def main():
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    if os.path.exists('user_info'):
        rfile=open('user_info','r')
        rf=rfile.readlines()
        if rf[2]=='unlocked\n':
            dsrc[0]=rf[1][:-1:]
        rfile.close()
    dsrc[1]='心算能手'
    dsrc[3]='开始(G)'
    dsrc[4]='帮助(H)'
    dsrc[5]='设置(S)'
    dsrc[6]='用户(U)'
    dsrc[7]='退出(Q)'
    dsrc[10]='输入功能字母'
    draw(dsrc)
    met=input(':')
    while True:
        if met=='g' or met=='G':
            start()
            break
        elif met=='h' or met =='H':
            helpdef()
            break
        elif met=='s' or met=='S':
            setdef()
            break
        elif met=='u' or met=='U':
            user()
            break
        elif met=='q' or met=='Q':
            quitdef()
            break
        else:
            dsrc[10]='输入错误，输入功能字母：'
            draw(dsrc)
            met=input()
    return

def helpdef():
    '''帮助信息'''
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    dsrc[1]='心算能手'
    dsrc[2]='一个用于心算练习的程序。你可以选择推荐模式或自定义。通过输入字母、数字，选择功能、输入答案。'
    dsrc[9]='返回(R)'
    dsrc[10]='输入功能字母:'
    draw(dsrc)
    met=None
    while True:
        if met=='r' or met=='R':
            break
        elif met!=None:
            dsrc[10]='输入错误，输入功能字母:'
            draw(dsrc)
            met=None
        else:
            met=input()
    return

def setdef():
    '''设置'''
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    dsrc[1]='设置'
    dsrc[3]='布局(L)'
    dsrc[4]='关于(A)'
    dsrc[9]='返回(R)'
    dsrc[10]='输入功能字母：'
    draw(dsrc)
    met=None
    while True:
        if met=='L' or met=='l':
            for i in range(11):
                dsrc[i]=None
            dsrc[1]='布局'
            if os.path.exists('user_info'):
                rfile=open('user_info','r')
                rf=rfile.readlines()
                rfile.close()
                if rf[2]=='unlocked\n':
                    layout=int(rf[4][:-1:])
            else:
                layout=35
            if layout==35:
                dsrc[3]='默认:'
            else:
                dsrc[3]='数值:'
            dsrc[3]+=str(layout)
            dsrc[3]+='(L+数字)'
            dsrc[4]='什么是布局？(H)'
            dsrc[9]='返回(R)'
            dsrc[10]='输入功能字母:'
            draw(dsrc)
            met=None
            while True:
                intt=False
                if met!=None and len(met)>1:
                    try:
                        intt=int(met[1:])
                    except:
                        init=False
                if met!=None and len(met)>1 and (met[0]=='l' or met[0]=='L') and intt:
                    if os.path.exists('user_info'):
                        rfile=open('user_info','r')
                        rf=rfile.readlines()
                        if rf[2]=='unlocked\n':
                            rfile.close()
                            wfile=open('user_info','w')
                            rf[4]=met[1:]+'\n'
                            wfile.writelines(rf)
                            wfile.close()
                            dsrc[10]='修改成功，输入功能字母:'
                            layout=int(met[1:])
                            if layout==35:
                                dsrc[3]='默认:'
                            else:
                                dsrc[3]='数值:'
                            dsrc[3]+=str(layout)
                            dsrc[3]+='(L+数字)'
                            draw(dsrc)
                        else:
                            rfile.close()
                            dsrc[10]='请登录后再修改，输入功能字母:'
                            draw(dsrc)
                    else:
                        dsrc[10]='请登录后再修改，输入功能字母:'
                        draw(dsrc)
                    met=None
                elif met=='h' or met=='H':
                    dsrc[3]=dsrc[4]=None
                    dsrc[2]='布局是绘图的屏幕宽度，单位字符，默认35。'
                    dsrc[10]='输入功能字母:'
                    draw(dsrc)
                    while True:
                        met=input()
                        if met=='r' or met=='R':
                            if layout==35:
                                dsrc[3]='默认：'
                            else:
                                dsrc[3]='数值：'
                            dsrc[3]+=str(layout)
                            dsrc[3]+='(L+数字)'
                            dsrc[2]=None
                            break
                        else:
                            dsrc[10]='输入错误，输入功能字母:'
                            draw(dsrc)
                    met=None
                    if layout==35:
                        dsrc[3]='默认'
                    else:
                        dsrc[3]='数值:'
                    dsrc[3]+=str(layout)
                    dsrc[3]+='(L+数字)'
                    dsrc[4]='什么是布局？(H)'
                    dsrc[10]='输入功能字母:'
                    draw(dsrc)
                    met=None
                elif met=='r' or met=='R':
                    dsrc[1]='设置'
                    dsrc[3]='布局(L)'
                    dsrc[4]='关于(A)'
                    met=None
                    draw(dsrc)
                    break
                elif met!=None:
                    dsrc[10]='输入错误，输入功能字母:'
                    met=None
                    draw(dsrc)
                else:
                    met=input()
        elif met=='a' or met=='A':
            met=None
            dsrc[1]='关于'
            dsrc[3]=dsrc[4]=None
            dsrc[2]='作者：MRY\n版本：1.0.0\n发布时间：2024.2.18\n联系：yrk2021***@***.com'
            draw(dsrc)
            while True:
                if met=='r' or met=='R':
                    met=None
                    dsrc[1]='设置'
                    dsrc[2]=None
                    dsrc[3]='布局(L)'
                    dsrc[4]='关于(A)'
                    dsrc[10]='输入功能字母:'
                    draw(dsrc)
                    break
                elif met!=None:
                    dsrc[10]='输入错误，输入功能字母:'
                    met=None
                    draw(dsrc)
                else:
                    met=input()
        elif met=='r' or met=='R':
            met=None
            if os.path.exists('user_info'):
                rfile=open('user_info','r')
                rf=rfile.readlines()
                if rf[2]=='unlocked\n':
                    dsrc[0]=rf[1][:-1:]
                rfile.close()
            dsrc[1]='心算能手'
            dsrc[3]='开始(G)'
            dsrc[4]='帮助(H)'
            dsrc[5]='设置(S)'
            dsrc[6]='用户(U)'
            dsrc[7]='退出(Q)'
            dsrc[9]=None
            dsrc[10]='输入功能字母:'
            draw(dsrc)
            break
        elif met!=None:
            dsrc[10]='输入错误，输入功能字母:'
            met=None
            draw(dsrc)
        else:
            met=input()
    return
                    
def draw(dsrc):
    '''绘图'''
    if os.path.exists('user_info'):
        rfile=open('user_info','r')
        rf=rfile.readlines()
        if rf[2]=='unlocked\n':
            layout=int(rf[4][:-1:])
        else:
            layout=35
    else:
        layout=35
    if os.path.exists('/storage') or os.path.exists('/root'):
        os.system('clear')
    else:
        os.system('cls')
    if dsrc[0]!=None:
        print(dsrc[0],end='')#1 line
    print('\n')#3 line
    stp=int(layout/2-int(len(dsrc[1])/2))
    for i in range(stp):
        print(' ',end='')
    print(dsrc[1])#4 line b
    line=4
    if dsrc[2]!=None:
        for i in range(6):
            print(' ',end='')
        estp=int(layout-5)
        rtlines=[]
        aplines=''
        for i in range(len(dsrc[2])):
            if i%estp==0 and i!=0:
                rtlines.append(aplines)
                aplines=''
            aplines+=dsrc[2][i]
        if aplines!='':
            rtlines.append(aplines)
        for i in rtlines:
            for j in range(5):
                print(' ',end='')
            print(i)
        line=4+len(rtlines)#4+len(rtlines) b
        for j in range(14-line):
            print()#14 line b
        line=14
    elif dsrc[3]!=None:
        print()#5 line b
        for i in range(5):
            print(' ',end='')
        print(dsrc[3])#6 line b
        line=6
    if dsrc[4]!=None:
        for i in range(7-line):
            print()#7 line b
        for i in range(5):
            print(' ',end='')
        print(dsrc[4])#8 line b
        line=8
    if dsrc[5]!=None:
        for i in range(9-line):
            print()#9 line b
        for i in range(5):
            print(' ',end='')
        print(dsrc[5])#10 line b
        line=10
    if dsrc[6]!=None:
        for i in range(11-line):
            print()#11 line b
        for i in range(5):
            print(' ',end='')
        print(dsrc[6])#12 line b
        line=12
    if dsrc[7]!=None:
        for i in range(13-line):
            print()
        for i in range(5):
            print( '',end='')
        print(dsrc[7])
        line=14
    if dsrc[8]!=None:
        csrc=['+','-','×','÷']
        nsrc=[(1,2,3,5,6,7),(3,6),(1,3,4,5,7),(1,3,4,6,7),(2,3,4,6),(1,2,4,6,7),(1,2,4,5,6,7),(1,3,6),(1,2,3,4,5,6,7),(1,2,3,4,6,7)]
        stp=int(layout/2)-3
        if dsrc[8]=='+':
            print()#5 line b
            for i in range(3):
                for j in range(stp+2):
                    print(' ',end='')
                print('|')#8 line b
            for i in range(stp-1):
                print(' ',end='')
            print('──┼──')#9 line b
            for i in range(3):
                for j in range(stp+2):
                    print(' ',end='')
                print('|')#12 line b
            print('\n')#14 line b
            line=14
        if dsrc[8]=='-':
            print('\n\n\n')#8 line b
            for i in range(stp-1):
                print(' ',end='')
            print('─────\n\n\n\n\n')#14 line b
            line=14
        if dsrc[8]=='×':
            print('\n')#6 line b
            for i in range(stp):
                print(' ',end='')
            print('╲   ╱')#7 line b
            for i in range(stp+1):
                print(' ',end='')
            print('╲ ╱')#8 line b
            for i in range(stp+2):
                print(' ',end='')
            print('╳')#9 line b
            for i in range(stp+1):
                print(' ',end='')
            print('╱ ╲')#10 line b
            for i in range(stp):
                print(' ',end='')
            print('╱   ╲')#11 line b
            print('\n\n')#14 line b
            line=14
        if dsrc[8]=='÷':
            print('\n')#6 line b
            for i in range(stp+2):
                print(' ',end='')
            print('○\n')#8 line b
            for i in range(stp):
                print(' ',end='')
            print('─────\n')#10 line b
            for i in range(stp+2):
                print(' ',end='')
            print('○\n\n\n')#14 line b
            line=14
        if dsrc[8] not in csrc:
            def skip():
                for i in range(5):
                    print(' ',end='')
            for i in range(stp-1):
                print(' ',end='')
            print('·',end='')
            if 1 in nsrc[dsrc[8]]:
                print('─────',end='')
            else:
                skip()
            print('·')#5 line b
            for j in range(7):
                if j==3:
                    for i in range(stp-1):
                        print(' ',end='')
                    print('·',end='')
                    if 4 in nsrc[dsrc[8]]:
                        print('─────',end='')
                    else:
                        skip()
                    print('·')
                    continue
                for i in range(stp-1):
                    print(' ',end='')
                if j<3:
                    c=2
                else:
                    c=5
                if c in nsrc[dsrc[8]]:
                    print('│',end='')
                else:
                    print(' ',end='')
                skip()
                if c+1 in nsrc[dsrc[8]]:
                    print('|')
                else:
                    print()#6 line b/7/8/9/10/11/12
            for i in range(stp-1):
                print(' ',end='')
            print('·',end='')
            if 7 in nsrc[dsrc[8]]:
                print('─────',end='')
            else:
                skip()
            print('·\n')#14 line b
            line=14
    if dsrc[9]!=None:
        for i in range(14-line):
            print()
        stp=layout-7
        for i in range(stp):
            print(' ',end='')
        print(dsrc[9])
        line=15#15 line b
    if dsrc[10]!=None:
        for i in range(15-line):
            print()
        print(dsrc[10],end='')
    '''绘图完成'''

def start():
    '''开始界面'''
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    dsrc[1]='开始'
    dsrc[3]='推荐模式(M)'
    dsrc[4]='自定义(C)'
    dsrc[9]='返回(R)'
    dsrc[10]='输入功能字母:'
    draw(dsrc)
    met=None
    while True:
        if met=='m' or met=='M':
            recommend()
            draw(dsrc)
            met=None
        elif met=='c' or met=='C':
            custom()
            draw(dsrc)
            met=None
        elif met=='r' or met=='R':
            return
        elif met!=None:
            dsrct=[]
            for i in dsrc:
                dsrct.append(i)
            dsrct[10]='输入错误，输入功能字母：'
            draw(dsrct)
            met=None
        else:
            met=input()

def recommend():
    '''推荐模式界面'''
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    dsrc[1]='推荐模式'
    dsrc[3]='简单(A)'
    dsrc[4]='普通(B)'
    dsrc[5]='复杂(C)'
    dsrc[6]='魔鬼(D)'
    dsrc[7]='大神(E)'
    dsrc[9]='返回(R)'
    dsrc[10]='输入功能字母：'
    met=None
    out=False
    while True:
        if not out:
            draw(dsrc)
        else:
            out=False
        dsrc3=[]
        for i in dsrc:
            dsrc3.append(i)
        dsrc3[3]=dsrc3[4]=dsrc3[5]=dsrc3[6]=dsrc3[7]=None
        mo=['简单','普通','复杂','魔鬼','大神']
        moin=[(5,1,2,2),(5,1,2,1),(10,1,1,1),(15,1,1,0.7),(20,1,0.7,0.5)]
        if met!=None and met!='' and len(met)==1 and (65<=ord(met)<=70 or 97<=ord(met)<=101):
            met3=None
            dsrc3[10]='输入(S)以开始：'
            while True:
                typ=ord(met.upper())-65
#                if typ>4:
#                    dsrc[10]='其他难度敬请期待输入功能字母：'
#                    draw(dsrc)
#                    dsrc[10]='输入功能字母：'
#                    pdb.set_trace()
#                    met=None
#                    out=True
#                    break
                dsrc3[1]=mo[typ]
                dsrc3[2]=f'笔数：{moin[typ][0]}\n位数：{moin[typ][1]}\n显示数字：{moin[typ][2]}s\n显示运算符：{moin[typ][3]}s'
                draw(dsrc3)
                if met3=='s' or met3=='S':
                    game(moin[typ][0],moin[typ][1],moin[typ][2],moin[typ][3])
                    met3=None
                elif met3=='r' or met3=='R':
                    met3=None
                    met=None
                    break
                elif met3!=None:
                    dsrc3[10]='输入错误，输入(S)以开始：'
                    met3=None
                else:
                    met3=input('')
        elif met=='r' or met=='R':
            break
        elif met!=None:
            dsrc[10]='输入错误，输入功能字母：'
            draw(dsrc)
            dsrc[10]='输入功能字母：'
            out=True
            met=None
        else:
            met=input()

def custom():
    '''自定义模式界面'''
    dsrc=[]
    for i in range(11):
        dsrc.append(None)
    dsrc[1]='自定义'
    dsrc[3]='位数：1(更多位数敬请期待)'
    dsrc[4]='笔数(T):'
    dsrc[5]='显示数字(I): s'
    dsrc[6]='显示运算符(U): s'
    dsrc[7]='输入S以开始'
    dsrc[9]='返回(R)'
    dsrc[10]='输入字母+值：'
    met=None
    T=I=U=0
    while True:
        draw(dsrc)
        if met!=None and len(met)>1 and (met[0]=='t' or met[0]=='T'):
            try:
                T=int(met[1:])
                met=None
                dsrc[4]=f'笔数(T):{T}'
            except:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入错误，输入字母+值'
                draw(dsrc)
                met=None
        elif met!=None and len(met)>1 and  (met[0]=='i' or met[0]=='I'):
            try:
                I=int(met[1:])
                met=None
                dsrc[5]=f'显示数字(I):{I}s'
            except:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入错误，输入字母+值：'
                draw(dsrct)
                met=None
        elif met!=None and len(met)>1 and (met[0]=='u' or met[0]=='U'):
            try:
                U=int(met[1:])
                met=None
                dsrc[6]=f'显示运算符(U):{U}s'
            except:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入错误，输入字母+值：'
                draw(dsrct)
                met=None
        elif met=='r' or met =='R':
            return
        elif met=='s' or met=='S':
            try:
                game(T,1,I,U)
            except:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入不全，输入字母+值：'
                draw(dsrct)
            met=None
        elif met!=None:
            dsrct=[]
            for i in dsrc:
                dsrct.append(i)
            dsrct[10]='输入错误，输入字母+值：'
            draw(dsrct)
            met=None
        else:
            met=input()

def game(T,r,I,U):
    '''游戏主界面'''
    dsrc=[None]*11
    t=0
    #预备
    dsrc[1]='预备'
    for i in [3,2,1]:
        dsrc[8]=i
        draw(dsrc)
        time.sleep(1)
    #提示开始
    dsrc[1]='开始'
    dsrc[8]=None
    draw(dsrc)
    time.sleep(1)
    T_range=[]
    for i in range(T):
        T_range.append(random.randint(1,9))#待计算数列
    op_ex=[None,'+','-','×','÷']
    op=[]
    for i in range(T-1):
        op.append(random.randint(1,7))#待运算符列
    ca=[]
    for i in range(len(T_range)):
        ca.append(T_range[i])
        if i!=len(T_range)-1:
            ca.append(op[i])
    r_ans=ca[0]#初始化正确答案
    progress=0
    #开始
    for i in range(len(ca)):
        progress+=1
        if i%2==0:
            dsrc[1]=f'{progress}/{len(T_range)}'
            dsrc[8]=ca[i]
            dsrc[0]=' u'
            if i-1>0:
                if ca[i-1]==1 or ca[i-1]==5:
                    r_ans+=ca[i]
                elif ca[i-1]==2 or ca[i-1]==6:
                    r_ans-=ca[i]
                elif ca[i-1]==3 or ca[i-1]==7:
                    r_ans*=ca[i]
                else:
                    r_ans/=ca[i]
            draw(dsrc)
            time.sleep(I)
        else:
            if ca[i]>4:
                dsrc[8]=op_ex[ca[i]-4]
            else:
                dsrc[8]=op_ex[ca[i]]
            dsrc[0]=' c'
            progress-=1
            draw(dsrc)
            time.sleep(U)
    #显示结束
    d0=datetime.datetime.now()
    dsrc[1]='结束'
    dsrc[2]='（四舍五入一位小数）不足填零0，如(12->12.0，23.456->23.5)计时中…'
    dsrc[8]=None
    dsrc[10]='答案是：'
    u_ans=None
    r_ans=round(r_ans,1)
    while True:
        draw(dsrc)
        if u_ans==r_ans:
            d1=datetime.datetime.now()
            d=d1-d0
            break
        elif u_ans!=None and u_ans!=r_ans:
            d1=datetime.datetime.now()
            d=d1-d0
            break
        else:
            while True:
                met=input()
                try:
                    u_ans=float(met)
                    break
                except:
                    dsrct=[]
                    for i in dsrc:
                        dsrct.append(i)
                    dsrct[10]='输入错误，答案是：'
                    draw(dsrct)
                    met=None
    result(u_ans,r_ans,d,(T,r,I,U))

def result(u_ans,r_ans,d,mod):
    '''显示结果'''
    dsrc=[None]*11
    dsrc[1]='成绩'
    if u_ans==r_ans:
        truth='正确'
    else:
        truth='错误'
    dsrc[2]=f'结果{truth}\n正确答案：{r_ans}\n你的答案：{u_ans}\n思考用时：{round(d.seconds+d.microseconds*0.000001,1)}s\n模式：{mod[0]}笔{mod[1]}位{mod[2]}s(+{mod[3]}s)'
    dsrc[9]='返回(R)'
    dsrc[6]='保存(S)'
    dsrc[10]='输入功能字母：'
    met=None
    saved=False
    draw(dsrc)
    while True:
        if (met=='s' or met=='S') and not saved:
            saved=update(datetime.date.today(),mod,truth,d)
            if not saved:
                dsrc[6]='保存失败，未登录'
            else:
                dsrc[6]='保存成功！'
            met=None
        elif (met=='s' or met=='S') and saved:
            dsrct=[]
            for i in dsrc:
                dsrct.append(i)
            dsrct[10]='已保存，输入功能字母：'
            draw(dsrct)
            met=None
            continue
        elif met=='r' or met=='R':
            break
        elif met!=None:
            dsrct=[]
            for i in dsrc:
                dsrct.append(i)
            dsrct[10]='输入错误，输入功能字母：'
            met=None
            draw(dsrct)
            continue
        else:
            met=input()
        draw(dsrc)

def update(now,mod,truth,d):
    '''保存结果'''
    if os.path.exists('user_info'):
        rfile=open('user_info','r')
        rf=rfile.readlines()
        if rf[2]=='unlocked\n':
            if rf[5]=='\n':
                rf[5]=str(now.year)+'.'+str(now.month)+'.'+str(now.day)+'-'+str(mod)+'-'+truth+'-'+str(d.seconds)+'\n'
            else:
                rf.append(str(now.year)+'.'+str(now.month)+'.'+str(now.day)+'-'+str(mod)+'-'+truth+'-'+str(round(d.seconds+d.microseconds*0.000001,1))+'\n')
            rfile.close()
            file=open('user_info','w')
            file.writelines(rf)
            file.close()
            return True
        else:
            rfile.close()
    return False

def user():
    '''用户界面'''
    dsrc=[None]*11
    dsrc[1]='用户'
    logined=False
    if os.path.exists('user_info'):
        rfile=open('user_info','r')
        rf=rfile.readlines()
        if rf[2]=='unlocked\n':
            logined=True
        rfile.close()
    if logined:
        dsrc[3]='编辑(E)'
        dsrc[4]='分享(S)'
        dsrc[5]='成就(A)'
        dsrc[6]='退出登录(Q)'
        dsrc[7]='注销(D)'
        dsrc[9]='返回(R)'
        dsrc[10]='输入功能字母：'
        draw(dsrc)
        met=None
        while True:
            if met=='e' or met=='E':
                edit()
                met=None
            elif met=='s' or met=='S':
                share(True)
                met=None
            elif met=='a' or met=='A':
                achievement()
                met=None
            elif met=='q' or met=='Q':
                logined=log_out()
                if not logined:
                    break
                met=None
            elif met=='d' or met=='D':
                logined=delete()
                if not logined:
                    break
                met=None
            elif met=='r' or met=='R':
                break
            elif met!=None:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入错误，输入功能字母：'
                draw(dsrct)
                met=None
                continue
            else:
                met=input()
            draw(dsrc)
    else:
        dsrc[3]='登录(L)'
        dsrc[4]='注册(T)'
        dsrc[5]='分享(S)'
        dsrc[9]='返回(R)'
        dsrc[10]='输入功能字母：'
        draw(dsrc)
        met=None
        while True:
            if met=='l' or met=='L':
                logined=log_in()
                if logined:
                    break
                met=None
            elif met=='t' or met=='T':
                logined=register()
                if logined:
                    break
                met=None
            elif met=='s' or met=='S':
                share(False)
                met=None
            elif met=='r' or met=='R':
                break
            elif met!=None:
                dsrct=[]
                for i in dsrc:
                    dsrct.append(i)
                dsrct[10]='输入错误，输入功能字母：'
                draw(dsrct)
                met=None
                continue
            else:
                met=input()
            draw(dsrc)
                

def quitdef():
    '''退出游戏'''
    dsrc=[None]*11
    dsrc[1]='心算能手'
    dsrc[2]='是否退出？'
    dsrc[10]='[Y/n]:'
    draw(dsrc)
    met=None
    while True:
        if met=='Y' or met=='y':
            dsrc[10]='谢谢使用！\n'
            draw(dsrc)
            time.sleep(0.5)
            os.remove('.cwd.tmp')
            exit()
        elif met!=None:
            break
        else:
            met=input()

def edit():
    '''编辑'''
    rfile=open('user_info','r')
    wfile=rfile.readlines()
    rfile.close()
    dsrc=[None]*11
    dsrc[1]='编辑个人信息'
    dsrc[3]=f'(N)登录名：{wfile[1][:-1:]}'
    dsrc[4]='(P)修改密码'
    dsrc[9]='返回(R)'
    dsrc[10]='输入字母+值：'
    draw(dsrc)
    met=None
    while True:
        if met!=None and len(met)>1 and (met[0]=='n' or met[0]=='N'):
            try:
                wfile[1]=met[1:]+'\n'
                dsrc[3]=f'(N)登录名：{wfile[1][:-1:]}'
                met=None
            except:
                dsrc[10]='输入错误，输入字母+值：'
                draw(dsrc)
                dsrc[10]='输入字母+值：'
                met=None
                continue
        elif met!=None and len(met)>1 and (met[0]=='p' or met[0]=='P'):
            try:
                wfilet=hashlib.md5()
                wfilet.update(met[1:].encode(encoding='utf-8'))
                met3=None
                dsrc[10]='输入旧密码以应用新密码：'
                draw(dsrc)
                run=True
                while run:
                    if met3!=None:
                        chm=hashlib.md5()
                        chm.update(met3.encode(encoding='utf-8'))
                        pdb.set_trace()
                        if wfile[0][:-1:]==chm.hexdigest():
                            wfile[0]=wfilet.hexdigest()+'\n'
                            dsrc[10]='修改成功。输入字母+值:'
                            draw(dsrc)
                            dsrc[10]='输入字母+值:'
                            met3=met=None
                            break
                        else:
                            dsrc[10]='密码错误，输入字母+值：'
                            draw(dsrc)
                            dsrc[10]='输入字母+值：'
                            met3=met=None
                            break
                    else:
                        met3=input()
                    draw(dsrc)
                continue
            except:
                pdb.set_trace()
                dsrc[10]='输入错误，输入字母+值:'
                draw(dsrc)
                dsrc[10]='输入字母+值:'
                met=None
                continue
        elif met=='r' or met=='R':
            file=open('user_info','w')
            file.writelines(wfile)
            file.close()
            break
        elif met!=None:
            dsrc[10]='输入错误，输入字母+值：'
            draw(dsrc)
            dsrc[10]='输入字母+值：'
            met=None
            continue
        else:
            met=input()
        draw(dsrc)

def share(dub):
    '''分享'''
    dsrc=[None]*11
    dsrc[1]='分享'
    dsrc[3]='以下为文件路径:'
    cp=os.getcwd()
    exec=None
    conf=None
    AIsear=None
    if os.path.exists('.cwd.tmp'):
        AIsear=open('.cwd.tmp','r').readlines()[0][:-1:]
    if os.path.exists('calc_challenge.py'):
        exec=cp
    elif os.path.exists(AIsear+'/calc_challenge.py'):
        exec=AIsear
    if os.path.exists('user_info'):
        conf=cp
    elif os.path.exists(AIsear+'/user_info'):
        conf=AIsear
    
    dsrc[4]='程序路径：'
    dsrc[5]='用户数据路径：'
    if exec:
        dsrc[4]+=exec
    else:
        dsrc[4]+='未知'
    if dub and conf:
        dsrc[5]+=conf
    else:
        dsrc[5]+='未知'
    dsrc[6]='浏览以上路径以分享'
    dsrc[9]='返回(R):'
    dsrc[10]='输入功能字母：'
    met=None
    draw(dsrc)
    while True:
        if met=='r' or met=='R':
            break
        elif met!=None:
            dsrc[10]='输入错误，输入功能字母：'
            draw(dsrc)
            dsrc[10]='输入功能字母：'
            met=None
            continue
        else:
            met=input()
        draw(dsrc)

def achievement():
    '''成就界面'''
    dsrc=[None]*11
    dsrc[1]='成就'
    rfile=open('user_info','r')
    rf=rfile.readlines()
    acs=rf[5:]
    ac_ind=0
    ac=acs[ac_ind].split('-')
    dsrc[7]='下一页(N)'
    dsrc[9]='返回(R):'
    dsrc[10]='输入功能字母：'
    met=None
    try:
        dsrc[3]='时间:'+ac[0]
        dsrc[4]='模式:'+ac[1]
        dsrc[5]=ac[2]
        dsrc[6]='思考'+ac[3]+'s'
    except:
        dsrc[3]='时间:'
        dsrc[4]='模式:'
        dsrc[5]
        dsrc[6]='思考'+'s'
    draw(dsrc)
    while True:
        if met=='n' or met=='N':
            if ac_ind==len(acs)-1:
                ac_ind=0
            else:
                ac_ind+=1
            met=None
        elif met=='r' or met=='R':
            break
        elif met!=None:
            dsrc[10]='输入错误，输入功能字母：'
            draw(dsrc)
            dsrc[10]='输入功能字母：'
            met=None
            continue
        else:
            met=input()
        try:
            ac=acs[ac_ind].split('-')
            dsrc[3]='时间:'+ac[0]
            dsrc[4]='模式:'+ac[1]
            dsrc[5]=ac[2]
            dsrc[6]='思考'+ac[3]+'s'
        except:
            dsrc[10]='暂无成就，输入功能字母：'
        draw(dsrc)

def log_out():
    '''登出界面'''
    dsrc=[None]*11
    dsrc[1]='退出登录'
    dsrc[3]='是否确认登出？[Y/n]'
    dsrc[10]=':'
    met=None
    draw(dsrc)
    while True:
        if met=='y' or met=='Y':
            rfile=open('user_info','r')
            wfilet=rfile.readlines()
            rfile.close()
            wfilet[2]='locked\n'
            wfile=open('user_info','w')
            wfile.writelines(wfilet)
            wfile.close()
            return False
        elif met!=None:
            return True
        else:
            met=input()
        draw(dsrc)

def delete():
    '''注销界面'''
    dsrc=[None]*11
    dsrc[1]='注销'
    with open('user_info','r') as rfile:
        rf=rfile.readlines()
        dsrc[2]=f'确定要注销用户{rf[1][:-1:]}吗？'
        rp=rf[0][:-1:]
    dsrc[9]='返回(R)'
    dsrc[10]='输入密码以注销用户：'
    draw(dsrc)
    met=None
    met5=None
    while True:
        if met5==rp:
            os.remove('user_info')
            return False
        elif met!=None:
            return True
        else:
            met=input()
            met5=hashlib.md5()
            met5.update(met.encode(encoding='utf-8'))
            met5=met5.hexdigest()

def log_in():
    '''登录界面'''
    dsrc=[None]*11
    dsrc[1]='登录'
    dsrc[3]='用户名(U)：'
    dsrc[4]='密码(P):'
    dsrc[5]='确认(C)'
    dsrc[9]='返回(R):'
    dsrc[10]='输入字母+值:'
    draw(dsrc)
    met=None
    while True:
        if met!=None and len(met)>1 and (met[0]=='u' or met[0]=='U'):
            iu=met[1:]
            met=None
            dsrc[3]='用户名(U)：'+iu
            draw(dsrc)
        elif met!=None and len(met)>1 and (met[0]=='p' or met[0]=='P'):
            met5=hashlib.md5()
            met5.update(met[1:].encode(encoding='utf-8'))
            ip=met5.hexdigest()
            met=None
            dsrc[4]='密码：***'
            draw(dsrc)
        elif met=='c' or met=='C':
            try:
                rfile=open('user_info','r')
                rf=rfile.readlines()
                u_exi=rf[1][:-1:]==iu
                p_exi=rf[0][:-1:]==ip
                rfile.close()
                if u_exi and p_exi:
                    rf[2]='unlocked\n'
                    wf=open('user_info','w')
                    wf.writelines(rf)
                    wf.close()
                    return True
                else:
                    dsrc[10]='输入错误，输入字母+值:'
                    draw(dsrc)
                    dsrc[10]='输入字母+值：'
                    met=None
                    continue
            except:
                dsrc[10]='用户未注册，输入字母+值:'
                draw(dsrc)
                dsrc[10]='输入字母+值：'
                met=None
                continue
        elif met=='r' or met=='R':
            return False
        elif met!=None:
            dsrc[10]='输入错误，输入字母+值:'
            draw(dsrc)
            dsrc[10]='输入字母+值：'
            met=None
            continue
        else:
            met=input()

def register():
    '''注册界面'''
    dsrc=[None]*11
    dsrc[1]='注册'
    dsrc[3]='用户名(U)：'
    dsrc[4]='密码(P):'
    dsrc[5]='确认(C)'
    dsrc[9]='返回(R)'
    dsrc[10]='输入字母+值：'
    draw(dsrc)
    met=None
    while True:
        if met!=None and len(met)>1 and (met[0]=='u' or met[0]=='U'):
            iu=met[1:]
            dsrc[3]='用户名(U):'+iu
            draw(dsrc)
            met=None
        elif met!=None and len(met)>1 and (met[0]=='p' or met[0]=='P'):
            met5=hashlib.md5()
            met5.update(met[1:].encode(encoding='utf-8'))
            ip=met5.hexdigest()
            dsrc[4]='密码:'+met[1:]
            draw(dsrc)
            met=None
        elif met=='c' or met=='C':
            if os.path.exists('user_info'):
                with open('user_info','r') as rfile:
                    rf=rfile.readlines()
                    if iu==rf[1]:
                        dsrc[10]='用户已存在，输入字母+值：'
                        draw(dsrc)
                        dsrc[10]='输入字母+值：'
                        met=None
                        continue
                    else:
                        dsrc[10]='已存在用户文件，注销或删除文件以注册，输入字母+值：'
                        draw(dsrc)
                        dsrc[10]='输入字母+值：'
                        met=None
                        continue
            else:
                try:
                    wft=[ip,iu,'unlocked','','35','']
                    wft2=[]
                    for i in wft:
                        wft2.append(i)
                        wft2.append('\n')
                    with open('user_info','w') as wf:
                        wf.writelines(wft2)
                    return True
                except:
                    dsrc[10]='输入错误，输入字母+值：'
                    draw(dsrc)
                    dsrc[10]='输入字母+值：'
                    met=None
        elif met=='r' or met=='R':
            return False
        elif met!=None:
            dsrc[10]='输入错误，输入字母+值：'
            draw(dsrc)
            dsrc[10]='输入字母+值：'
            met=None
        else:
            met=input()

if __name__=='__main__':
    cp=os.getcwd()
    wp=None
    while True:
        try:
            if wp!=None and wp!='' and os.path.exists(wp):
                print(os.path.abspath(wp))
                confirmt=input('输入Y以确认：')
                if confirmt=='y' or confirmt=='Y':
                    os.chdir(wp)
                    break
            elif wp=='':
                break
            elif wp!=None:
                wp=print('输入错误，',end='')
        except:
            wp=print('输入错误，',end='')
        wp=input(f'输入工作路径(留空以默认{os.getcwd()}):')
    with open('.cwd.tmp','w') as file:
        file.write(cp+'\n')
        file.write(os.getcwd()+'\n')

    while True:
        main()
else:
    print('请直接在控制台运行！')
