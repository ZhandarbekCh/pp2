def square():
    i=2
    y=int(input())
    while(i<=y):
        yield i**2
        i+=1

for j in square():
    print(j)
