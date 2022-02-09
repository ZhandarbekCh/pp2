n=input().split()
b=[]
for i in n:
    if len(i)>=3:
        b.append(i)
        x=" ".join(b)
print(x)