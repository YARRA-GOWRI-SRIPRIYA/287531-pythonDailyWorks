t=(1,3,4,31,1,3)
l=[]
for i in t:
    if t.count(i)>1:
        l.append(i)
l=set(l)
for i in l:
    print(i,end=" ")
       