#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import os
import datetime
import time
import requests

def main():
    while True:
        print('================================')
        print('--------------------------------')
        print('       加密聊天系统(KCS)')
        print('  1.Help(帮助)')
        print('  2.Send messages(发送信息)')
        print('  3.Receive messages(接收信息)')
        print('  4.About(关于)')
        print('  5.Settings(设置)')
        print('  6.Quit(退出)')
        mode=int(input(' Please enter a number to launch its method(请输入功能数字):'))
        print('--------------------------------')
        if mode==1:
            helpdef()
        elif mode==2:
            send()
        elif mode==3:
            receive()
        elif mode==4:
            about()
        elif mode==5:
            setdef()
        elif mode==6:
            quit_bool=input('Really quit(是否退出)? y/n')
            if quit_bool=='y' or quit_bool=='Y':
                print('Thanks for your use(谢谢使用)!')
                exit()
            else:
                continue
        else:
            print('Error number(错误数字)')


def about():
    print('        About')
    print('Program name: Key In/Out-Chatting System')
    print('Version:1.0.0')
    print('Released time:2023.9.8')
    print('Programmed by:MRY')
    print('Contaction:yrk2021***@outlook.com')


def helpdef():
    print('        Help')
    print('This program only works on some avaiable devices/systems/versions:')
    print('Available systems:Windows,Linux,Android(with Python),iOS(with Python on iSH/LibTerm,etc.)')
    print('Available devices types: computers(with Windows/Linux),mobile phones(with Android), iPhone/iPad(with iOS)')
    print('Available version: Python 3.x')
    print('If your device is not available unlikely, you may use virtual machine to emulate the available environment.')
    print('--------------------------------------')
    print('Support language: English')
    print("Support connection:WLAN,Internet(If the connection you use is WLAN and is diffrent from the WLAN name your partner connects,I'm sorry but it's not supported")
    print('--------------------------------------')
    print('       Guidance')
    print("Enter a number and press enter to choose the method. You will be asked to input the text. You'd like to send. Also you should input the password to unlock or lock the text while sending and receiving. If you enter a wrong password, the text it shows cannot be understood.")
    print('Have a good time chatting!')
    print('Modified by MRY')

def cfile():
    print('当前工作目录：',os.getcwd())
    chdir=input('输入要进入的目录:(回车以取消更改)')
    if chdir:
        try:
            os.chdir(chdir)
        except:
            print('Changing failed')
    print(os.lsdir())
    chofile=input('Choose a file with its full name:')
    if not os.path.exists(chofile):
        print('File not exist')
    else:
        with open(file=chofile,mode='r') as rfile:
            rfile=rfile.read()
    return rfile


def modify():
    print('--------------------------------')
    print('Tips: Please only input in English. Any character is OK. If you want to rinput or cancel, you can choose the method later.')
    while True:
        text=input('Message:\n')
        print('Confirm text:\n',text)
        cfirm=input('y:confirm; n:reinput; c:cancel (Default: reinput)')
        if cfirm=='y' or cfirm=='Y':
            return text
        elif cfirm=='c' or cfirm=='C':
            return
        else:
            continue

def keyin(text):
    key=int(input('Please input your key (Enter not to lock): '))
    print('Locking...',end='')
    i=0
    text_len=len(text)
    while i+1<=text_len:
        if 'a'<=text[i]<='z':
            text[i]=chr(ord(text[i])+key)
    print('Success')
    return text

def keyout(text):
    key=int(input('Please input your key (Enter not to unlock):'))
    print('Unlocking...',end='')
    i=0
    text_len=len(text)
    while i+1<=text_len:
        if 'd'<=text[i]<='z' or 123<=ord(text[i])<=125:
            text[i]=chr(ord(text[i])-key)
    print('Success')
    return text

def send():
    print('         Send Messages(发送信息)')
    writer=input('Writer (your nickname or realname):')
    receiver=input('Receiver (his/her nickname or realname):')
    receiver_ip=input("Receiver's IP address (Please input as: http://xxx.xxx.xxx.xxx:xxx)\n:")
    try:
        headers={'User-Agent':'KCS'}
        url=receiver_ip
        resp_g=requests.get(headers=headers,url=url)
        resp_p=requests.post(url=url,data={'data':'test'})
      #  if resp_g:#: #and resp_p.ok :
       #     pass
      #  else:
       #     print(f'Server error. Get type:{resp_g.ok}. Post type:{resp_p.ok}')
       #     print(' Maybe target server is not currently open?  Please try again.')
       #     return
    except:
        print(' Something went wrong. Maybe your network is not connected, or your version is not available.')
        return
    print('    1: choose a file')
    print('    2: input text')
    method=int(input('choose a method:'))
    if method==1:
        text=cfile()
    elif method==2:
        text=modify()
    if text=='':
        print("You didn't imput anything. Please try again.")
        return
    text='writer:'+writer+'\nreceiver:'+receiver+'\ntext:\n'+text
    with open('int.tmp','w') as wfile:
        wfile.write(text)
    data={'data':('int.tmp',open('int.tmp','r'))}
    resp=requests.post(url=url,files=data,headers=headers)
    time.sleep(1)
    if not resp.ok:
        print('Sending failed. please try again.')
    else:
        print('Message sent.')

def receive():
    print('----------------------------------')
    print('Input any key and enter to cancel waiting.')
    print('Waiting to receive files...',end='')
    d1=datetime.datetime.now()
    # os.popen('read name | echo > ctmp.tmp')
    while True:
        d2=datetime.datetime.now()
        d=d2-d1
        if os.path.exists('ctmp.tmp'):
            print('Waiting cancelled.')
            return
        elif os.path.exists('int.tmp'):
            print('---',end='')
            print('Received')
            break
        elif d.seconds>=1:
            print('.',end='')
    input('Enter to show text:')
    if os.path.exists('ctmp.tmp'):
        os.system('rm ctmp.tmp')
    with open('int.tmp','r') as rfile:
        print('----------------------------')
        print(rfile.read())
        print('----------------------------')
    input('Enter to return:')

def setdef():
    print('-------------------------------')
    print('Current working directory:',os.getcwd())
    chdir_bool=input('input y to change directory:')
    if chdir_bool=='y' or chdir_bool=='Y':
        chdir=input('input directory to go to:')
        os.chdir(chdir)
        if os.path.exists('int.tmp'):
            os.system('rm int.tmp')
        if os.path.exists('ctmp.tmp'):
            os.system('rm ctmp.tmp')
        print('Current working directory:',os.getcwd())

if __name__=='__main__':
    setdef()
    if os.path.exists('int.tmp'):
        os.system('rm int.tmp')
    if os.path.exists('ctmp.tmp'):
        os.system('rm ctmp.tmp')
    try:
        #os.popen('python -m http.server 8080')
        os.popen('python /sdcard/com.hipipal.qpyplus/sock.py')
    except:
        print('Your version is not available.')
        exit()
    helpdef()
    main()
else:
    print('请直接在控制台运行！')