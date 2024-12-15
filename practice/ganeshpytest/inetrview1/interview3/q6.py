#reading from a file and writting to same file
#'r+' is used to read and write also same time

with open("data.txt","r+")as fr:
    print(fr.read())
    fr.write("\nitaly\n")
    fr.write("yousuf")
    fr.read()