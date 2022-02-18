def filter(arr):
    result=[]
    for i in arr:
        ans=True
        for j in range(2,i//2+1):
            test = checking(j)
            if(test(i)==0):
                ans=False
                break
        if(ans):
            result.append(i)
    return (result)

def checking(j):
    x=lambda n: n % j 
    return x

arr=list(map(int,input().split()))
print(filter(arr))
