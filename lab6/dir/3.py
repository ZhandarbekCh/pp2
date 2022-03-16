import os
path='C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\forprob'
if os.path.exists(path):
    print("Exits\nFile name:",os.path.basename(path))
    print("Dir and files in path: ", os.listdir(path))
else: print("NO")
