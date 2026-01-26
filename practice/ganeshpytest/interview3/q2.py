'''
by using with key word
we dont need to close the file soecially
by using with keyword it will automatically close the file
'''
#fr=open("data.txt)
with open("data.txt") as fr:
    out=fr.read()
print(out)
print("#########")
print(fr.closed)