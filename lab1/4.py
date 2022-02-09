n=int(input())
x= input()
if (x=='b'):
    print(n*1024)
if(x=='k'):
    y=int(input())
    l="{:."+str(y)+"f}"
    print(l.format(n/1024))