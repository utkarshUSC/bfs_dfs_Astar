f1 = open("output.txt", "r")
f2 = open("output10.txt", "r")
lines1=[]
lines2 = []
for each_line in f1:
    lines1.append(each_line)
for each_line in f2:
    lines2.append(each_line)
f1.close()
f2.close()

for i in range(0, len(lines2)):
    if lines1[i]!=lines2[i]:
        print(lines1[i], lines2[i])
        break
