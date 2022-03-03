def evens(i,y):
    while(i<=y):
        if(i%2==0):
            yield i
        i+=1
i=int(input())
y=int(input())
for i in evens(i,y):
    print(i)
