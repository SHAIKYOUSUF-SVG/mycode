fr=open("r+.txt", "r+")
out=fr.read()
fr.write("hi\n")
fr.write("hello\n")
fr.close()

print(out)