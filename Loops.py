# while True :
#     line = input('> ')
#     if line == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('done')
#
# friends = ['omar' , 'ali', 'bani issa']
# for i in friends :
#     print('my name is ' , i)
list1 = [5,2,1,43,12]
largest = list1[0]
x = False
for i in list1 :
    if i == 2 :
      x = True
    print( x , i)
    x= False

minimum = None
maximum = None

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break

    try:
        num = int(inp)
    except:
        print ('Invalid input')
        continue

    if minimum is None or num < minimum:
        minimum = num

    if maximum is None or num > maximum:
        maximum = num

print ('Maximum:', maximum)
print ('Minimum:', minimum)


minimum = None
maximum = None

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break

    try:
        num = int(inp)
    except:
        print ('Invalid input')
        continue

    if minimum is None or num < minimum:
        minimum = num

    if maximum is None or num > maximum:
        maximum = num

print ('Maximum:', maximum)
print ('Minimum:', minimum)