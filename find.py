fhand =open("from.txt")
for line in fhand:
    line=line.rstrip()
    if line.find("From") >=0:
        print(line)

    