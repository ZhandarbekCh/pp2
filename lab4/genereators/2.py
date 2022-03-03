def evens(y):
    i=0
    while(i<=y):
        if(i%2==0):
            yield i
        i+=1
y=int(input())
for i in evens(y):
    print(i)
