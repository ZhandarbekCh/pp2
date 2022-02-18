class MyClass:
    def __init__(self,x):
        self.x=x
    def printString(self):
        print(self.x)
def getString():
        n=input()
        return n

a = MyClass(getString())

a.printString()
