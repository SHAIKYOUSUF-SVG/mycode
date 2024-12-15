#seek :used to move cursor from the point
#tell:used to get the cursor position


with open ("data.txt") as fr:
    print(fr.tell())
    fr.readline()
    print(fr.tell())
    #move the cursor from anywhere to beggining of file
    fr.seek(0,0)  #seek takes 2 arguments first 0 is how much to move and another 0 is from where
    print(fr.tell())
    fr.seek(2,0)


    print(fr.tell())


