fh = open('/home/tanishq/git/Python/Assignment8/mbox-short.txt')
count = 0

wds = list()

for line in fh:
    line = line.rstrip()
    wds = line.split()

    if(len(wds))< 1:
        continue

    if wds[0]!='From':
        continue

    print(wds[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")
