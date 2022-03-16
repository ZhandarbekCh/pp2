list=input().split()
with open('for_writeList.txt','w') as file:
    for i in list:
        file.write('%s\n' % i)
file=open('for_writeList.txt')
print(file.read())
