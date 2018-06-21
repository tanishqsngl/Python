fh = open('/home/tanishq/git/Python/Assignment9/mbox-short.txt')

wrds = dict()
lst = list()
wds = list()

for line in fh:
    line = line.rstrip()
    wds = line.split()

    if(len(wds))< 1:
        continue

    if wds[0]!='From':
        continue
    else:
        lst.append(wds[1])

for words in lst:
    wrds[words] = wrds.get(words,0) + 1

bigCount=None
bigWord=None
for word,count in wrds.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print(bigWord,bigCount)
