#10.2
try:
    x= open("C:\\Users\\OMAR\Desktop\\mbox-short.txt",'r')
except:
    print("Error path")
Dict = dict()
List = list()
newList= list()
for i in x :
    if i.startswith("From ") :
        i = i.strip()
        List   = i.split()
        x =List[5]
        Dict[x[0:2]] = Dict.get(x[0:2], 0) +1
tup = sorted(Dict.items())
for k ,v in tup :
    print(k,v)
print(f'dict is {Dict}')