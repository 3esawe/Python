import string
try:
    x= open("C:\\Users\\OMAR\Desktop\\New Text Document.txt",'r')
except:
    print("Error path")
common = dict()
for i in x :
    list = i.split(" ")
    for word in list:
        common[word] = common.get(word,0)+1
geart = None
words = None
for key,value in common.items():
    if geart is None or value > geart:
        geart =value
        words = key
#9.4

mbox = open("C:\\Users\\OMAR\\Desktop\\mbox-short.txt")
def word (word):
    dictm = dict()
    for i in mbox:
        if i.startswith("From "):

             list = i.split(" ")
             dictm[list[1]] = dictm.get(list[1],0)+1


    maxword = None
    maxcount = None
    for key , value in dictm.items():
        if maxcount is None or maxcount < value:
            maxcount = value
            maxword = key

    print(maxword, maxcount)
    return dictm

word(mbox)
# advanced text parsing

rome = open("C:\\Users\\OMAR\\Desktop\\romeo.txt")
counts = dict()
for line in rome:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

