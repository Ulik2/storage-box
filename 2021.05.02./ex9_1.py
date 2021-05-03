fname = input('Enter a file')
if len(fname) < 1 : fname = "clown.txt"
fhand = open(fname)

dic = dict()
for line in fhand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    print(wds)
    for w in wds:
        if w in dic:
            dic[w] = dic[w] + 1
        else:
            dic[w] = 1
        #print(w,dic[w])

bigword = None
bigcount = None
for  word,count in dic.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
