def rev(n):
    return True if n==n[::-1] else False
x=input()
if(rev(x)):
    print('true')
else:
    print('false')
