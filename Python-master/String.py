index = 0
word = 'banana'

while index < len(word):
    print(index, word[index])
    index = index +1
for  i in word :
    print(i)
count = 0
for i in range(len(word)):
        if ((word[i:i+3] =="ban")):
             count = count +1
print(range(len(word)))

# Slicing String
text = "X-DSPAM-Confidence:    0.8475";
x =text.find('0')
print(text[x:])
