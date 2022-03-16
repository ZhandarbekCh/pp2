for i in range(65,90):
    with open(chr(i) + ".txt","w") as file:
        file.writelines(chr(i))
