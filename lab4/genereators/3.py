def check(y):
    i=0
    while(i<=y):
        if((i%3==0) & (i%4==0)):
            yield i
        i+=1
y=int(input())
for i in check(y):
    print(i)
