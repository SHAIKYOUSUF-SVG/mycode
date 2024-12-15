fw=open('inp.txt','w')
fw.write('1\n')
fw.write('2\n')
fw.write('3\n')
out=fw.tell()
fw.close()
print(out)
print(fw.closed)

