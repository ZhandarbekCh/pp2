def filter_prime(x):
    ans=[]
    for i in range(len(x)):
        count=True
        for j in range(2,int(x[i])//2+1):
            if(int(x[i])%j==0):
                count=False
                break
        if(count):
            ans.append(int(x[i]))
    return ans


def Fah(f):
    C=(5/9)*(f-32)
    return C
