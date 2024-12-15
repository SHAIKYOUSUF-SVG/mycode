with open('inp.txt','r+') as fw:
    out=fw.read()
    print(out)
    print(fw.closed)
    print(fw.mode)
    print(fw.name)
    fw.write('hi yousuf \n')
    fw.write('how are you')