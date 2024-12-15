
#converting list to dict usinf 2line for loop
data=["inida","uk","france","gwrmany"]

#{india:5,uk:2,france:6,germany:7}

#[["india",5],["uk",2],["france",6],["germany",7]  we can covert this dict easily

out=[[i,len(i)] for i in data]
print(dict(out))