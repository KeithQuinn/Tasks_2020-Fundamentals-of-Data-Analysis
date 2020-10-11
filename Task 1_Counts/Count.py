mylist = [1, 2, 5, 4, 1, 1, 3, 2, 1, 1, 1, 'e', 'e']

mydict = {}

for i in range (len(mylist)):
    mydict[mylist[i]] = mylist.count(mylist[i])
    print(mydict)

print(mydict)
