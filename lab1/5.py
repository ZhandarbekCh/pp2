n = input().split()
x=int(n[0])
y=int(n[1])
z=0
for i in range(2, int(x/2) +1):
    if x % i == 0:
        z+=1
        break
if(x<500 and z==0 and y%2==0):
    print("Good job!")
else :
    print("Try next time!")