fh = open('/home/tanishq/git/Python/Assignment8/romeo.txt')
lst = list()
words = list()
for line in fh:
    line = line.rstrip()
    words=line.split()
    for i in range(len(words)):
        if words[i] in lst:
            continue
        else:
            lst.append(words[i])
lst.sort()
print(lst)

