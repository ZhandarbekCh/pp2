import os
print ("Existence:", os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\hello world.txt', os.F_OK))
print ("Readability:", os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\hello world.txt', os.R_OK))
print ("Writability:", os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\hello world.txt', os.W_OK))
print ("Executability:", os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\pp2\\lab6\\direct\\hello world.txt', os.X_OK))
