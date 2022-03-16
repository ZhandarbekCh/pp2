import os
path='C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\del_file.txt'
if os.access(path,os.F_OK):
    os.remove('del_file.txt')
    print('File deleted')
else:
    print('File do not exits')
    a=open('del_file.txt', 'x')
