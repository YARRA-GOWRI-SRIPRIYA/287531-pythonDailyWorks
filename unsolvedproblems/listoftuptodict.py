def convert(tup,di):
    for a,b in tup:
        di.setdefault(a,[]).append(b)
    return di
tups=[("akash",10),("suraj",20),("akhil",25)]
dictionary={}
print(convert(tups,dictionary))