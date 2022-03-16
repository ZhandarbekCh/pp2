from os import read


file=open('hello world.txt','r')
cnt=0
read=file.read()
line=read.split('\n')
for i in line:
    if i:
        cnt+=1
print(cnt)
