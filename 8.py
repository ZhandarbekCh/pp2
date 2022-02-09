n=str(input())
z=input()
x=n.find(z)
y=n.rfind(z)
if(x==y):
    print(x)
else:print(x, y)