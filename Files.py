handle = open("C:\\Users\\OMAR\Desktop\\mbox-short.txt","r")
x= handle.read()
y = handle.readline()
ssum = 0
nline = 0

for i in range(len(x)):

     if x[i:].startswith('X-DSPAM-Confidence:'):

         span = float(x[i+20:i+26])
         ssum += span
         nline += 1

print("Average spam confidence:",ssum/nline)
