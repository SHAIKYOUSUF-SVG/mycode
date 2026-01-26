import re

fr=open("file2.txt","r")
country=""
for i in fr:
    i=i.strip()

    exp1="^=+\s*([a-zA-Z]+)\s*=+$"
    o1=re.search(exp1,i)
    if o1:
        #print(o1.group(1))
        country=o1.group(1)
        print(f"country is {country}")
    exp2="^[a-z]{3}\s*:\s*(\d+)$"
    o2=re.search(exp2,i)
    if o2:
        print(i)
    exp3="^=+$"
    o3=re.search(exp3,i)
    if o3:
        print(f"end of country {country}")
fr.close()