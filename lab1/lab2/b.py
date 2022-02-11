n=int(input())
max=0
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]*a[j]>max:
            max=a[i]*a[j]
print(max)