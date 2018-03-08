# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x=0
line1=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x+=1
    line = line.rstrip()
    line = line[20:]
    line = float(line)
    line1 = line1 + line 
    #print(line1/x)

print("Average spam confidence:",line1/x)
