filename = input("What file would you like to open?\n")

file1 = open(filename + ".ann_tuple")
file2 = open("wsj_1041_2.txt")
file3 = open("wsj_1041_3.txt")

mappings = {}
for line in file3:
    mappings[line] = []
    
linesFile2 = []
for line in file2:
    linesFile2.append(line.split("\t"))

linesFile1 = []
for line in file1:
    linesFile1.append(line.split("\t"))


for i in range(len(linesFile1)-1):
    for key in mappings:
        if linesFile1[i][8].lower() in key.lower():
            mappings[key].append(linesFile1[i])

for i in range(len(linesFile2)-1):
    for key in mappings:
        if linesFile2[i][6].lower() in key.lower():
            mappings[key].append(linesFile2[i])

for key in mappings:
    if len(mappings[key]) > 2:
        print(key, mappings[key])

