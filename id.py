#import io
#import sys
#import os
#os.sys('set $PYTHONIOENCODING=utf-8')
#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ag=0
while ag==0:
        print('\n  Identifier Check Code Calculator\n')
        a=input('Please input identifier(first 17):\n')
        a=int(a)
        
        '''
        get number
        '''
        
        #17
        b=a%10
        b =int(b)
        b=b*2
        #16
        c=(a/10)%10
        c=int(c)
        c=c*4
        #15
        d=(a/100)%10
        d=int(d)
        d=d*8
        #14
        e=(a/1000)%10
        e=int(e)
        e=e*5
        #13
        f=(a/10000)%10
        f=int(f)
        f=f*10
        #12
        g=(a/100000)%10
        g=int(g)
        g=g*9
        #11
        h=(a/1000000)%10
        h=int(h)
        h=h*7
        #10
        i=(a/10000000)%10
        i=int(i)
        i=i*3
        #9
        j=(a/100000000)%10
        j=int(j)
        j=j*6
        #8
        k=(a/1000000000)%10
        k=int(k)
        k=k*1
        #7
        l=(a/10000000000)%10
        l=int(l)
        l=l*2
        #6
        m=(a/100000000000)%10
        m=int(m)
        m=m*4
        #5
        n=(a/1000000000000)%10
        n=int(n)
        n=n*8
        #4
        o=(a/10000000000000)%10
        o=int(o)
        o=o*5
        #3
        p=(a/100000000000000)%10
        p=int(p)
        p=p*10
        #2
        q=(a/1000000000000000)%10
        q=int(q)
        q=q*9
        #1
        r=(a/10000000000000000)%10
        r=int(r)
        r=r*7
        
        '''
        plus number
        '''
        
        s=b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r
        
        #output
        s=s%11
        s=int(s)
        if s==1:
                print('Your check code is \n  0')
        elif s==0:
                print(' Your check code is\n  1')
        else:
                s=12-s
                print(' Your check code is ')
                if s==10:
                    print('X')
                else:
                    print(s)
                print('\n')
        ag=input(' Calculate again?\n 0 to again ,1 to exit:\n')
        ag=int(ag)