'''
srt++tring is data type
it will containe any type of charecter
methids are:upper,lower,index,count,replace,strip,lstrip,rstrip,startswith,endswith,split,join,
'''

#upper
#lower
#strip
str1="yousuf"
str2="wfuehfuhiquehqukiewhifhwihioifwehioehofiwe"
print(str1.index("u"))

print(str1.count("u"))
print(str1.count("f"))



print(str2.count("e"))


out=str1.replace("u","U",2)
print(str1)
print(out)


#it will remove whitespaces space,newline,tab
str3="    sssjkenfjen wnifwoih4e   benen   addd"

out=str3.strip()
out=str3.lstrip()
out=str3.rstrip()
print(out)


#split

out=str1.split("o")
out=str1.split("u") #output list format
print(out)
str4="8990"
print(str4,type(str4))
out=str4.isdigit()
print(out)
out=int(str4)
print(out,type(out))