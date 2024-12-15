fr=open("data.txt")
fr.seek(9,0)
print(fr.read())
print("######")
print(fr.tell())

fr.seek(0,2)
print(fr.tell())

fr.close()