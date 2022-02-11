n = list(map(int, input().split())) 
l = None 

if len(n) <= 1: 
    l = int(input()) 

if l is None: 
    l = n[1] 
n = n[0] 
a = [(l+2*i) for i in range(n)] 

if n == 1: 
    print(l) 
    exit(0) 
b = a[0]^a[1] 

for i in range(2, n): 
    b = b^a[i] 

print(b)