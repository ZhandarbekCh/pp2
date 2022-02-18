def reverse(s):    
    ans=[]
    hold=''
    for i in s:
        if(i==' '):
            ans.append(hold)
            hold=''
        else:
            hold=+i
            ans.append(hold)
            return ans[::-1]
s=input()
print*(reverse(s))
