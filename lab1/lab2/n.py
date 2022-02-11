a, b, x = [], [], int(input()) 
while x != 0: 

    a.append(x) 
    x = int(input()) 
j = len(a)-1 

for i in range(len(a)//2): 
    b.append (a[i] + a[j]) 
    j -= 1 

if(len(a) %2 == 1): 
    
    b.append(a[len(a)//2]) 
print(*b)