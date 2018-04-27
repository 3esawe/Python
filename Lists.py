# 8.4
x = open("C:\\Users\OMAR\\Desktop\\romeo.txt")
words = list()
for i in x:
     list = i.rstrip().split(" ")
     for word in list:
         if word in words :
             continue
         else:
            words.append(word)
print(sorted(words))

#8.5
count = 0
y = open("C:\\Users\\OMAR\\Desktop\\mbox-short.txt","r")
for i in y  :
    if i.startswith('From:'):
        list = i.strip().split(" ")
        print(list[1])
        count = count +1

print("There were", count, "lines in the file with From as the first word")
