with open('ctrlC.txt', 'r') as first,open('ctrlV.txt', 'a') as second:
    for i in first:
        second.write(i)
