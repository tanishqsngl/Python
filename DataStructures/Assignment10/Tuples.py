fh = open('/home/tanishq/git/Python/DataStructures/Assignment10/mbox-short.txt')

wrds = dict()
lst = list()
lst1 = list()
wds = list()

for line in fh:
    line = line.rstrip()
    wds = line.split()

    if(len(wds))< 1:
        continue

    if wds[0]!='From':
        continue
    else:
        wds=wds[5].split(':')
        lst.append(wds[0])

for words in lst:
    wrds[words] = wrds.get(words,0) + 1

for key,val in wrds.items():
    newtup = (key,val)
    lst1.append(newtup)

lst1 = sorted(lst1)

for val,key in lst1:
    print(val,key)