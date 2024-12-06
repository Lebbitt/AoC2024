file = open("data/Day1.txt").read()
file_strip = file.strip()
file_list = file_strip.split("\n")

list_1 = []
list_2 = []

for f in file_list:
    line = f.split("   ", 1)
    list_1.append(line[0])
    list_2.append(line[1])

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

totals = []
for number in sorted_list_1:
    #print(number)
    count = 0
    for number_l2 in sorted_list_2:
        #print(number_l2)
        if (int(number)==int(number_l2)):
            count += 1
        else:
            pass
       #print(count)
    total = count * int(number)
    totals.append(total)
    print(totals)

answer = sum(totals)
print(answer)

