def histogram(h):

    for i in h:
        while int(i)!=0:
            i=int(i)-1
            print("*",end='')
        print()

h=(input().split())
print(histogram(h))
