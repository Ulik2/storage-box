fname = input('Enter file name : ')
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    print(line.upper())
    end = '-0500'
    if end in line:
        break
