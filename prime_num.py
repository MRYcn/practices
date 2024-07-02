#encoding=utf-8
def main():
    while True:
        print('---------------------------------')
        print('      质数')
        try:
            innum=int(input('输入正整数(输入0以退出)'))
        except:
            print('输入不规范，请重新输入。')
            continue
        if innum==0:
            print('谢谢使用。')
            exit()
        elif innum>0:
            outnum=calc(innum)
            if outnum==0:
                print('1×',innum,'=',innum)
            else:
                print('1',end='')
                for i in outnum:
                    print('×',i,end='')
                print('=',innum)
        else:
            print('数字＜0')

def calc(num):
    if num==1:
        return 0
    elif num==2:
        return 0
    sq=[]
    st=False
    for left in range(1,num):
        for right in range(0,num):
            if left<=right and left*right==num and not(st):
                sq.append(left)
                sq.append(right)
                st=True
    if sq==[]:
        return 0
    if calc(sq[1])!=0:
        ch=calc(sq[1])
        sq.pop(1)
        for i in ch:
            sq.append(i)
    return sq

if __name__=='__main__':
    main()