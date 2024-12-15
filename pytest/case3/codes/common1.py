def common(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

def uniq(obj):
    uniq_list=[]
    for i in obj:
        #if i not in uniq_list:
        if i  in uniq_list: #wrote wrong for getting failed test case
            uniq_list.append(i)
    return uniq_list