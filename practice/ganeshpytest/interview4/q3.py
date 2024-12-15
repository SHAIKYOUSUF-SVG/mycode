#what is differnec of test file nd binary fiel?
#different modes of opeartions:r,w,a,r+(read and write),rb(readbinary),wb(writebinary)
'''
with open("out.txt","w") as fw:
    fw.write("hi,this is yousuf")
'''

#to write in binary

fw=open("out2.txt","wb")  #wb means write in binary
fw.write(b"\x74\x65\x73\x74") #(b means binary  and for every letter we need to write \x befpre letter)
fw.close()

#for alphabet have binary values